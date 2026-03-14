#!/usr/bin/env python3
"""
Apollo.io Integration para Ley 21.719
Busqueda de prospectos por sector para cumplimiento de proteccion de datos
"""

import csv
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests
import structlog

logger = structlog.get_logger()

# =============================================================================
# CONFIGURACION MULTI-SECTOR LEY 21.719
# =============================================================================

SECTOR_CONFIGS_LEY21719 = {
    "fintech": {
        "target_titles": [
            "CEO", "CTO", "CFO", "COO",
            "Compliance Officer", "Chief Compliance Officer",
            "Gerente Legal", "Director Legal",
            "Risk Manager", "Gerente de Riesgos",
            "CISO", "Chief Information Security Officer",
            "DPO", "Data Protection Officer"
        ],
        "company_keywords": [
            "fintech", "pagos", "lending", "crypto", "neobank",
            "wallet", "credito", "prestamo", "factoring",
            "crowdfunding", "insurtech", "regtech"
        ],
        "priority": 1,
        "risk_level": "ALTO",
        "data_sensitivity": "Datos financieros sensibles",
        "urgency_message": "CMF y nueva Ley 21.719 exigen compliance inmediato"
    },
    "salud": {
        "target_titles": [
            "Director Medico", "Director General",
            "Gerente General", "CEO",
            "Jefe TI", "Director TI", "CTO",
            "Encargado Calidad", "Director Calidad",
            "Gerente Operaciones", "COO",
            "Director Administrativo"
        ],
        "company_keywords": [
            "clinica", "laboratorio", "hospital",
            "telemedicina", "salud", "medico",
            "diagnostico", "farmacia",
            "isapre", "prestador", "centro medico"
        ],
        "priority": 2,
        "risk_level": "MUY ALTO",
        "data_sensitivity": "Datos de salud = categoria especial",
        "urgency_message": "Datos sensibles requieren consentimiento EXPLICITO"
    },
    "retail": {
        "target_titles": [
            "CEO", "Gerente General",
            "CMO", "Director Marketing", "Gerente Marketing",
            "Director Fidelizacion", "Gerente CRM",
            "Director Comercial", "Gerente Comercial",
            "CTO", "Director TI",
            "Director Operaciones"
        ],
        "company_keywords": [
            "retail", "ecommerce", "e-commerce", "supermercado",
            "tienda", "multitienda", "farmacias", "farmacia",
            "moda", "vestuario", "electrodomesticos",
            "marketplace", "delivery"
        ],
        "priority": 3,
        "risk_level": "ALTO",
        "data_sensitivity": "Alto volumen de datos de consumidores",
        "urgency_message": "Programas de fidelizacion bajo escrutinio regulatorio"
    },
    "educacion": {
        "target_titles": [
            "Rector", "Rectora",
            "Director General", "Directora General",
            "Vicerrector", "Vicerrectora",
            "Gerente TI", "Director TI",
            "Director Academico", "Directora Academica",
            "Gerente Administracion", "Director Finanzas"
        ],
        "company_keywords": [
            "universidad", "colegio", "instituto",
            "educacion", "escuela",
            "academia", "capacitacion", "formacion",
            "preuniversitario", "postgrado"
        ],
        "priority": 4,
        "risk_level": "ALTO",
        "data_sensitivity": "Datos de menores y academicos",
        "urgency_message": "Proteccion especial para datos de menores de edad"
    }
}

DEFAULT_TITLES_LEY21719 = [
    "CEO", "CTO", "CFO", "COO",
    "Gerente General", "Director General",
    "Compliance Officer", "Gerente Legal",
    "DPO", "Data Protection Officer",
    "CISO", "Director TI"
]

COMPANY_SIZE_FILTERS = {
    "small": {"min_employees": 10, "max_employees": 50},
    "medium": {"min_employees": 50, "max_employees": 200},
    "large": {"min_employees": 200, "max_employees": 500},
    "enterprise": {"min_employees": 500, "max_employees": None}
}


class ApolloLey21719Client:
    """Cliente Apollo.io especializado para prospeccion Ley 21.719"""

    def __init__(self, api_key: str, rate_limit: int = 200):
        self.api_key = api_key
        self.base_url = "https://api.apollo.io/v1"
        self.rate_limit = rate_limit
        self.requests_made = 0
        self.last_reset = time.time()

        if not api_key:
            raise ValueError("Apollo API key required")

        logger.info("Apollo Ley21719 client initialized", rate_limit=rate_limit)

    def _check_rate_limit(self):
        """Enforce rate limiting"""
        current_time = time.time()
        time_elapsed = current_time - self.last_reset

        if time_elapsed >= 3600:
            self.requests_made = 0
            self.last_reset = current_time

        if self.requests_made >= self.rate_limit:
            wait_time = 3600 - time_elapsed
            if wait_time > 0:
                logger.warning("Rate limit reached", wait_seconds=int(wait_time))
                time.sleep(wait_time)
                self.requests_made = 0
                self.last_reset = time.time()

    def search_sector(
        self,
        sector: str,
        country: str = "Chile",
        min_employees: int = 50,
        max_employees: int = 500,
        per_page: int = 25
    ) -> Optional[Dict]:
        """Busca contactos por sector"""
        if sector not in SECTOR_CONFIGS_LEY21719:
            logger.error(f"Sector invalido: {sector}")
            return None

        config = SECTOR_CONFIGS_LEY21719[sector]
        self._check_rate_limit()

        headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        payload = {
            'person_titles': config["target_titles"],
            'q_organization_keyword_tags': config["company_keywords"],
            'organization_locations': [country],
            'organization_num_employees_ranges': [f"{min_employees},{max_employees}"],
            'per_page': per_page
        }

        try:
            response = requests.post(
                f"{self.base_url}/mixed_people/search",
                json=payload,
                headers=headers,
                timeout=30
            )
            self.requests_made += 1

            if response.status_code == 200:
                data = response.json()
                data['sector_config'] = config
                logger.info(
                    "Search successful",
                    sector=sector,
                    contacts=len(data.get('people', []))
                )
                return data
            else:
                logger.warning("Search failed", status=response.status_code)
                return None

        except Exception as e:
            logger.error("API error", error=str(e))
            return None

    def search_all_sectors(
        self,
        country: str = "Chile",
        min_employees: int = 50,
        max_employees: int = 500,
        per_page_per_sector: int = 25
    ) -> Dict[str, Dict]:
        """Busca en todos los sectores"""
        results = {}

        sorted_sectors = sorted(
            SECTOR_CONFIGS_LEY21719.items(),
            key=lambda x: x[1]["priority"]
        )

        for sector, _ in sorted_sectors:
            sector_results = self.search_sector(
                sector=sector,
                country=country,
                min_employees=min_employees,
                max_employees=max_employees,
                per_page=per_page_per_sector
            )
            if sector_results:
                results[sector] = sector_results
            time.sleep(1)

        return results

    def export_csv(self, results: Dict[str, Dict], output_path: str) -> str:
        """Exporta contactos a CSV"""
        rows = []
        for sector, data in results.items():
            config = data.get('sector_config', {})
            for person in data.get('people', []):
                org = person.get('organization', {})
                rows.append({
                    'nombre': person.get('name', ''),
                    'cargo': person.get('title', ''),
                    'email': person.get('email', ''),
                    'linkedin_url': person.get('linkedin_url', ''),
                    'empresa': org.get('name', ''),
                    'sector': sector,
                    'prioridad': config.get('priority', 0),
                    'nivel_riesgo': config.get('risk_level', ''),
                    'fecha_extraccion': datetime.now().isoformat()
                })

        rows.sort(key=lambda x: x['prioridad'])

        if rows:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)

        return output_path

    @staticmethod
    def get_sector_info(sector: str) -> Optional[Dict]:
        return SECTOR_CONFIGS_LEY21719.get(sector)

    @staticmethod
    def list_sectors() -> List[str]:
        return sorted(
            SECTOR_CONFIGS_LEY21719.keys(),
            key=lambda x: SECTOR_CONFIGS_LEY21719[x]["priority"]
        )

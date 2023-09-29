AUTH_BASE_URL = "https://identity.vaillant-group.com/auth/realms"
LOGIN_URL = AUTH_BASE_URL + "/{realm}/login-actions/authenticate"
AUTHENTICATE_URL = AUTH_BASE_URL + "/{realm}/protocol/openid-connect/auth"
TOKEN_URL = AUTH_BASE_URL + "/{realm}/protocol/openid-connect/token"
API_URL_BASE = (
    "https://api.vaillant-group.com/service-connected-control/end-user-app-api/v1"
)
CLIENT_ID = "myvaillant"
BRANDS = {
    "vaillant": "Vaillant",
    "sdbg": "Saunier Duval",
    "bulex": "Bulex",
}
DEFAULT_BRAND = "vaillant"
COUNTRIES = {
    "vaillant": {
        "albania": "Albania",
        "austria": "Austria",
        "belgium": "Belgium",
        "bulgaria": "Bulgaria",
        "croatia": "Croatia",
        "czechrepublic": "Czechia",
        "denmark": "Denmark",
        "estonia": "Estonia",
        "finland": "Finland",
        "france": "France",
        "georgia": "Georgia",
        "germany": "Germany",
        "greece": "Greece",
        "hungary": "Hungary",
        "italy": "Italy",
        "latvia": "Latvia",
        "lithuania": "Lithuania",
        "luxembourg": "Luxembourg",
        "netherlands": "Netherlands",
        "norway": "Norway",
        "poland": "Poland",
        "portugal": "Portugal",
        "romania": "Romania",
        "serbia": "Serbia",
        "slovakia": "Slovakia",
        "slovenia": "Slovenia",
        "spain": "Spain",
        "sweden": "Sweden",
        "switzerland": "Switzerland",
        "ukraine": "Ukraine",
        "unitedkingdom": "United Kingdom",
        "uzbekistan": "Uzbekistan",
    },
    "sdbg": {
        "austria": "Austria",
        "czechrepublic": "Czechia",
        "finland": "Finland",
        "france": "France",
        "greece": "Greece",
        "hungary": "Hungary",
        "italy": "Italy",
        "lithuania": "Lithuania",
        "poland": "Poland",
        "portugal": "Portugal",
        "romania": "Romania",
        "slovakia": "Slovakia",
        "spain": "Spain",
    },
}
ALL_COUNTRIES = {c: n for d in COUNTRIES.values() for c, n in d.items()}
MANUAL_SETPOINT_TYPES = {
    "HEATING": "Heating",
    "COOLING": "Cooling",
}
DEFAULT_MANUAL_SETPOINT_TYPE = "HEATING"
DEFAULT_QUICK_VETO_DURATION = 3.0  # in hours
DEFAULT_CONTROL_IDENTIFIER = "tli"

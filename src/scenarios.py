"""Cenários prontos usados como pontos de partida na interface."""

CENARIOS = {
    "Personalizado": {
        "temperatura_inicial_c": 8.0,
        "temperatura_ambiente_c": 25.0,
        "volume_liquido_ml": 350.0,
        "volume_gas_ml": 150.0,
        "pressao_manometrica_inicial_kpa": 180.0,
        "altitude_m": 0.0,
        "tempo_simulacao_h": 3.0,
        "area_superficial_cm2": 500.0,
        "coeficiente_global_u": 8.0,
        "fluido_manometrico": "Água",
    },
    "Bebida gelada em ambiente quente": {
        "temperatura_inicial_c": 4.0,
        "temperatura_ambiente_c": 35.0,
        "volume_liquido_ml": 350.0,
        "volume_gas_ml": 150.0,
        "pressao_manometrica_inicial_kpa": 180.0,
        "altitude_m": 0.0,
        "tempo_simulacao_h": 4.0,
        "area_superficial_cm2": 500.0,
        "coeficiente_global_u": 10.0,
        "fluido_manometrico": "Água",
    },
    "Recipiente em altitude elevada": {
        "temperatura_inicial_c": 10.0,
        "temperatura_ambiente_c": 22.0,
        "volume_liquido_ml": 350.0,
        "volume_gas_ml": 150.0,
        "pressao_manometrica_inicial_kpa": 180.0,
        "altitude_m": 2500.0,
        "tempo_simulacao_h": 3.0,
        "area_superficial_cm2": 500.0,
        "coeficiente_global_u": 8.0,
        "fluido_manometrico": "Mercúrio",
    },
    "Volume de gás pequeno": {
        "temperatura_inicial_c": 8.0,
        "temperatura_ambiente_c": 30.0,
        "volume_liquido_ml": 450.0,
        "volume_gas_ml": 50.0,
        "pressao_manometrica_inicial_kpa": 200.0,
        "altitude_m": 0.0,
        "tempo_simulacao_h": 3.0,
        "area_superficial_cm2": 520.0,
        "coeficiente_global_u": 8.0,
        "fluido_manometrico": "Óleo",
    },
    "Pressão inicial alta": {
        "temperatura_inicial_c": 12.0,
        "temperatura_ambiente_c": 28.0,
        "volume_liquido_ml": 330.0,
        "volume_gas_ml": 170.0,
        "pressao_manometrica_inicial_kpa": 380.0,
        "altitude_m": 0.0,
        "tempo_simulacao_h": 2.0,
        "area_superficial_cm2": 500.0,
        "coeficiente_global_u": 7.0,
        "fluido_manometrico": "Mercúrio",
    },
    "Ambiente frio": {
        "temperatura_inicial_c": 25.0,
        "temperatura_ambiente_c": 2.0,
        "volume_liquido_ml": 350.0,
        "volume_gas_ml": 150.0,
        "pressao_manometrica_inicial_kpa": 180.0,
        "altitude_m": 800.0,
        "tempo_simulacao_h": 5.0,
        "area_superficial_cm2": 500.0,
        "coeficiente_global_u": 9.0,
        "fluido_manometrico": "Água",
    },
}


def obter_cenario(nome_cenario: str) -> dict[str, float | str]:
    """Retorna uma cópia dos parâmetros de um cenário pronto pelo nome."""
    if nome_cenario not in CENARIOS:
        raise ValueError(f"Cenário desconhecido: {nome_cenario}")
    return CENARIOS[nome_cenario].copy()


def listar_cenarios() -> list[str]:
    """Retorna os nomes dos cenários na ordem usada pela interface."""
    return list(CENARIOS.keys())


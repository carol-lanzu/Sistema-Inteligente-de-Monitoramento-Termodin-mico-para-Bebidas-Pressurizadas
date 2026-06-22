"""Modelo concentrado e simplificado de transferência de calor."""


def calcular_massa_liquido(volume_liquido_m3: float, densidade_kg_m3: float) -> float:
    """
    Calcula a massa aproximada do líquido pela relação m = rho V.

    Args:
        volume_liquido_m3: volume de líquido em m³.
        densidade_kg_m3: densidade aproximada em kg/m³.

    Returns:
        Massa de líquido em kg.
    """
    if volume_liquido_m3 <= 0 or densidade_kg_m3 <= 0:
        raise ValueError("Volume e densidade do líquido devem ser positivos.")
    return densidade_kg_m3 * volume_liquido_m3


def calcular_taxa_transferencia_calor(
    coeficiente_global_w_m2_k: float,
    area_superficial_m2: float,
    temperatura_ambiente_k: float,
    temperatura_bebida_k: float,
) -> float:
    """
    Calcula a taxa instantânea de calor entre ambiente e bebida.

    Fórmula: Q_dot = U A (T_amb - T_bebida).
    Um valor positivo aquece a bebida; um valor negativo indica resfriamento.
    Temperaturas podem ser dadas em K porque somente sua diferença é utilizada.
    """
    if coeficiente_global_w_m2_k <= 0 or area_superficial_m2 <= 0:
        raise ValueError("O coeficiente U e a área devem ser positivos.")

    # U reúne, de forma didática, resistências de convecção e condução.
    return (
        coeficiente_global_w_m2_k
        * area_superficial_m2
        * (temperatura_ambiente_k - temperatura_bebida_k)
    )


def calcular_variacao_temperatura_passo(
    taxa_calor_w: float,
    passo_tempo_s: float,
    massa_liquido_kg: float,
    calor_especifico_j_kg_k: float,
) -> float:
    """
    Calcula a variação de temperatura em um passo explícito da simulação.

    Fórmula: dT = Q_dot dt/(m c). O líquido é considerado uniforme e bem
    misturado, sem gradientes espaciais de temperatura.
    """
    if passo_tempo_s < 0 or massa_liquido_kg <= 0 or calor_especifico_j_kg_k <= 0:
        raise ValueError("Passo não pode ser negativo; massa e calor específico devem ser positivos.")
    return taxa_calor_w * passo_tempo_s / (massa_liquido_kg * calor_especifico_j_kg_k)


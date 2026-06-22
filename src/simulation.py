"""Integração temporal da temperatura e da pressão do recipiente fechado."""

import numpy as np
import pandas as pd

from src.conversions import converter_kelvin_para_celsius
from src.heat_transfer import (
    calcular_taxa_transferencia_calor,
    calcular_variacao_temperatura_passo,
)
from src.pressure import (
    calcular_pressao_absoluta_gas_ideal,
    calcular_pressao_manometrica,
)


def simular_evolucao_temperatura_pressao(
    temperatura_inicial_k: float,
    temperatura_ambiente_k: float,
    volume_gas_m3: float,
    quantidade_mols_gas: float,
    massa_liquido_kg: float,
    calor_especifico_j_kg_k: float,
    area_superficial_m2: float,
    coeficiente_global_u_w_m2_k: float,
    pressao_atmosferica_pa: float,
    tempo_total_s: float,
    numero_pontos: int,
) -> pd.DataFrame:
    """
    Simula a evolução térmica e a pressão de um recipiente fechado.

    O método de Euler explícito integra o balanço concentrado
    m c dT/dt = U A (T_amb - T). Em seguida, a pressão é recalculada por
    P = nRT/V, mantendo quantidade de gás e volume constantes.

    Args:
        temperatura_inicial_k: temperatura inicial da bebida e do gás em K.
        temperatura_ambiente_k: temperatura constante do ambiente em K.
        volume_gas_m3: volume constante do espaço gasoso em m³.
        quantidade_mols_gas: quantidade constante de gás em mol.
        massa_liquido_kg: massa térmica aproximada da bebida em kg.
        calor_especifico_j_kg_k: calor específico da bebida em J/(kg·K).
        area_superficial_m2: área efetiva de troca térmica em m².
        coeficiente_global_u_w_m2_k: coeficiente global U em W/(m²·K).
        pressao_atmosferica_pa: pressão atmosférica local em Pa.
        tempo_total_s: duração total da simulação em s.
        numero_pontos: número de estados, incluindo início e fim.

    Returns:
        DataFrame com tempo, temperatura, calor e pressões em unidades SI e
        unidades amigáveis para exibição.
    """
    if temperatura_inicial_k <= 0 or temperatura_ambiente_k <= 0:
        raise ValueError("As temperaturas absolutas devem ser positivas.")
    if volume_gas_m3 <= 0 or massa_liquido_kg <= 0:
        raise ValueError("Os volumes e massas do modelo devem ser positivos.")
    if calor_especifico_j_kg_k <= 0 or area_superficial_m2 <= 0:
        raise ValueError("Calor específico e área superficial devem ser positivos.")
    if coeficiente_global_u_w_m2_k <= 0 or tempo_total_s <= 0:
        raise ValueError("O coeficiente U e o tempo total devem ser positivos.")
    if numero_pontos <= 1:
        raise ValueError("O número de pontos deve ser maior que 1.")

    tempos_s = np.linspace(0.0, tempo_total_s, numero_pontos)
    passo_tempo_s = float(tempos_s[1] - tempos_s[0])

    temperaturas_k = np.empty(numero_pontos)
    taxas_calor_w = np.empty(numero_pontos)
    calores_acumulados_j = np.zeros(numero_pontos)
    pressoes_absolutas_pa = np.empty(numero_pontos)
    pressoes_manometricas_pa = np.empty(numero_pontos)

    temperaturas_k[0] = temperatura_inicial_k

    for indice in range(numero_pontos):
        # 1. A taxa de calor é avaliada com a temperatura atual da bebida.
        taxas_calor_w[indice] = calcular_taxa_transferencia_calor(
            coeficiente_global_u_w_m2_k,
            area_superficial_m2,
            temperatura_ambiente_k,
            temperaturas_k[indice],
        )

        # 2. A equação dos gases ideais fornece a pressão absoluta em cada estado.
        pressoes_absolutas_pa[indice] = calcular_pressao_absoluta_gas_ideal(
            quantidade_mols_gas,
            temperaturas_k[indice],
            volume_gas_m3,
        )

        # 3. A pressão manométrica compara o interior com a atmosfera local.
        pressoes_manometricas_pa[indice] = calcular_pressao_manometrica(
            pressoes_absolutas_pa[indice], pressao_atmosferica_pa
        )

        if indice == numero_pontos - 1:
            continue

        # 4. Euler explícito usa a taxa atual para avançar um passo no tempo.
        variacao_temperatura_k = calcular_variacao_temperatura_passo(
            taxas_calor_w[indice],
            passo_tempo_s,
            massa_liquido_kg,
            calor_especifico_j_kg_k,
        )
        temperaturas_k[indice + 1] = temperaturas_k[indice] + variacao_temperatura_k

        # 5. O calor acumulado é a soma algébrica de Q_dot vezes dt.
        calores_acumulados_j[indice + 1] = (
            calores_acumulados_j[indice] + taxas_calor_w[indice] * passo_tempo_s
        )

    return pd.DataFrame(
        {
            "tempo_s": tempos_s,
            "tempo_h": tempos_s / 3600.0,
            "temperatura_k": temperaturas_k,
            "temperatura_c": converter_kelvin_para_celsius(temperaturas_k),
            "taxa_calor_w": taxas_calor_w,
            "calor_acumulado_j": calores_acumulados_j,
            "calor_acumulado_kj": calores_acumulados_j / 1000.0,
            "pressao_absoluta_pa": pressoes_absolutas_pa,
            "pressao_absoluta_kpa": pressoes_absolutas_pa / 1000.0,
            "pressao_manometrica_pa": pressoes_manometricas_pa,
            "pressao_manometrica_kpa": pressoes_manometricas_pa / 1000.0,
        }
    )


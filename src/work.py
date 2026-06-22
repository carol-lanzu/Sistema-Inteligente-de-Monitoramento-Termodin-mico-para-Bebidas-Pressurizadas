"""Estimativa didática do trabalho de expansão na abertura do recipiente."""

import math

from src.constants import CONSTANTE_GASES_J_MOL_K
from src.conversions import converter_joules_para_quilojoules


def calcular_trabalho_expansao_isotermica(
    quantidade_mols: float,
    temperatura_kelvin: float,
    pressao_inicial_pa: float,
    pressao_final_pa: float,
) -> tuple[float, float, str]:
    """
    Estima o trabalho de uma expansão isotérmica idealizada de gás ideal.

    Fórmula: W ≈ nRT ln(P_i/P_f).

    Returns:
        Trabalho em J, trabalho em kJ e mensagem interpretativa.

    Hipóteses:
        A temperatura é constante durante a expansão e a pressão final é a
        atmosférica. Não representa a dinâmica real e rápida de uma abertura.
    """
    if quantidade_mols < 0 or temperatura_kelvin <= 0 or pressao_final_pa <= 0:
        raise ValueError("Mols não podem ser negativos; temperatura e pressão final devem ser positivas.")

    if pressao_inicial_pa <= pressao_final_pa:
        return (
            0.0,
            0.0,
            "Não há expansão positiva estimada, pois a pressão interna não supera a externa.",
        )

    # A integral isotérmica do trabalho de gás ideal resulta no logaritmo da razão de pressões.
    trabalho_j = (
        quantidade_mols
        * CONSTANTE_GASES_J_MOL_K
        * temperatura_kelvin
        * math.log(pressao_inicial_pa / pressao_final_pa)
    )
    return (
        trabalho_j,
        converter_joules_para_quilojoules(trabalho_j),
        "Trabalho positivo estimado para a expansão idealizada até a pressão atmosférica.",
    )


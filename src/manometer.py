"""Cálculos e interpretação de um manômetro de coluna em U."""

from src.constants import GRAVIDADE_M_S2


def calcular_altura_coluna_manometro(
    pressao_manometrica_pa: float, densidade_fluido_kg_m3: float
) -> tuple[float, float]:
    """
    Calcula a diferença de altura produzida pela pressão manométrica.

    Fórmula: Delta h = Delta P/(rho g).

    Returns:
        Tupla com altura em metros e em centímetros.

    Hipóteses:
        O fluido está em repouso e sua densidade é constante. Uma altura
        negativa indica inversão do sentido da coluna, pois a pressão interna
        ficou abaixo da pressão atmosférica.
    """
    if densidade_fluido_kg_m3 <= 0:
        raise ValueError("A densidade do fluido manométrico deve ser positiva.")

    # O sinal é preservado para comunicar qual lado do manômetro fica mais alto.
    altura_m = pressao_manometrica_pa / (densidade_fluido_kg_m3 * GRAVIDADE_M_S2)
    return altura_m, altura_m * 100.0


def gerar_interpretacao_manometro(altura_coluna_cm: float) -> str:
    """Gera uma interpretação textual do sinal da coluna manométrica."""
    if altura_coluna_cm > 0:
        return (
            "A pressão interna supera a atmosférica; a coluna é deslocada no "
            "sentido correspondente a uma sobrepressão no recipiente."
        )
    if altura_coluna_cm < 0:
        return (
            "A pressão interna é inferior à atmosférica; o sentido da coluna "
            "se inverte em relação ao caso de sobrepressão."
        )
    return "As pressões estão equilibradas e não há diferença de altura entre as colunas."


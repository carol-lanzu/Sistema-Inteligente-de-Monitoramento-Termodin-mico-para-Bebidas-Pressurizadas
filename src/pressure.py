"""Cálculos de pressão atmosférica, manométrica e de gás ideal."""

from src.constants import (
    CONSTANTE_GASES_J_MOL_K,
    DENSIDADE_AR_KG_M3,
    GRAVIDADE_M_S2,
    PRESSAO_ATMOSFERICA_NIVEL_MAR_PA,
)


def calcular_pressao_atmosferica_por_altitude(altitude_m: float) -> float:
    """
    Estima a pressão atmosférica local por uma aproximação hidrostática linear.

    Fórmula: P_atm ≈ P0 - rho_ar g h.

    Args:
        altitude_m: altitude em relação ao nível do mar, em metros (m).

    Returns:
        Pressão atmosférica aproximada em pascal (Pa), nunca negativa.

    Hipóteses:
        A densidade do ar é constante. A aproximação é didática e adequada
        apenas para discutir altitudes moderadas, não para previsão meteorológica.
    """
    # A coluna de ar acima do ponto diminui conforme a altitude aumenta.
    pressao_atmosferica_pa = (
        PRESSAO_ATMOSFERICA_NIVEL_MAR_PA
        - DENSIDADE_AR_KG_M3 * GRAVIDADE_M_S2 * altitude_m
    )
    return max(0.0, pressao_atmosferica_pa)


def calcular_pressao_absoluta_inicial(
    pressao_atmosferica_pa: float, pressao_manometrica_pa: float
) -> float:
    """
    Calcula a pressão absoluta inicial a partir da atmosfera e do manômetro.

    Fórmula: P_abs = P_atm + P_man. Todas as entradas e a saída estão em Pa.
    """
    return pressao_atmosferica_pa + pressao_manometrica_pa


def calcular_pressao_manometrica(
    pressao_absoluta_pa: float, pressao_atmosferica_pa: float
) -> float:
    """
    Calcula quanto a pressão interna está acima ou abaixo da atmosfera local.

    Fórmula: P_man = P_abs - P_atm. Todas as pressões usam pascal (Pa).
    Um resultado negativo representa pressão interna inferior à atmosférica.
    """
    # A leitura manométrica usa a atmosfera local como referência de zero.
    return pressao_absoluta_pa - pressao_atmosferica_pa


def calcular_quantidade_mols_gas_ideal(
    pressao_absoluta_pa: float, volume_gas_m3: float, temperatura_kelvin: float
) -> float:
    """
    Estima a quantidade de matéria do gás pela equação dos gases ideais.

    Fórmula: n = PV/(RT).

    Args:
        pressao_absoluta_pa: pressão absoluta do gás em Pa.
        volume_gas_m3: volume ocupado pelo gás em m³.
        temperatura_kelvin: temperatura absoluta do gás em K.

    Returns:
        Quantidade de matéria em mol.

    Raises:
        ValueError: se volume, pressão absoluta ou temperatura não forem positivos.
    """
    if pressao_absoluta_pa <= 0 or volume_gas_m3 <= 0 or temperatura_kelvin <= 0:
        raise ValueError("Pressão absoluta, volume e temperatura devem ser positivos.")

    # PV = nRT é usado apenas para o gás no espaço superior do recipiente.
    return (
        pressao_absoluta_pa
        * volume_gas_m3
        / (CONSTANTE_GASES_J_MOL_K * temperatura_kelvin)
    )


def calcular_pressao_absoluta_gas_ideal(
    quantidade_mols: float, temperatura_kelvin: float, volume_gas_m3: float
) -> float:
    """
    Calcula a pressão absoluta de um gás ideal em volume constante.

    Fórmula: P = nRT/V. A saída é fornecida em pascal (Pa).

    Raises:
        ValueError: se volume ou temperatura não forem positivos, ou se n for negativo.
    """
    if volume_gas_m3 <= 0 or temperatura_kelvin <= 0 or quantidade_mols < 0:
        raise ValueError("Volume e temperatura devem ser positivos; mols não podem ser negativos.")

    # Antes da abertura, n e V são constantes; assim, P varia proporcionalmente a T.
    return (
        quantidade_mols
        * CONSTANTE_GASES_J_MOL_K
        * temperatura_kelvin
        / volume_gas_m3
    )


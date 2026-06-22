"""Conversões entre unidades amigáveis da interface e unidades do SI."""


def converter_celsius_para_kelvin(temperatura_celsius: float) -> float:
    """Converte uma temperatura de graus Celsius (°C) para kelvin (K)."""
    return temperatura_celsius + 273.15


def converter_kelvin_para_celsius(temperatura_kelvin: float) -> float:
    """Converte uma temperatura de kelvin (K) para graus Celsius (°C)."""
    return temperatura_kelvin - 273.15


def converter_mililitros_para_metros_cubicos(volume_mililitros: float) -> float:
    """Converte volume de mililitros (mL) para metros cúbicos (m³)."""
    return volume_mililitros * 1e-6


def converter_centimetros_quadrados_para_metros_quadrados(area_cm2: float) -> float:
    """Converte área de centímetros quadrados (cm²) para metros quadrados (m²)."""
    return area_cm2 * 1e-4


def converter_kpa_para_pa(pressao_kpa: float) -> float:
    """Converte pressão de quilopascal (kPa) para pascal (Pa)."""
    return pressao_kpa * 1000.0


def converter_pa_para_kpa(pressao_pa: float) -> float:
    """Converte pressão de pascal (Pa) para quilopascal (kPa)."""
    return pressao_pa / 1000.0


def converter_joules_para_quilojoules(energia_j: float) -> float:
    """Converte energia de joules (J) para quilojoules (kJ)."""
    return energia_j / 1000.0


def converter_segundos_para_horas(tempo_segundos: float) -> float:
    """Converte intervalo de tempo de segundos (s) para horas (h)."""
    return tempo_segundos / 3600.0


def converter_horas_para_segundos(tempo_horas: float) -> float:
    """Converte intervalo de tempo de horas (h) para segundos (s)."""
    return tempo_horas * 3600.0


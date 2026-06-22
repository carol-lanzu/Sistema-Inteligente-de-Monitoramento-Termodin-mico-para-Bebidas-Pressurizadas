"""Testes unitários dos principais cálculos físicos do PressurizaLab."""

import math

import pytest

from src.constants import CONSTANTE_GASES_J_MOL_K
from src.conversions import (
    converter_celsius_para_kelvin,
    converter_kelvin_para_celsius,
)
from src.manometer import calcular_altura_coluna_manometro
from src.pressure import (
    calcular_pressao_absoluta_gas_ideal,
    calcular_pressao_atmosferica_por_altitude,
    calcular_pressao_manometrica,
    calcular_quantidade_mols_gas_ideal,
)
from src.work import calcular_trabalho_expansao_isotermica


def test_conversao_celsius_kelvin() -> None:
    """Verifica pontos conhecidos e a reversibilidade da conversão térmica."""
    assert converter_celsius_para_kelvin(0.0) == pytest.approx(273.15)
    assert converter_kelvin_para_celsius(373.15) == pytest.approx(100.0)


def test_pressao_atmosferica_ao_nivel_mar() -> None:
    """Ao nível do mar, a aproximação deve recuperar a atmosfera padrão."""
    assert calcular_pressao_atmosferica_por_altitude(0.0) == pytest.approx(101325.0)


def test_pressao_manometrica_e_diferenca_de_referencia() -> None:
    """A pressão manométrica deve ser a diferença entre absoluta e atmosférica."""
    assert calcular_pressao_manometrica(250000.0, 100000.0) == pytest.approx(150000.0)


def test_equacao_gas_ideal_nos_dois_sentidos() -> None:
    """O cálculo de n seguido do cálculo de P deve recuperar a pressão inicial."""
    pressao_pa = 200000.0
    volume_m3 = 0.001
    temperatura_k = 300.0
    quantidade_mols = calcular_quantidade_mols_gas_ideal(
        pressao_pa, volume_m3, temperatura_k
    )
    assert quantidade_mols == pytest.approx(
        pressao_pa * volume_m3 / (CONSTANTE_GASES_J_MOL_K * temperatura_k)
    )
    assert calcular_pressao_absoluta_gas_ideal(
        quantidade_mols, temperatura_k, volume_m3
    ) == pytest.approx(pressao_pa)


def test_altura_manometro_segue_relacao_hidrostatica() -> None:
    """Uma diferença de rho*g Pa em água deve produzir um metro de coluna."""
    altura_m, altura_cm = calcular_altura_coluna_manometro(1000.0 * 9.81, 1000.0)
    assert altura_m == pytest.approx(1.0)
    assert altura_cm == pytest.approx(100.0)


def test_trabalho_expansao_positivo_apenas_com_sobrepressao() -> None:
    """A estimativa deve ser positiva somente quando a pressão interna é maior."""
    trabalho_j, trabalho_kj, _ = calcular_trabalho_expansao_isotermica(
        1.0, 300.0, 200000.0, 100000.0
    )
    esperado_j = CONSTANTE_GASES_J_MOL_K * 300.0 * math.log(2.0)
    assert trabalho_j == pytest.approx(esperado_j)
    assert trabalho_kj == pytest.approx(esperado_j / 1000.0)

    trabalho_sem_expansao_j, trabalho_sem_expansao_kj, _ = (
        calcular_trabalho_expansao_isotermica(1.0, 300.0, 100000.0, 100000.0)
    )
    assert trabalho_sem_expansao_j == 0.0
    assert trabalho_sem_expansao_kj == 0.0


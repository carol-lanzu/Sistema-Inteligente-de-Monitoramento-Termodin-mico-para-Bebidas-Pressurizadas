"""Classificação didática da pressão, sem finalidade de segurança real."""


def classificar_nivel_pressao(pressao_manometrica_kpa: float) -> tuple[str, str, str, str]:
    """
    Classifica uma pressão manométrica em faixas didáticas de interpretação.

    Returns:
        Nível, mensagem, recomendação e categoria de cor para a interface.

    Observação:
        Os limites não são critérios de projeto, certificação ou segurança de
        recipientes reais. Servem somente para comparar cenários simulados.
    """
    # As faixas abaixo são escolhas pedagógicas, não limites estruturais reais.
    if pressao_manometrica_kpa < 100.0:
        return (
            "Baixa",
            "A sobrepressão simulada está na menor faixa didática.",
            "Compare este cenário com outro mais aquecido ou com menor volume de gás.",
            "verde",
        )
    if pressao_manometrica_kpa <= 300.0:
        return (
            "Moderada",
            "A sobrepressão simulada está na faixa intermediária didática.",
            "Observe como temperatura e altitude alteram a pressão manométrica.",
            "amarelo",
        )
    return (
        "Elevada",
        "A sobrepressão simulada está na maior faixa didática.",
        "Interprete com cautela: isto não avalia resistência nem segurança do recipiente.",
        "vermelho",
    )


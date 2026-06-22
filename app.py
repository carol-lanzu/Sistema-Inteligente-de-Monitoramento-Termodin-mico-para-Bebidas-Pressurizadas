"""Interface principal do PressurizaLab, desenvolvida com Streamlit."""

import streamlit as st

from src.charts import (
    criar_figura_manometro_virtual,
    criar_grafico_calor_tempo,
    criar_grafico_pressao_tempo,
    criar_grafico_temperatura_tempo,
)
from src.constants import (
    CALOR_ESPECIFICO_AGUA_J_KG_K,
    DENSIDADE_AGUA_KG_M3,
    DENSIDADES_FLUIDOS_MANOMETRICOS,
)
from src.conversions import (
    converter_celsius_para_kelvin,
    converter_centimetros_quadrados_para_metros_quadrados,
    converter_horas_para_segundos,
    converter_kpa_para_pa,
    converter_mililitros_para_metros_cubicos,
    converter_pa_para_kpa,
)
from src.heat_transfer import calcular_massa_liquido
from src.manometer import calcular_altura_coluna_manometro, gerar_interpretacao_manometro
from src.pressure import (
    calcular_pressao_absoluta_inicial,
    calcular_pressao_atmosferica_por_altitude,
    calcular_quantidade_mols_gas_ideal,
)
from src.safety import classificar_nivel_pressao
from src.scenarios import listar_cenarios, obter_cenario
from src.simulation import simular_evolucao_temperatura_pressao
from src.work import calcular_trabalho_expansao_isotermica


st.set_page_config(
    page_title="PressurizaLab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


def aplicar_estilo_visual() -> None:
    """Aplica pequenos ajustes visuais sem substituir os componentes nativos."""
    st.markdown(
        """
        <style>
        .block-container {padding-top: 2rem; padding-bottom: 3rem;}
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, #f8fafc, #eef2ff);
            border: 1px solid #dbeafe;
            border-radius: 0.8rem;
            padding: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def exibir_cabecalho() -> None:
    """Exibe o título, a proposta e o aviso principal do simulador."""
    st.title("🧪 PressurizaLab")
    st.subheader("Simulador Computacional de Pressão, Calor e Trabalho")
    st.write(
        "Explore como um recipiente fechado com líquido e uma região gasosa "
        "responde a mudanças de temperatura, altitude e configuração."
    )
    st.warning(
        "Modelo didático simplificado: não representa carbonatação, espuma, "
        "ruptura estrutural ou a segurança real de uma bebida pressurizada."
    )


def exibir_guia_didatico_aba(
    objetivo: str,
    conceito: str,
    formula_principal: str,
    interpretacao: str,
    fala_apresentacao: str,
) -> None:
    """Exibe um guia de leitura e uma sugestão curta para a apresentação oral."""
    st.info(
        f"""
        **O que esta aba faz:** {objetivo}

        **Conceito físico:** {conceito}

        **Fórmula principal:** `{formula_principal}`

        **Como interpretar:** {interpretacao}
        """
    )
    with st.expander("Como explicar esta aba na apresentação"):
        st.write(fala_apresentacao)


def coletar_parametros_interface() -> dict[str, float | int | str]:
    """
    Cria os controles de configuração e retorna os valores escolhidos.

    As entradas aparecem em unidades familiares. A conversão para o Sistema
    Internacional ocorre somente antes dos cálculos físicos.
    """
    st.sidebar.header("Cenário de partida")
    cenarios_disponiveis = listar_cenarios()
    nome_cenario = st.sidebar.selectbox(
        "Cenário exemplo",
        cenarios_disponiveis,
        index=cenarios_disponiveis.index("Bebida gelada em ambiente quente"),
        help="Trocar o cenário carrega um novo conjunto de valores iniciais.",
    )
    cenario = obter_cenario(nome_cenario)
    chave = nome_cenario.replace(" ", "_")

    st.sidebar.caption(
        "Os cenários são exemplos didáticos. Todos os campos podem ser ajustados manualmente."
    )

    temperatura_inicial_c = st.sidebar.number_input(
        "Temperatura inicial da bebida (°C)",
        min_value=-50.0,
        max_value=100.0,
        value=float(cenario["temperatura_inicial_c"]),
        step=1.0,
        key=f"temp_inicial_{chave}",
    )
    temperatura_ambiente_c = st.sidebar.number_input(
        "Temperatura ambiente (°C)",
        min_value=-50.0,
        max_value=100.0,
        value=float(cenario["temperatura_ambiente_c"]),
        step=1.0,
        key=f"temp_ambiente_{chave}",
    )
    volume_liquido_ml = st.sidebar.number_input(
        "Volume de líquido (mL)",
        min_value=1.0,
        max_value=5000.0,
        value=float(cenario["volume_liquido_ml"]),
        step=10.0,
        key=f"vol_liquido_{chave}",
    )
    volume_gas_ml = st.sidebar.number_input(
        "Volume de gás (mL)",
        min_value=1.0,
        max_value=5000.0,
        value=float(cenario["volume_gas_ml"]),
        step=10.0,
        key=f"vol_gas_{chave}",
        help=(
            "Volume ocupado pelo gás no espaço superior. Ele não pode ser zero e "
            "permanece constante enquanto o recipiente está fechado."
        ),
    )
    pressao_manometrica_inicial_kpa = st.sidebar.number_input(
        "Pressão manométrica inicial (kPa)",
        min_value=-90.0,
        max_value=1000.0,
        value=float(cenario["pressao_manometrica_inicial_kpa"]),
        step=10.0,
        key=f"pressao_{chave}",
        help=(
            "Diferença entre a pressão absoluta interna e a pressão atmosférica "
            "local: P_man = P_abs - P_atm."
        ),
    )
    altitude_m = st.sidebar.number_input(
        "Altitude (m)",
        min_value=-500.0,
        max_value=5000.0,
        value=float(cenario["altitude_m"]),
        step=100.0,
        key=f"altitude_{chave}",
    )
    tempo_simulacao_h = st.sidebar.number_input(
        "Tempo de simulação (h)",
        min_value=0.1,
        max_value=48.0,
        value=float(cenario["tempo_simulacao_h"]),
        step=0.5,
        key=f"tempo_{chave}",
    )
    with st.sidebar.expander("Parâmetros avançados"):
        area_superficial_cm2 = st.number_input(
            "Área superficial aproximada (cm²)",
            min_value=1.0,
            max_value=5000.0,
            value=float(cenario["area_superficial_cm2"]),
            step=10.0,
            key=f"area_{chave}",
            help=(
                "Área efetiva usada na troca de calor. Uma área maior aumenta a "
                "taxa de aquecimento ou resfriamento no modelo."
            ),
        )
        coeficiente_global_u = st.number_input(
            "Coeficiente global U (W/(m²·K))",
            min_value=0.1,
            max_value=100.0,
            value=float(cenario["coeficiente_global_u"]),
            step=0.5,
            key=f"u_{chave}",
            help=(
                "Parâmetro simplificado que reúne os efeitos de condução e convecção. "
                "Quanto maior U, mais rápida é a troca de calor."
            ),
        )
        fluidos = list(DENSIDADES_FLUIDOS_MANOMETRICOS.keys())
        fluido_padrao = str(cenario["fluido_manometrico"])
        fluido_manometrico = st.selectbox(
            "Fluido do manômetro",
            fluidos,
            index=fluidos.index(fluido_padrao),
            key=f"fluido_{chave}",
            help="A densidade do fluido determina a altura necessária para indicar a pressão.",
        )
        numero_pontos = st.slider(
            "Número de pontos da simulação",
            min_value=20,
            max_value=1000,
            value=200,
            step=10,
            key=f"pontos_{chave}",
            help=(
                "Quantidade de instantes calculados entre o início e o fim. Mais "
                "pontos deixam as curvas mais detalhadas e reduzem o passo de integração."
            ),
        )

    return {
        "nome_cenario": nome_cenario,
        "temperatura_inicial_c": temperatura_inicial_c,
        "temperatura_ambiente_c": temperatura_ambiente_c,
        "volume_liquido_ml": volume_liquido_ml,
        "volume_gas_ml": volume_gas_ml,
        "pressao_manometrica_inicial_kpa": pressao_manometrica_inicial_kpa,
        "altitude_m": altitude_m,
        "tempo_simulacao_h": tempo_simulacao_h,
        "area_superficial_cm2": area_superficial_cm2,
        "coeficiente_global_u": coeficiente_global_u,
        "fluido_manometrico": fluido_manometrico,
        "numero_pontos": numero_pontos,
    }


def converter_e_calcular_estado(parametros: dict[str, float | int | str]) -> dict:
    """Converte entradas para SI, calcula o estado inicial e executa a simulação."""
    temperatura_inicial_k = converter_celsius_para_kelvin(
        float(parametros["temperatura_inicial_c"])
    )
    temperatura_ambiente_k = converter_celsius_para_kelvin(
        float(parametros["temperatura_ambiente_c"])
    )
    volume_liquido_m3 = converter_mililitros_para_metros_cubicos(
        float(parametros["volume_liquido_ml"])
    )
    volume_gas_m3 = converter_mililitros_para_metros_cubicos(
        float(parametros["volume_gas_ml"])
    )
    pressao_manometrica_inicial_pa = converter_kpa_para_pa(
        float(parametros["pressao_manometrica_inicial_kpa"])
    )
    area_superficial_m2 = converter_centimetros_quadrados_para_metros_quadrados(
        float(parametros["area_superficial_cm2"])
    )
    tempo_total_s = converter_horas_para_segundos(float(parametros["tempo_simulacao_h"]))

    if temperatura_inicial_k <= 0 or temperatura_ambiente_k <= 0:
        raise ValueError("As temperaturas informadas devem ser superiores ao zero absoluto.")

    pressao_atmosferica_pa = calcular_pressao_atmosferica_por_altitude(
        float(parametros["altitude_m"])
    )
    pressao_absoluta_inicial_pa = calcular_pressao_absoluta_inicial(
        pressao_atmosferica_pa, pressao_manometrica_inicial_pa
    )
    if pressao_absoluta_inicial_pa <= 0:
        raise ValueError("A combinação escolhida resulta em pressão absoluta não positiva.")

    quantidade_mols = calcular_quantidade_mols_gas_ideal(
        pressao_absoluta_inicial_pa, volume_gas_m3, temperatura_inicial_k
    )
    massa_liquido_kg = calcular_massa_liquido(volume_liquido_m3, DENSIDADE_AGUA_KG_M3)

    resultados = simular_evolucao_temperatura_pressao(
        temperatura_inicial_k=temperatura_inicial_k,
        temperatura_ambiente_k=temperatura_ambiente_k,
        volume_gas_m3=volume_gas_m3,
        quantidade_mols_gas=quantidade_mols,
        massa_liquido_kg=massa_liquido_kg,
        calor_especifico_j_kg_k=CALOR_ESPECIFICO_AGUA_J_KG_K,
        area_superficial_m2=area_superficial_m2,
        coeficiente_global_u_w_m2_k=float(parametros["coeficiente_global_u"]),
        pressao_atmosferica_pa=pressao_atmosferica_pa,
        tempo_total_s=tempo_total_s,
        numero_pontos=int(parametros["numero_pontos"]),
    )

    return {
        "temperatura_inicial_k": temperatura_inicial_k,
        "temperatura_ambiente_k": temperatura_ambiente_k,
        "volume_liquido_m3": volume_liquido_m3,
        "volume_gas_m3": volume_gas_m3,
        "area_superficial_m2": area_superficial_m2,
        "pressao_atmosferica_pa": pressao_atmosferica_pa,
        "pressao_absoluta_inicial_pa": pressao_absoluta_inicial_pa,
        "pressao_manometrica_inicial_pa": pressao_manometrica_inicial_pa,
        "quantidade_mols": quantidade_mols,
        "massa_liquido_kg": massa_liquido_kg,
        "resultados": resultados,
    }


aplicar_estilo_visual()
exibir_cabecalho()
parametros = coletar_parametros_interface()

try:
    estado = converter_e_calcular_estado(parametros)
except ValueError as erro:
    st.error(f"Não foi possível executar a simulação: {erro}")
    st.stop()

resultados = estado["resultados"]
estado_final = resultados.iloc[-1]

abas = st.tabs(
    [
        "1. Configurar Cenário",
        "2. Pressão Inicial",
        "3. Aquecimento/Resfriamento",
        "4. Manômetro",
        "5. Abrir Recipiente",
        "6. Resumo e Alertas",
    ]
)

with abas[0]:
    st.header("1. Configurar cenário")
    exibir_guia_didatico_aba(
        objetivo="Define as condições iniciais do recipiente e o tempo observado.",
        conceito="Definição do sistema, das propriedades e das unidades de entrada.",
        formula_principal="V_total = V_líquido + V_gás",
        interpretacao=(
            "Os valores desta etapa alimentam todas as outras abas. Compare principalmente "
            "as temperaturas, o volume gasoso e a pressão inicial."
        ),
        fala_apresentacao=(
            "Primeiro definimos o sistema físico: quanto líquido e gás existem, as "
            "temperaturas, a pressão inicial e a altitude. A interface recebe unidades "
            "familiares e o programa converte tudo para o SI antes dos cálculos."
        ),
    )
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)
    coluna_1.metric("Cenário", str(parametros["nome_cenario"]))
    coluna_2.metric("Volume total", f"{float(parametros['volume_liquido_ml']) + float(parametros['volume_gas_ml']):.0f} mL")
    coluna_3.metric("Tempo", f"{float(parametros['tempo_simulacao_h']):.1f} h")
    coluna_4.metric("Resolução", f"{int(parametros['numero_pontos'])} pontos")

    st.subheader("Resumo das entradas")
    resumo_1, resumo_2 = st.columns(2)
    with resumo_1:
        st.markdown(
            f"""
            - Temperatura inicial: **{float(parametros['temperatura_inicial_c']):.1f} °C**
            - Temperatura ambiente: **{float(parametros['temperatura_ambiente_c']):.1f} °C**
            - Volume de líquido: **{float(parametros['volume_liquido_ml']):.0f} mL**
            - Volume de gás: **{float(parametros['volume_gas_ml']):.0f} mL**
            - Pressão manométrica inicial: **{float(parametros['pressao_manometrica_inicial_kpa']):.1f} kPa**
            """
        )
    with resumo_2:
        st.markdown(
            f"""
            - Altitude: **{float(parametros['altitude_m']):.0f} m**
            - Área de troca: **{float(parametros['area_superficial_cm2']):.0f} cm²**
            - Coeficiente global U: **{float(parametros['coeficiente_global_u']):.1f} W/(m²·K)**
            - Fluido manométrico: **{parametros['fluido_manometrico']}**
            """
        )
    st.info(
        "Hipóteses: líquido aproximado como água e bem misturado; gás ideal; "
        "volume gasoso constante antes da abertura; ambiente com temperatura constante."
    )

with abas[1]:
    st.header("2. Pressão inicial")
    exibir_guia_didatico_aba(
        objetivo="Calcula as pressões e estima a quantidade de gás no estado inicial.",
        conceito="Pressão absoluta, atmosférica, manométrica e equação dos gases ideais.",
        formula_principal="P_abs = P_atm + P_man; PV = nRT",
        interpretacao=(
            "A pressão absoluta é usada no gás ideal; a manométrica mostra quanto o "
            "interior está acima ou abaixo da atmosfera local."
        ),
        fala_apresentacao=(
            "Aqui distinguimos as três pressões. A absoluta parte do vácuo, a atmosférica "
            "vem do ar externo e a manométrica é a diferença entre elas. Depois usamos "
            "a pressão absoluta em PV igual a nRT para estimar os mols de gás."
        ),
    )
    metrica_1, metrica_2, metrica_3 = st.columns(3)
    metrica_1.metric(
        "Pressão atmosférica local",
        f"{converter_pa_para_kpa(estado['pressao_atmosferica_pa']):.2f} kPa",
    )
    metrica_2.metric(
        "Pressão absoluta inicial",
        f"{converter_pa_para_kpa(estado['pressao_absoluta_inicial_pa']):.2f} kPa",
    )
    metrica_3.metric(
        "Pressão manométrica inicial",
        f"{converter_pa_para_kpa(estado['pressao_manometrica_inicial_pa']):.2f} kPa",
    )
    metrica_4, metrica_5, metrica_6 = st.columns(3)
    metrica_4.metric("Volume gasoso", f"{float(parametros['volume_gas_ml']):.0f} mL")
    metrica_5.metric("Quantidade de gás", f"{estado['quantidade_mols']:.5f} mol")
    metrica_6.metric("Massa aproximada do líquido", f"{estado['massa_liquido_kg']:.3f} kg")

    formula_1, formula_2 = st.columns(2)
    with formula_1:
        st.latex(r"P_{abs}=P_{atm}+P_{man}")
        st.caption("A referência zero da pressão absoluta é o vácuo.")
    with formula_2:
        st.latex(r"PV=nRT")
        st.caption("O gás do espaço superior é considerado ideal.")
    st.info(
        "A pressão atmosférica usa P_atm ≈ P₀ − ρ_ar g h, uma aproximação linear "
        "adequada somente à discussão didática de altitudes moderadas."
    )

with abas[2]:
    st.header("3. Aquecimento ou resfriamento")
    exibir_guia_didatico_aba(
        objetivo="Simula a temperatura, a taxa de calor e a pressão ao longo do tempo.",
        conceito="Balanço de energia em um sistema concentrado e transferência de calor.",
        formula_principal="Q_dot = UA(T_amb - T); mc(dT/dt) = Q_dot",
        interpretacao=(
            "Taxa positiva aquece a bebida e taxa negativa a resfria. A curva tende à "
            "temperatura ambiente e fica menos inclinada perto do equilíbrio térmico."
        ),
        fala_apresentacao=(
            "Tratamos a bebida como uma massa uniforme e bem misturada. A diferença de "
            "temperatura produz uma taxa de calor, que muda a temperatura passo a passo. "
            "Quando a bebida se aproxima do ambiente, a taxa diminui."
        ),
    )
    termica_1, termica_2, termica_3 = st.columns(3)
    termica_1.metric("Taxa inicial", f"{resultados.iloc[0]['taxa_calor_w']:.3f} W")
    termica_2.metric("Taxa final", f"{estado_final['taxa_calor_w']:.3f} W")
    termica_3.metric(
        "Temperatura final",
        f"{estado_final['temperatura_c']:.2f} °C",
        delta=f"{estado_final['temperatura_c'] - float(parametros['temperatura_inicial_c']):.2f} °C",
    )
    grafico_1, grafico_2 = st.columns(2)
    with grafico_1:
        st.plotly_chart(criar_grafico_temperatura_tempo(resultados), width="stretch")
    with grafico_2:
        st.plotly_chart(criar_grafico_calor_tempo(resultados), width="stretch")
    st.latex(r"\dot{Q}=UA(T_{amb}-T) \qquad mc\frac{dT}{dt}=\dot{Q}")
    st.caption(
        "U concentra efeitos térmicos que seriam separados em um modelo detalhado. "
        "A integração usa Euler explícito e temperatura uniforme no líquido."
    )

with abas[3]:
    st.header("4. Manômetro")
    exibir_guia_didatico_aba(
        objetivo="Converte a pressão manométrica final em uma diferença de altura.",
        conceito="Equilíbrio hidrostático em um manômetro de coluna em U.",
        formula_principal="ΔP = ρgΔh",
        interpretacao=(
            "Para a mesma pressão, fluidos mais densos exigem colunas menores. O sinal "
            "da altura informa o sentido do desequilíbrio entre interior e atmosfera."
        ),
        fala_apresentacao=(
            "O manômetro transforma diferença de pressão em uma grandeza visível: altura. "
            "A pressão equilibra o peso da coluna; por isso o mercúrio, sendo mais denso, "
            "precisa de uma coluna menor que a água."
        ),
    )
    densidade_fluido = DENSIDADES_FLUIDOS_MANOMETRICOS[str(parametros["fluido_manometrico"])]
    altura_m, altura_cm = calcular_altura_coluna_manometro(
        float(estado_final["pressao_manometrica_pa"]), densidade_fluido
    )
    mano_1, mano_2, mano_3 = st.columns(3)
    mano_1.metric("Pressão manométrica final", f"{estado_final['pressao_manometrica_kpa']:.2f} kPa")
    mano_2.metric("Densidade do fluido", f"{densidade_fluido:.0f} kg/m³")
    mano_3.metric("Diferença de altura", f"{altura_cm:.2f} cm")
    st.plotly_chart(
        criar_figura_manometro_virtual(altura_cm, str(parametros["fluido_manometrico"])),
        width="stretch",
    )
    st.latex(r"\Delta P=\rho g\Delta h \qquad \Delta h=\frac{\Delta P}{\rho g}")
    st.info(gerar_interpretacao_manometro(altura_cm))
    st.caption(
        f"Altura física calculada: {altura_m:.4f} m. O desenho normaliza a escala "
        "para continuar legível; o valor numérico é o resultado quantitativo."
    )
    st.plotly_chart(criar_grafico_pressao_tempo(resultados), width="stretch")

with abas[4]:
    st.header("5. Abrir recipiente")
    exibir_guia_didatico_aba(
        objetivo="Estima o trabalho do gás ao passar do estado final para a atmosfera.",
        conceito="Trabalho de expansão isotérmica idealizada de um gás ideal.",
        formula_principal="W ≈ nRT ln(P_i/P_f)",
        interpretacao=(
            "O trabalho é positivo somente quando a pressão interna supera a externa. "
            "O resultado é uma estimativa energética, não a dinâmica real da abertura."
        ),
        fala_apresentacao=(
            "Usamos o último estado da simulação como condição antes da abertura. "
            "Idealizamos uma expansão isotérmica até a pressão atmosférica e calculamos "
            "o trabalho; não simulamos o escoamento rápido do gás."
        ),
    )
    abertura_1, abertura_2, abertura_3 = st.columns(3)
    abertura_1.metric("Pressão antes da abertura", f"{estado_final['pressao_absoluta_kpa']:.2f} kPa")
    abertura_2.metric("Pressão final assumida", f"{converter_pa_para_kpa(estado['pressao_atmosferica_pa']):.2f} kPa")
    abertura_3.metric(
        "Queda de pressão",
        f"{max(0.0, estado_final['pressao_manometrica_kpa']):.2f} kPa",
    )
    st.latex(r"W\approx nRT\ln\left(\frac{P_i}{P_f}\right)")

    if st.button("💨 Abrir recipiente", type="primary", width="stretch"):
        trabalho_j, trabalho_kj, mensagem_trabalho = calcular_trabalho_expansao_isotermica(
            estado["quantidade_mols"],
            float(estado_final["temperatura_k"]),
            float(estado_final["pressao_absoluta_pa"]),
            estado["pressao_atmosferica_pa"],
        )
        trabalho_1, trabalho_2 = st.columns(2)
        trabalho_1.metric("Trabalho estimado", f"{trabalho_j:.3f} J")
        trabalho_2.metric("Trabalho estimado", f"{trabalho_kj:.6f} kJ")
        st.success(mensagem_trabalho)
    else:
        st.info("Acione o botão para calcular a expansão idealizada do estado final.")
    st.warning(
        "A abertura real é transiente, não necessariamente isotérmica e envolve escoamento. "
        "O cálculo acima é uma estimativa energética didática, não uma previsão industrial."
    )

with abas[5]:
    st.header("6. Resumo e alertas")
    exibir_guia_didatico_aba(
        objetivo="Reúne os resultados principais e classifica a pressão em faixas didáticas.",
        conceito="Interpretação integrada de pressão, temperatura, calor e hipóteses.",
        formula_principal="P_man = P_abs - P_atm",
        interpretacao=(
            "Use o resumo para comparar o início e o fim. As categorias de alerta "
            "servem apenas para discussão acadêmica e não indicam segurança real."
        ),
        fala_apresentacao=(
            "Por fim, reunimos as mudanças de temperatura, pressão e calor e mostramos "
            "uma classificação apenas didática. O ponto mais importante é que o modelo "
            "permite interpretar tendências, mas não certifica um recipiente real."
        ),
    )
    nivel, mensagem, recomendacao, cor = classificar_nivel_pressao(
        float(estado_final["pressao_manometrica_kpa"])
    )
    st.metric("Nível didático de pressão", nivel)
    if cor == "verde":
        st.success(mensagem)
    elif cor == "amarelo":
        st.warning(mensagem)
    else:
        st.error(mensagem)
    st.write(f"**Recomendação de análise:** {recomendacao}")

    st.subheader("Resumo do cenário")
    st.markdown(
        f"""
        - A bebida passou de **{float(parametros['temperatura_inicial_c']):.2f} °C** para
          **{estado_final['temperatura_c']:.2f} °C**.
        - A pressão absoluta passou de **{converter_pa_para_kpa(estado['pressao_absoluta_inicial_pa']):.2f} kPa**
          para **{estado_final['pressao_absoluta_kpa']:.2f} kPa**.
        - O calor líquido acumulado foi **{estado_final['calor_acumulado_kj']:.3f} kJ**.
        - A pressão varia com a temperatura porque **n** e **V** permanecem constantes no recipiente fechado.
        """
    )
    st.subheader("Hipóteses e limitações")
    st.markdown(
        """
        - gás ideal, sem gás dissolvido no líquido;
        - líquido aproximado como água e com temperatura uniforme;
        - volume gasoso e quantidade de matéria constantes antes da abertura;
        - coeficiente global U constante e ambiente com temperatura fixa;
        - pressão atmosférica por aproximação linear;
        - nenhuma análise de espuma, mudança de fase, escoamento ou resistência estrutural.
        """
    )
    st.error(
        "Os alertas são categorias didáticas de comparação. Não certificam segurança, "
        "não definem limites de operação e não devem orientar o uso de recipientes reais."
    )

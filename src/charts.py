"""Gráficos interativos e esquema do manômetro virtual em Plotly."""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


COR_AZUL = "#2563EB"
COR_LARANJA = "#F97316"
COR_VERDE = "#059669"
COR_VERMELHO = "#DC2626"


def _aplicar_layout_padrao(figura: go.Figure, titulo: str) -> go.Figure:
    """Aplica um estilo visual comum e discreto aos gráficos do aplicativo."""
    figura.update_layout(
        title=titulo,
        template="plotly_white",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=55, b=20),
        legend_title_text="",
    )
    return figura


def criar_grafico_temperatura_tempo(resultados: pd.DataFrame) -> go.Figure:
    """Cria o gráfico interativo da temperatura da bebida ao longo do tempo."""
    figura = px.line(
        resultados,
        x="tempo_h",
        y="temperatura_c",
        labels={"tempo_h": "Tempo (h)", "temperatura_c": "Temperatura (°C)"},
    )
    figura.update_traces(line=dict(color=COR_LARANJA, width=3), name="Bebida")
    return _aplicar_layout_padrao(figura, "Temperatura da bebida × tempo")


def criar_grafico_pressao_tempo(resultados: pd.DataFrame) -> go.Figure:
    """Cria um gráfico comparando pressão absoluta e manométrica no tempo."""
    figura = go.Figure()
    figura.add_trace(
        go.Scatter(
            x=resultados["tempo_h"],
            y=resultados["pressao_absoluta_kpa"],
            mode="lines",
            name="Pressão absoluta",
            line=dict(color=COR_AZUL, width=3),
        )
    )
    figura.add_trace(
        go.Scatter(
            x=resultados["tempo_h"],
            y=resultados["pressao_manometrica_kpa"],
            mode="lines",
            name="Pressão manométrica",
            line=dict(color=COR_VERDE, width=3, dash="dash"),
        )
    )
    figura.update_xaxes(title_text="Tempo (h)")
    figura.update_yaxes(title_text="Pressão (kPa)")
    return _aplicar_layout_padrao(figura, "Pressões × tempo")


def criar_grafico_calor_tempo(resultados: pd.DataFrame) -> go.Figure:
    """Cria o gráfico do calor acumulado recebido ou cedido pela bebida."""
    figura = px.area(
        resultados,
        x="tempo_h",
        y="calor_acumulado_kj",
        labels={"tempo_h": "Tempo (h)", "calor_acumulado_kj": "Calor acumulado (kJ)"},
    )
    figura.update_traces(line=dict(color=COR_VERDE, width=3), fillcolor="rgba(5,150,105,0.20)")
    return _aplicar_layout_padrao(figura, "Calor acumulado × tempo")


def criar_figura_manometro_virtual(
    altura_coluna_cm: float, fluido_manometrico: str
) -> go.Figure:
    """
    Cria uma representação esquemática de um manômetro em U.

    A escala visual é normalizada para manter a figura legível mesmo quando a
    altura física calculada é muito grande. O valor numérico real aparece na
    anotação e deve ser usado na interpretação quantitativa.
    """
    deslocamento_visual = max(-3.2, min(3.2, altura_coluna_cm / 25.0))
    nivel_esquerdo = -deslocamento_visual / 2.0
    nivel_direito = deslocamento_visual / 2.0

    figura = go.Figure()

    # Contorno das duas pernas e da curva inferior do tubo em U.
    figura.add_trace(
        go.Scatter(
            x=[-1.4, -1.4, -1.4, -1.2, -0.8, 0.8, 1.2, 1.4, 1.4, 1.4],
            y=[5.0, -3.0, -3.4, -3.8, -4.0, -4.0, -3.8, -3.4, -3.0, 5.0],
            mode="lines",
            line=dict(color="#334155", width=8),
            hoverinfo="skip",
            showlegend=False,
        )
    )

    # Segmentos coloridos representam o fluido em cada lado do tubo.
    figura.add_trace(
        go.Scatter(
            x=[-1.4, -1.4, -1.2, -0.8, 0.8, 1.2, 1.4, 1.4],
            y=[nivel_esquerdo, -3.2, -3.7, -3.9, -3.9, -3.7, -3.2, nivel_direito],
            mode="lines",
            line=dict(color=COR_AZUL, width=12),
            name=fluido_manometrico,
            hoverinfo="skip",
        )
    )

    figura.add_annotation(x=-1.4, y=5.4, text="Recipiente", showarrow=False)
    figura.add_annotation(x=1.4, y=5.4, text="Atmosfera", showarrow=False)
    figura.add_annotation(
        x=0,
        y=3.4,
        text=f"Δh calculado = {altura_coluna_cm:.2f} cm<br><sup>desenho com escala normalizada</sup>",
        showarrow=False,
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="#CBD5E1",
    )
    figura.update_xaxes(visible=False, range=[-3.2, 3.2])
    figura.update_yaxes(visible=False, range=[-4.8, 6.0], scaleanchor="x", scaleratio=0.6)
    figura.update_layout(
        template="plotly_white",
        height=430,
        margin=dict(l=10, r=10, t=15, b=10),
        showlegend=False,
    )
    return figura


def criar_figura_abertura_recipiente_pressurizado(
    pressao_interna_atual_kpa: float,
    pressao_atmosferica_kpa: float,
    progresso_equalizacao: float,
) -> go.Figure:
    """
    Cria um quadro esquemático da abertura de um recipiente pressurizado.

    A figura mostra recipiente, tampa, região gasosa e partículas meramente
    ilustrativas. ``progresso_equalizacao`` deve variar de 0 a 1 e controla
    somente a apresentação visual; ele não representa tempo físico nem resolve
    o escoamento real durante a abertura.

    Args:
        pressao_interna_atual_kpa: pressão absoluta exibida no quadro, em kPa.
        pressao_atmosferica_kpa: pressão atmosférica de referência, em kPa.
        progresso_equalizacao: fração visual da abertura entre 0 e 1.

    Returns:
        Figura Plotly com o estado visual da abertura.
    """
    progresso = max(0.0, min(1.0, progresso_equalizacao))
    sobrepressao_kpa = max(0.0, pressao_interna_atual_kpa - pressao_atmosferica_kpa)

    figura = go.Figure()

    # Corpo, líquido e região gasosa formam um desenho esquemático do recipiente.
    figura.add_shape(
        type="rect", x0=0.35, x1=1.65, y0=0.2, y1=4.0,
        line=dict(color="#334155", width=5), fillcolor="rgba(255,255,255,0.15)",
    )
    figura.add_shape(
        type="rect", x0=0.75, x1=1.25, y0=4.0, y1=5.0,
        line=dict(color="#334155", width=5), fillcolor="rgba(255,255,255,0.15)",
    )
    figura.add_shape(
        type="rect", x0=0.4, x1=1.6, y0=0.25, y1=2.55,
        line=dict(width=0), fillcolor="rgba(37,99,235,0.60)",
    )

    # A cor do espaço gasoso perde intensidade conforme a sobrepressão diminui.
    intensidade_gas = min(0.65, 0.18 + sobrepressao_kpa / 600.0)
    figura.add_shape(
        type="rect", x0=0.4, x1=1.6, y0=2.55, y1=3.95,
        line=dict(width=0), fillcolor=f"rgba(249,115,22,{intensidade_gas:.3f})",
    )

    # A tampa sobe e se desloca para a direita no começo da sequência.
    deslocamento_tampa = min(1.0, progresso * 4.0)
    figura.add_shape(
        type="rect",
        x0=0.68 + 0.75 * deslocamento_tampa,
        x1=1.32 + 0.75 * deslocamento_tampa,
        y0=5.0 + 0.55 * deslocamento_tampa,
        y1=5.25 + 0.55 * deslocamento_tampa,
        line=dict(color="#0F172A", width=3),
        fillcolor="#64748B",
    )

    # Partículas apenas sugerem visualmente a saída; não representam massa ou velocidade.
    if 0.0 < progresso < 0.95 and sobrepressao_kpa > 0.0:
        intensidade_particulas = max(0.15, 1.0 - progresso)
        figura.add_trace(
            go.Scatter(
                x=[0.88, 1.08, 1.27, 1.43, 1.58],
                y=[5.15, 5.42, 5.72, 6.02, 6.30],
                mode="markers",
                marker=dict(
                    size=[13, 11, 9, 7, 5],
                    color=COR_LARANJA,
                    opacity=intensidade_particulas,
                ),
                hoverinfo="skip",
                showlegend=False,
            )
        )

    figura.add_annotation(
        x=1.0,
        y=3.3,
        text=f"P interna<br><b>{pressao_interna_atual_kpa:.1f} kPa</b>",
        showarrow=False,
        font=dict(color="#7C2D12", size=15),
    )
    figura.add_annotation(
        x=2.75,
        y=3.3,
        text=f"Atmosfera<br><b>{pressao_atmosferica_kpa:.1f} kPa</b>",
        showarrow=False,
        bordercolor="#94A3B8",
        borderwidth=1,
        bgcolor="rgba(248,250,252,0.9)",
    )
    figura.add_annotation(
        x=2.0,
        y=1.0,
        text=f"Equalização visual: {progresso * 100:.0f}%",
        showarrow=False,
        font=dict(size=16, color=COR_VERDE if progresso >= 1.0 else COR_VERMELHO),
    )

    figura.update_xaxes(visible=False, range=[0.0, 3.6])
    figura.update_yaxes(visible=False, range=[0.0, 6.7])
    figura.update_layout(
        template="plotly_white",
        height=430,
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
    )
    return figura

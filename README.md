# PressurizaLab: Simulador Computacional de Pressão, Calor e Trabalho em Recipientes Pressurizados

### Alunos: Caroline Lanzuolo e Ian Andriani

### Professor: Rogério Gomes de Oliveira

### Disciplina: Fenômenos de Transporte

### Semestre: 2026.1

---

## 1. Descrição do Projeto

O **PressurizaLab** é um software interativo desenvolvido em **Python com Streamlit** para simular, de forma simplificada e didática, o comportamento termodinâmico de um recipiente pressurizado contendo líquido e uma região gasosa.

A aplicação utiliza como contexto prático um recipiente semelhante a uma garrafa/lata com bebida, mas o objetivo principal não é reproduzir de forma completa o comportamento real de uma bebida gaseificada. O objetivo é construir um **modelo físico simplificado**, aderente aos conteúdos da primeira avaliação da disciplina, envolvendo:

* pressão absoluta;
* pressão manométrica;
* pressão atmosférica;
* manometria;
* coluna de fluido;
* gás ideal;
* transferência de calor;
* trabalho de expansão;
* variação temporal de temperatura e pressão;
* análise computacional e visualização de dados.

O produto funciona como um **protótipo digital de monitoramento termodinâmico**, permitindo que o usuário configure um cenário, simule sua evolução ao longo do tempo e visualize os fenômenos físicos envolvidos.

---

## 2. Justificativa da Escolha do Tema

A proposta final surgiu da mescla entre duas ideias:

1. **Ideia inicial da Caroline:**
   Um sistema inteligente de monitoramento termodinâmico para bebidas pressurizadas.

2. **Ideia de maximização de conteúdo:**
   Um simulador computacional interativo cobrindo os principais tópicos da primeira avaliação de Fenômenos de Transporte.

A decisão de mesclar as duas ideias foi tomada porque cada uma possui uma vantagem importante dentro dos critérios de avaliação do trabalho.

A ideia da Caroline possui maior força como **produto**, pois apresenta um contexto real, uma aplicação prática, interface, alertas, simulação temporal e potencial de inovação. Porém, se tratada como uma simulação realista de bebida gaseificada, ela poderia exigir conceitos que não foram foco da primeira avaliação, como solubilidade de gases, comportamento real do CO₂ dissolvido, formação de espuma e equilíbrio químico.

A ideia de simulador geral possui maior segurança em relação à **aderência ao conteúdo da disciplina**, pois permite cobrir diretamente pressão, manometria, trabalho, calor e gás ideal. Porém, sozinha, poderia parecer apenas uma calculadora didática de exercícios.

Por isso, a solução adotada foi:

> Usar a ideia de recipiente/bebida pressurizada como narrativa e produto, mas estruturar o sistema internamente como um simulador dos conteúdos da primeira avaliação.

Assim, o projeto busca maximizar simultaneamente:

* aderência ao conteúdo da disciplina;
* qualidade da modelagem;
* clareza didática;
* conexão com Engenharia de Computação;
* inovação;
* potencial de demonstração na apresentação oral.

---

## 3. Estratégia para Maximização dos Critérios de Avaliação

O trabalho será desenvolvido considerando diretamente os critérios avaliados pelo professor.

---

### 3.1. Critério A — Quantidade de Conteúdo Aderente

Para maximizar a quantidade de conteúdo aderente, o produto não ficará restrito a um único fenômeno físico. O sistema será dividido em módulos conectados por um mesmo cenário físico.

Os principais conteúdos da primeira avaliação contemplados serão:

* propriedades termodinâmicas;
* pressão absoluta;
* pressão manométrica;
* pressão atmosférica;
* massa específica;
* gás ideal;
* manometria;
* coluna de fluido;
* transferência de calor;
* condução/convecção simplificada;
* trabalho realizado por expansão de gás;
* unidades e dimensões;
* gráficos e interpretação física.

Dessa forma, o projeto cobre uma quantidade significativa do conteúdo lecionado, sem depender de tópicos externos à disciplina.

---

### 3.2. Critério B — Qualidade

Para maximizar a qualidade, o projeto será baseado em modelos físicos simples, mas bem definidos.

O sistema deixará explícitas as hipóteses simplificadoras utilizadas, evitando prometer uma simulação realista demais. A aplicação apresentará:

* equações utilizadas;
* unidades;
* variáveis de entrada;
* variáveis de saída;
* interpretação física dos resultados;
* gráficos;
* validações com cenários semelhantes aos estudados em aula;
* limitações do modelo.

O foco será demonstrar domínio dos conceitos, e não criar um modelo industrial completo.

---

### 3.3. Critério C — Conteúdo Não Aderente

A narrativa de bebida pressurizada será usada apenas como aplicação prática.

O projeto evitará aprofundar tópicos que não fazem parte do escopo da primeira avaliação, como:

* solubilidade real do CO₂;
* formação de espuma;
* equilíbrio líquido-vapor complexo;
* ruptura estrutural real da garrafa;
* cinética de liberação de gás;
* modelagem química da carbonatação.

Esses temas poderão ser citados apenas como limitações do modelo, mas não serão usados como base principal do projeto.

Isso reduz o risco de o trabalho parecer não aderente ao conteúdo da disciplina.

---

### 3.4. Critério D — Aderência, Relevância e Qualidade para Engenharia de Computação

O projeto possui forte relação com Engenharia de Computação porque será desenvolvido como uma aplicação computacional interativa.

A aplicação utilizará:

* Python;
* Streamlit;
* simulação numérica;
* modularização de código;
* interface gráfica;
* entrada de parâmetros;
* geração de gráficos;
* validação de unidades;
* alertas inteligentes;
* visualização de dados;
* organização em módulos físicos e computacionais.

O sistema também simula uma aplicação de monitoramento inteligente, semelhante a um produto embarcado ou sistema de apoio à decisão.

---

### 3.5. Critério E — Inovação

A inovação está na transformação de conteúdos teóricos da primeira avaliação em um produto digital interativo.

Em vez de apenas apresentar fórmulas ou resolver exercícios manualmente, o PressurizaLab permite que o usuário altere parâmetros e observe como o sistema responde.

Elementos inovadores do produto:

* simulação temporal;
* gráficos dinâmicos;
* manômetro virtual;
* alerta de pressão;
* botão de abertura do recipiente;
* comparação entre estado inicial e final;
* análise integrada de pressão, calor e trabalho;
* aplicação dos conceitos em um cenário cotidiano.

---

### 3.6. Apresentação Oral

A apresentação será preparada para maximizar os critérios de demonstração de conhecimento e clareza.

A estratégia será:

1. explicar o problema físico;
2. apresentar as hipóteses;
3. demonstrar os módulos do software;
4. relacionar cada módulo com os conteúdos da disciplina;
5. mostrar os gráficos e interpretar fisicamente;
6. responder perguntas sobre equações, unidades e limitações.

Como o produto é interativo, a apresentação poderá mostrar variações em tempo real, como:

* aumentar a temperatura ambiente;
* alterar o volume de gás;
* variar a altitude;
* observar mudança na pressão;
* abrir o recipiente;
* analisar a leitura do manômetro.

---

## 4. O Que Será Mantido da Ideia Original

A ideia original da Caroline será mantida como base conceitual do produto.

Serão mantidos:

* o contexto de bebidas/recipientes pressurizados;
* a ideia de sistema inteligente;
* a simulação de pressão interna;
* a análise da temperatura da bebida;
* a transferência de calor com o ambiente;
* a relação entre temperatura e pressão;
* a leitura por manometria;
* a abertura do recipiente;
* os alertas visuais de segurança;
* os gráficos de evolução temporal;
* a interface interativa.

Esses elementos dão ao trabalho uma identidade de produto e reforçam a conexão com Engenharia de Computação.

---

## 5. O Que Será Cortado ou Reduzido da Ideia Original

Alguns elementos da proposta original serão cortados ou reduzidos para manter o trabalho aderente, viável e defensável na apresentação.

Serão removidos ou tratados apenas como limitações:

### 5.1. Modelagem Real de Bebida Gaseificada

Não será modelado o comportamento real do CO₂ dissolvido na bebida.

Motivo:

* isso exigiria conteúdos além da primeira avaliação;
* poderia abrir margem para perguntas complexas;
* aumentaria o risco de baixa qualidade na modelagem.

O sistema considerará apenas o gás presente no espaço superior do recipiente, tratado como gás ideal.

---

### 5.2. Espuma e Carbonatação

O sistema não simulará espuma, bolhas ou liberação real de gás dissolvido.

Esses efeitos serão citados como limitações do modelo.

---

### 5.3. Ruptura Real da Garrafa

O sistema não calculará ruptura estrutural real do recipiente.

Em vez disso, haverá apenas um alerta didático de pressão elevada, usando limites configuráveis.

---

### 5.4. Backend Complexo ou React

A aplicação será feita em Streamlit, sem necessidade de React, API separada ou backend complexo.

Motivo:

* reduzir tempo de implementação;
* facilitar execução pelo professor;
* permitir foco maior na física e na apresentação;
* evitar problemas técnicos no dia da entrega.

---

### 5.5. Relatório Automático em PDF

O relatório automático em PDF será considerado opcional.

O foco principal será:

* aplicação funcionando;
* README bem documentado;
* material descritivo;
* apresentação oral.

---

## 6. O Que Será Adicionado da Ideia de Maximização de Conteúdo

A proposta será enriquecida com elementos da ideia de simulador abrangente dos tópicos da primeira prova.

Serão adicionados:

* organização por módulos físicos;
* validação com cenários semelhantes aos da primeira avaliação;
* maior ênfase em pressão, manometria, calor e trabalho;
* explicação explícita das equações;
* interpretação dos resultados;
* gráficos didáticos;
* seção de hipóteses simplificadoras;
* seção de limitações;
* possibilidade de carregar exemplos prontos.

O objetivo é evitar que o produto seja apenas uma simulação visual e garantir que ele demonstre quantidade e qualidade de conteúdo aderente.

---

## 7. Escopo Final do Produto

O PressurizaLab será organizado em abas. Cada aba representa uma etapa do sistema físico, e não apenas uma fórmula isolada.

A sequência lógica será:

1. configurar o recipiente;
2. calcular o estado termodinâmico;
3. simular transferência de calor;
4. medir a pressão por manometria;
5. abrir o recipiente e estimar trabalho;
6. analisar segurança;
7. validar com casos de estudo.

---

## 8. Estrutura das Abas

---

### 8.1. Aba 1 — Configuração do Recipiente

Nesta aba, o usuário define os parâmetros iniciais do sistema.

Entradas:

* tipo de recipiente;
* material do recipiente;
* volume total;
* volume de líquido;
* volume de gás;
* temperatura inicial do líquido;
* temperatura ambiente;
* altitude;
* tempo de simulação;
* fluido manométrico.

Exemplos de materiais:

* PET;
* alumínio;
* vidro;
* aço inox.

Exemplos de fluidos manométricos:

* água;
* mercúrio;
* óleo.

Objetivo físico:

* definir o sistema;
* caracterizar as propriedades iniciais;
* trabalhar com unidades e dimensões.

Objetivo computacional:

* receber parâmetros do usuário;
* validar entradas;
* preparar os dados para os demais módulos.

---

### 8.2. Aba 2 — Estado Termodinâmico Atual

Nesta aba, o sistema calcula o estado inicial do recipiente.

Saídas:

* temperatura inicial;
* pressão atmosférica local;
* pressão absoluta interna;
* pressão manométrica;
* volume de gás;
* quantidade de matéria do gás;
* massa aproximada de líquido;
* massa específica aproximada.

Equações utilizadas:

```text
P_abs = nRT / V_gás
P_man = P_abs - P_atm
P_atm ≈ P0 - ρ_ar g h
```

Onde:

* `P_abs` é a pressão absoluta;
* `P_man` é a pressão manométrica;
* `P_atm` é a pressão atmosférica;
* `n` é a quantidade de matéria;
* `R` é a constante universal dos gases;
* `T` é a temperatura absoluta;
* `V_gás` é o volume ocupado pelo gás.

Hipótese:

* o gás presente no espaço superior do recipiente é tratado como gás ideal.

---

### 8.3. Aba 3 — Transferência de Calor

Nesta aba, o sistema simula a troca de calor entre o ambiente e o recipiente.

Saídas:

* taxa de transferência de calor;
* calor acumulado;
* temperatura da bebida ao longo do tempo;
* sentido do fluxo de calor;
* gráfico Temperatura × Tempo;
* gráfico Calor Transferido × Tempo.

Modelo simplificado:

```text
Q̇ = U A (T_amb - T_bebida)
m c dT/dt = Q̇
```

Onde:

* `Q̇` é a taxa de transferência de calor;
* `U` é o coeficiente global de transferência de calor;
* `A` é a área superficial aproximada;
* `T_amb` é a temperatura ambiente;
* `T_bebida` é a temperatura da bebida;
* `m` é a massa da bebida;
* `c` é o calor específico.

Hipóteses:

* a bebida é considerada bem misturada;
* a temperatura interna da bebida é uniforme;
* o modelo usa uma aproximação concentrada;
* o coeficiente global `U` representa efeitos combinados de condução e convecção.

---

### 8.4. Aba 4 — Pressão e Manômetro Virtual

Nesta aba, o sistema relaciona a pressão interna com uma leitura de manômetro em U.

Saídas:

* pressão absoluta;
* pressão manométrica;
* diferença de altura da coluna;
* gráfico Pressão × Tempo;
* representação visual simplificada do manômetro.

Equação utilizada:

```text
ΔP = ρ g Δh
Δh = ΔP / (ρ g)
```

Onde:

* `ΔP` é a diferença de pressão;
* `ρ` é a massa específica do fluido manométrico;
* `g` é a aceleração da gravidade;
* `Δh` é a diferença de altura da coluna.

Objetivo físico:

* demonstrar a relação entre pressão e coluna de fluido;
* diferenciar pressão absoluta e pressão manométrica;
* aplicar o conceito de manometria.

Objetivo computacional:

* transformar uma grandeza calculada em uma visualização física;
* apresentar dados numéricos e visuais ao usuário.

---

### 8.5. Aba 5 — Abertura do Recipiente e Trabalho de Expansão

Nesta aba, o usuário pode simular a abertura do recipiente.

Antes da abertura, o sistema mostra:

* pressão interna;
* pressão atmosférica;
* pressão manométrica;
* temperatura do gás.

Após a abertura, o sistema mostra:

* pressão final;
* variação de pressão;
* energia/trabalho estimado;
* interpretação do resultado.

Modelo principal:

```text
W ≈ nRT ln(P_i / P_f)
```

Onde:

* `W` é o trabalho estimado;
* `n` é a quantidade de matéria do gás;
* `R` é a constante universal dos gases;
* `T` é a temperatura absoluta;
* `P_i` é a pressão inicial;
* `P_f` é a pressão final, assumida como pressão atmosférica.

Modelo alternativo simplificado:

```text
W ≈ P_média ΔV
```

Hipóteses:

* expansão idealizada;
* comportamento isotérmico aproximado;
* gás ideal;
* objetivo didático, não industrial.

---

### 8.6. Aba 6 — Alertas e Análise de Segurança

Nesta aba, o sistema apresenta uma análise qualitativa do estado do recipiente.

Saídas:

* indicador de pressão baixa, moderada ou elevada;
* alerta visual;
* resumo da temperatura;
* resumo da pressão;
* recomendação didática.

Exemplo de níveis:

* verde: pressão manométrica baixa;
* amarelo: pressão manométrica moderada;
* vermelho: pressão manométrica elevada.

Observação:

Os limites não representam certificação real de segurança. Eles servem apenas como ferramenta didática para interpretar os resultados da simulação.

---

### 8.7. Aba 7 — Casos de Estudo e Validação

Esta aba será usada para demonstrar que o produto está conectado ao conteúdo da primeira avaliação.

Em vez de criar uma aba para cada enunciado, o sistema apresentará cenários prontos semelhantes aos tipos de problema trabalhados em aula.

Exemplos de casos:

1. recipiente em ambiente quente;
2. recipiente em altitude elevada;
3. variação de volume gasoso;
4. comparação entre materiais;
5. leitura por manômetro;
6. abertura do recipiente pressurizado.

Cada caso terá:

* valores de entrada;
* resultados esperados;
* interpretação física;
* equações utilizadas.

Essa aba ajuda na apresentação oral e na demonstração de conhecimento.

---

## 9. Módulo Opcional — Flutuação e Empuxo

Caso haja tempo, será implementado um módulo opcional de flutuação do recipiente.

Objetivo:

* calcular se o recipiente flutuaria ou afundaria em água;
* relacionar massa total, volume deslocado e empuxo;
* ampliar a quantidade de conteúdo aderente.

Equações:

```text
E = ρ_fluido g V_deslocado
P = m_total g
```

Interpretação:

* se o empuxo for maior que o peso, o recipiente tende a flutuar;
* se o peso for maior que o empuxo, o recipiente tende a afundar.

Esse módulo não é essencial para o MVP, mas pode aumentar a abrangência do trabalho se houver tempo.

---

## 10. Hipóteses Simplificadoras do Modelo

O modelo do PressurizaLab será simplificado para manter aderência à disciplina e viabilidade de implementação.

Hipóteses adotadas:

1. O gás no espaço superior do recipiente é tratado como gás ideal.
2. A bebida é aproximada como água.
3. A temperatura da bebida é considerada uniforme.
4. O recipiente é considerado fechado antes da abertura.
5. O volume do gás é considerado constante antes da abertura.
6. A transferência de calor é modelada por coeficiente global simplificado.
7. A pressão atmosférica é estimada por modelo linear simplificado com a altitude.
8. A abertura do recipiente é tratada como expansão idealizada.
9. O sistema não modela CO₂ dissolvido.
10. O sistema não modela espuma, bolhas ou ruptura real do recipiente.

Essas hipóteses serão apresentadas no relatório e na apresentação para deixar claro o escopo físico do produto.

---

## 11. Arquitetura Computacional

A aplicação será desenvolvida em Python utilizando Streamlit.

Bibliotecas previstas:

* `streamlit`;
* `numpy`;
* `pandas`;
* `matplotlib` ou `plotly`.

Estrutura sugerida do projeto:

```text
pressurizalab/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── constants.py
│   ├── pressure.py
│   ├── heat_transfer.py
│   ├── manometer.py
│   ├── work.py
│   ├── safety.py
│   └── simulation.py
│
└── docs/
    ├── relatorio.pdf
    └── apresentacao.pdf
```

---

## 12. Responsabilidade de Cada Módulo

### `constants.py`

Define constantes físicas:

* gravidade;
* constante dos gases;
* pressão atmosférica ao nível do mar;
* densidade do ar;
* propriedades aproximadas de materiais;
* propriedades aproximadas de fluidos manométricos.

---

### `pressure.py`

Responsável por:

* calcular pressão atmosférica;
* calcular pressão absoluta;
* calcular pressão manométrica;
* aplicar gás ideal.

---

### `heat_transfer.py`

Responsável por:

* calcular taxa de transferência de calor;
* calcular evolução da temperatura;
* calcular calor acumulado;
* preparar dados para gráficos.

---

### `manometer.py`

Responsável por:

* calcular diferença de altura no manômetro;
* converter metros para centímetros ou milímetros;
* preparar dados para visualização.

---

### `work.py`

Responsável por:

* calcular trabalho estimado de expansão;
* calcular variação de pressão;
* comparar estado antes e depois da abertura.

---

### `safety.py`

Responsável por:

* classificar níveis de pressão;
* retornar alerta visual;
* gerar mensagens didáticas.

---

### `simulation.py`

Responsável por:

* integrar a simulação temporal;
* gerar vetores de tempo;
* calcular temperatura e pressão a cada passo.

---

## 13. MVP — Produto Mínimo Viável

O MVP precisa conter obrigatoriamente:

1. interface em Streamlit;
2. configuração de parâmetros do recipiente;
3. cálculo de pressão atmosférica;
4. cálculo de pressão absoluta e manométrica;
5. simulação de temperatura ao longo do tempo;
6. gráfico Temperatura × Tempo;
7. gráfico Pressão × Tempo;
8. manômetro virtual;
9. abertura do recipiente;
10. estimativa de trabalho;
11. alertas visuais;
12. README explicativo;
13. relatório ou material descritivo.

Com esse MVP, o trabalho já atende bem aos critérios de produto, conteúdo e computação.

---

## 14. Funcionalidades Opcionais

Caso haja tempo, podem ser adicionadas:

* módulo de flutuação e empuxo;
* comparação entre diferentes materiais;
* exportação de resultados;
* presets de cenários;
* animação simples do manômetro;
* modo escuro;
* relatório automático;
* mais exemplos semelhantes aos exercícios.

Essas funcionalidades não são necessárias para o funcionamento principal, mas podem melhorar a percepção de qualidade e inovação.

---

## 15. Entregáveis

Serão entregues:

1. Código-fonte do aplicativo.
2. Arquivo `requirements.txt`.
3. Arquivo `README.md`.
4. Relatório ou documento descritivo.
5. Apresentação em slides.
6. Demonstração funcional do software.

---

## 16. Como Executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar aplicação:

```bash
streamlit run app.py
```

---

## 17. Relação com Fenômenos de Transporte

O PressurizaLab se relaciona com a disciplina por aplicar os conceitos físicos em um sistema integrado.

| Módulo                 | Conteúdo da Disciplina                   |
| ---------------------- | ---------------------------------------- |
| Configuração           | propriedades, unidades, sistema          |
| Estado termodinâmico   | pressão, gás ideal, massa específica     |
| Transferência de calor | calor, taxa de calor, convecção/condução |
| Manômetro virtual      | hidrostática, pressão, coluna de fluido  |
| Abertura do recipiente | trabalho, expansão, energia              |
| Alertas                | interpretação física dos resultados      |
| Casos de estudo        | aplicação dos conceitos da avaliação     |

---

## 18. Relação com Engenharia de Computação

O projeto também possui forte aderência ao curso de Engenharia de Computação.

Aspectos computacionais:

* desenvolvimento de software;
* interface gráfica;
* simulação numérica;
* modularização;
* visualização de dados;
* processamento de entradas;
* geração de gráficos;
* alertas inteligentes;
* organização de arquitetura;
* documentação técnica.

O produto pode ser interpretado como um protótipo digital de um sistema de monitoramento, semelhante a aplicações de sensores, sistemas embarcados e análise de dados.

---

## 19. Estratégia para Apresentação Oral

A apresentação será organizada para demonstrar domínio técnico e clareza.

Roteiro sugerido:

1. Apresentação do problema.
2. Justificativa do produto.
3. Explicação das hipóteses simplificadoras.
4. Demonstração da configuração do sistema.
5. Demonstração da pressão e gás ideal.
6. Demonstração da transferência de calor.
7. Demonstração do manômetro virtual.
8. Demonstração da abertura e trabalho de expansão.
9. Discussão dos alertas.
10. Relação com Engenharia de Computação.
11. Limitações e possíveis melhorias.

---

## 20. Divisão de Tarefas

Sugestão de divisão:

### Ian

* implementação em Python;
* estrutura do Streamlit;
* módulos de cálculo;
* gráficos;
* organização do repositório;
* README técnico.

### Caroline

* revisão conceitual;
* relatório;
* explicação das equações;
* slides;
* hipóteses e limitações;
* organização da apresentação.

Apesar da divisão, ambos devem compreender todos os módulos, pois a apresentação oral será avaliada por perguntas do professor.

---

## 21. Cronograma

### Dia 1

* fechar escopo;
* criar projeto;
* montar estrutura inicial do Streamlit;
* criar abas.

### Dia 2

* implementar pressão atmosférica;
* implementar gás ideal;
* implementar pressão absoluta e manométrica.

### Dia 3

* implementar transferência de calor;
* gerar gráfico Temperatura × Tempo;
* gerar gráfico Calor × Tempo.

### Dia 4

* implementar manômetro virtual;
* implementar gráfico Pressão × Tempo.

### Dia 5

* implementar abertura do recipiente;
* calcular trabalho de expansão;
* implementar alertas.

### Dia 6

* melhorar interface;
* revisar unidades;
* escrever relatório;
* preparar apresentação.

### Dia 7

* testar aplicação;
* treinar apresentação;
* revisar possíveis perguntas.

---

## 22. Limitações do Projeto

O PressurizaLab é um modelo didático e simplificado.

Limitações:

* não simula CO₂ dissolvido;
* não simula formação de espuma;
* não calcula ruptura real do recipiente;
* não representa todos os fenômenos de uma bebida gaseificada real;
* utiliza aproximações para transferência de calor;
* utiliza aproximação para pressão atmosférica;
* utiliza modelo idealizado para expansão do gás.

Essas limitações não reduzem o objetivo acadêmico do trabalho, pois o foco é aplicar os conceitos estudados na primeira avaliação de forma integrada, visual e computacional.

---

## 23. Conclusão

O PressurizaLab foi proposto como uma solução intermediária entre um produto aplicado e um simulador didático.

A ideia de recipiente/bebida pressurizada fornece um contexto intuitivo e relevante, enquanto a estrutura de módulos físicos garante aderência aos conteúdos da disciplina.

A proposta busca maximizar a nota nos critérios avaliados por:

* cobrir vários conteúdos da primeira avaliação;
* apresentar um produto computacional funcional;
* usar modelos físicos explicáveis;
* demonstrar inovação por meio de simulação e visualização;
* permitir uma apresentação oral clara e interativa;
* evitar tópicos excessivamente complexos ou pouco aderentes.

Dessa forma, o projeto pretende equilibrar qualidade, quantidade de conteúdo, inovação e viabilidade de implementação dentro do prazo disponível.

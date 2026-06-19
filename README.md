# Sistema Inteligente de Monitoramento Termodinâmico para Bebidas Pressurizadas

## Descrição do Projeto

O Sistema Inteligente de Monitoramento Termodinâmico para Bebidas Pressurizadas é um software interativo desenvolvido para simular o comportamento termodinâmico de bebidas armazenadas em recipientes pressurizados.

O objetivo é demonstrar, de forma visual e interativa, conceitos de:

* Pressão absoluta
* Pressão manométrica
* Pressão atmosférica
* Coluna de líquido
* Manometria
* Gases ideais
* Transferência de calor
* Trabalho realizado por gases
* Variação temporal de propriedades termodinâmicas

O projeto foi idealizado como um protótipo digital de um produto inteligente capaz de monitorar as condições internas de uma bebida gaseificada.

---

# Problema

Bebidas pressurizadas sofrem alterações de pressão quando expostas a diferentes temperaturas e condições ambientais.

O usuário normalmente não possui informações sobre:

* Temperatura real da bebida
* Pressão interna do recipiente
* Quantidade de calor transferida
* Risco de excesso de pressão
* Comportamento da bebida ao longo do tempo

O sistema simula essas informações em tempo real.

---

# Objetivo Acadêmico

Aplicar conceitos dos capítulos iniciais de Termodinâmica e Fenômenos de Transporte:

* Pressão
* Gás Ideal
* Massa específica
* Coluna de líquido
* Manometria
* Transferência de calor
* Trabalho de expansão

---

# Fluxo Conceitual do Sistema

Temperatura Ambiente
↓
Transferência de Calor
↓
Temperatura da Bebida
↓
Pressão Interna
↓
Leitura do Manômetro
↓
Trabalho de Expansão ao Abrir a Garrafa

---

# Arquitetura do Sistema

## Entradas

O usuário poderá configurar:

* Tipo de bebida
* Temperatura inicial da bebida
* Temperatura ambiente
* Volume total da garrafa
* Volume de líquido
* Volume de gás acima do líquido
* Altitude
* Material da garrafa
* Tempo de simulação

---

# Tela 1 – Configuração Inicial

## Campos

### Bebida

* Água
* Refrigerante
* Cerveja
* Energético

### Temperatura Inicial

°C

### Temperatura Ambiente

°C

### Altitude

m

### Volume Total

mL

### Volume do Líquido

mL

### Volume de Gás

mL

### Material

* Plástico PET
* Alumínio
* Aço inox
* Vidro

---

# Tela 2 – Estado Termodinâmico Atual

## Exibir

### Temperatura Atual

°C

### Pressão Absoluta

kPa

### Pressão Manométrica

kPa

### Pressão Atmosférica Local

kPa

### Massa Específica do Líquido

kg/m³

---

# Equações Utilizadas

## Pressão Absoluta

Pabs = Patm + Pman

---

## Pressão Atmosférica

Modelo simplificado:

Patm = P0 - ρgh

onde:

* P0 = 101,3 kPa
* ρ = densidade do ar
* g = gravidade
* h = altitude

---

## Gás Ideal

PV = nRT

onde:

* P = pressão
* V = volume do gás
* n = quantidade de matéria
* R = constante universal dos gases
* T = temperatura absoluta

---

# Tela 3 – Transferência de Calor

## Objetivo

Demonstrar como o calor é transferido do ambiente para a bebida ou vice-versa.

## Exibir

### Taxa de Transferência de Calor

W

### Calor Acumulado

kJ

### Temperatura da Parede

°C

### Sentido do Fluxo de Calor

* Ambiente → Bebida
* Bebida → Ambiente

---

# Mecanismos de Transferência

## Condução

Q̇ = kAΔT/L

onde:

* k = condutividade térmica
* A = área
* ΔT = diferença de temperatura
* L = espessura

---

## Convecção

Q̇ = hA(Ts − T∞)

onde:

* h = coeficiente convectivo
* A = área superficial
* Ts = temperatura da superfície
* T∞ = temperatura do ambiente

---

# Tela 4 – Simulação Temporal

## Objetivo

Permitir observar a evolução do sistema ao longo do tempo.

## Botões

* Simular 1 hora
* Simular 6 horas
* Simular 24 horas

---

# Gráficos

## Temperatura × Tempo

Mostrar a evolução da temperatura da bebida.

---

## Pressão × Tempo

Mostrar a evolução da pressão interna.

---

## Calor Transferido × Tempo

Mostrar a energia acumulada.

---

# Tela 5 – Manometria

## Objetivo

Relacionar a pressão interna com a leitura de um manômetro em U.

## Exibir

* Manômetro virtual
* Diferença de altura da coluna
* Pressão medida

---

# Equação

ΔP = ρgh

onde:

* ρ = massa específica do fluido manométrico
* g = gravidade
* h = diferença de altura

---

# Tela 6 – Análise de Segurança e Trabalho

## Botão

Abrir Garrafa

---

## Antes da Abertura

Mostrar:

* Pressão interna
* Pressão atmosférica
* Pressão manométrica

---

## Após a Abertura

Mostrar:

* Pressão final
* Variação de pressão
* Energia liberada

---

# Trabalho de Expansão

W = ∫PdV

Para simplificação inicial:

W = P(V2 − V1)

---

# Alertas Inteligentes

## Pressão Elevada

Exibir alerta quando:

Pman > limite configurado

---

## Risco de Ruptura

Exibir indicador visual:

* Verde
* Amarelo
* Vermelho

---

# Tecnologias Recomendadas

## Backend

Python

Bibliotecas:

* NumPy
* SciPy

---

## Interface

Opção 1:

Streamlit

ou

Opção 2:

React + Python API

---

## Gráficos

* Plotly
* Matplotlib

---

# Entregáveis

## MVP

* Configuração do cenário
* Cálculo de pressão
* Cálculo de temperatura
* Cálculo de transferência de calor
* Simulação temporal
* Manômetro virtual

## Versão Completa

* Gráficos dinâmicos
* Alertas inteligentes
* Animação de abertura da garrafa
* Relatório automático em PDF

---

# Resultado Esperado

O sistema deverá permitir que o usuário compreenda visualmente como:

* O calor afeta a temperatura da bebida.
* A temperatura afeta a pressão interna.
* A pressão pode ser medida por manometria.
* A expansão do gás realiza trabalho.
* Todos esses fenômenos estão interligados dentro de um único sistema físico.

---
### Alunos: Caroline Lanzuolo e Ian Andriani
### Professor: Rogerio Gomes de Oliveira 
### Disciplina: Fenômenos de Transporte
### Semestre: 2026.1

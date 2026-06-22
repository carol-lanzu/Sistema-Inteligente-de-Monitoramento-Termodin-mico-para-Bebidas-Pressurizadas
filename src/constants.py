"""Constantes físicas utilizadas pelo modelo didático do PressurizaLab."""

# A aceleração gravitacional é considerada uniforme em todos os cenários.
GRAVIDADE_M_S2 = 9.81

# Constante universal dos gases na forma compatível com Pa, m³, mol e K.
CONSTANTE_GASES_J_MOL_K = 8.314462618

# Valor de referência da atmosfera padrão ao nível médio do mar.
PRESSAO_ATMOSFERICA_NIVEL_MAR_PA = 101325.0

# Densidade de referência do ar seco próxima ao nível do mar.
DENSIDADE_AR_KG_M3 = 1.225

# O líquido do recipiente é aproximado como água no modelo térmico.
DENSIDADE_AGUA_KG_M3 = 1000.0
CALOR_ESPECIFICO_AGUA_J_KG_K = 4186.0

# Densidades aproximadas para comparar a resposta de diferentes manômetros.
DENSIDADES_FLUIDOS_MANOMETRICOS = {
    "Água": 1000.0,
    "Óleo": 850.0,
    "Mercúrio": 13600.0,
}


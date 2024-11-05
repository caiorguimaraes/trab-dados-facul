import pandas as pd
import numpy as np

# Função para criar o dataframe
def criar_dataframe_diario_2024():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
             'Julho', 'Agosto', 'Setembro', 'Outubro']
    dias_no_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31]  # Janeiro a Outubro em 2024 (2024 foi ano bissexto)
    vendas_mensais = {
        'Mês': meses,
        'EH': [17884.998, 13819.429, 18425.725, 17469.373, 18304.294, 
               18291.936, 18178.344, 15978.070, 13327.475, 18055.671],
        'GC': [4560.597, 6318.705, 7019.276, 4080.925, 4205.233, 
               5434.417, 5775.765, 3537.623, 3685.394, 4914.672],
        'GA': [20937.868, 17406.978, 19379.365, 17899.655, 20855.725, 
               20430.968, 20266.685, 16972.499, 18580.801, 19793.356],
        'DS': [21647.258, 22472.734, 24803.491, 18283.419, 17428.831, 
               21680.401, 21741.689, 17050.559, 17390.484, 20262.072]
    }
    
    # Criando um DataFrame inicial com os dados mensais
    df_mensal = pd.DataFrame(vendas_mensais)

    # Expandindo para dados diários
    dados_diarios = {
        "Data": [],
        "EH": [],
        "GC": [],
        "GA": [],
        "DS": []
    }
    
    for i, mes in enumerate(df_mensal['Mês']):
        for dia in range(1, dias_no_mes[i] + 1):
            dados_diarios["Data"].append(f"2024-{i+1:02d}-{dia:02d}")  # Formato de data ano-mês-dia
            '''{i+1:02d}: i é o índice do loop que itera sobre os meses ( 0 para Janeiro, 1 para Fevereiro, etc.). i + 1 é utilizado para converter esse índice em um número de mês (1 a 10). O :02d formata o número como uma string de dois dígitos, preenchendo com zeros à esquerda se necessário. se i for 0 (Janeiro), i + 1 será 1, que será formatado como 01.
{dia:02d}: dia é o número do dia atual na iteração do loop. Novamente, :02d formata o dia para ter sempre dois dígitos, por exemplo, 1 se tornará 01'''
            fator_variação = np.random.uniform(0.9, 1.1)  # Variação de 10%
            dados_diarios["EH"].append(df_mensal["EH"][i] / dias_no_mes[i] * fator_variação)
            dados_diarios["GC"].append(df_mensal["GC"][i] / dias_no_mes[i] * fator_variação)
            dados_diarios["GA"].append(df_mensal["GA"][i] / dias_no_mes[i] * fator_variação)
            dados_diarios["DS"].append(df_mensal["DS"][i] / dias_no_mes[i] * fator_variação)

    df_diario = pd.DataFrame(dados_diarios)
    
    # Adicionando uma coluna de Total diário de vendas
    df_diario['Total'] = df_diario[['EH', 'GC', 'GA', 'DS']].sum(axis=1)

    # Calculando a variação percentual total diária
    df_diario['Variação (%) Total'] = df_diario['Total'].pct_change() * 100  # Variação percentual do total

    return df_diario

# Função para salvar o DataFrame em um arquivo Excel
def salvar_dataframe_excel(df, caminho):
    df.to_excel(caminho, index=False)

# Criando e verificando o DataFrame para o ano de 2024
df_diario_2024 = criar_dataframe_diario_2024()
print("Número de linhas e colunas no DataFrame diário de 2024:", df_diario_2024.shape)
print("Exemplo de dados no DataFrame diário de 2024:\n", df_diario_2024.head())

# Caminho para salvar o arquivo Excel
arquivo_excel = 'vendas_2024.xlsx'
salvar_dataframe_excel(df_diario_2024, arquivo_excel)
print(f"Dados salvos no arquivo: {arquivo_excel}")
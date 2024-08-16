import pandas as pd

"""
Nome: Matheus Mozart da Silva Neves Borges
linkedin: https://www.linkedin.com/in/matheus-mozart-borges
whatsapp: https://wa.me/5569993655504
email: mmsnborges@gmail.com
"""

"""
2 - Manipulação de Dados com Pandas

a) Ler o arquivo CSV com a biblioteca Pandas.
"""

print('2 - Manipulação de Dados com Pandas')
print('*******************************************************************************')
print('')
print('a) Ler o arquivo CSV com a biblioteca Pandas.')
print('')

try:
    df = pd.read_csv('medicoes_eletricas.csv')
    print(f'Leitura feita, seguem os dados:\n{df}')
except FileNotFoundError:
    print("O arquivo 'medicoes_eletricas.csv' não foi encontrado.")
    df = pd.DataFrame()

"""
b) Exibir todos os registros onde a frequência (Frequencia_Hz) esteja fora da faixa normal de operação (assuma que a faixa normal é de 59.8 a 60.2 Hz).
"""
print('')
print('*******************************************************************************')
print('b) Exibir todos os registros onde a frequência (Frequencia_Hz) esteja fora da faixa normal de operação (assuma que a faixa normal é de 59.8 a 60.2 Hz).')
print('')

if not df.empty:
    faixa_normal_min = 59.8
    faixa_normal_max = 60.2

    print(f'Faixa normal mínima de {faixa_normal_min}. Faixa normal máxima {faixa_normal_max}')

    df['Frequencia_Hz'] = pd.to_numeric(df['Frequencia_Hz'], errors='coerce')  # Garantir que os dados são numéricos

    df_fora_faixa_normal = df[(df['Frequencia_Hz'] > faixa_normal_max) | (df['Frequencia_Hz'] < faixa_normal_min)]

    if df_fora_faixa_normal.empty:
        print("Não há dados fora da faixa normal.")
    else:
        print(f'Dados fora da faixa normal:\n{df_fora_faixa_normal}')

import pandas as pd
from decimal import Decimal, getcontext


"""
Nome: Matheus Mozart da Silva Neves Borges
linkedin: https://www.linkedin.com/in/matheus-mozart-borges
whatsapp: https://wa.me/5569993655504
email: mmsnborges@gmail.com
"""

"""
3 - Criação de Função para Processamento de Dados Elétricos
Crie uma função chamada calcular_fator_potencia que receba um arquivo CSV chamado medicoes_potencia.csv e um intervalo de tempo em minutos. A função deve:
"""
getcontext().prec = 6

print('3 - Criação de Função para Processamento de Dados Elétricos')
print('*******************************************************************************')
print('')

def calcular_fator_potencia(data: str, intervalo_minutos: int) -> str:
    """ a) Ler o arquivo CSV. """
    df = pd.read_csv(data)
    
    if not {'Data', 'Potencia_W', 'Tensao_V', 'Corrente_A', 'Frequencia_Hz'}.issubset(df.columns):
        raise ValueError("O arquivo CSV deve conter as colunas 'Data', 'Potencia_W', 'Tensao_V', 'Corrente_A', 'Frequencia_Hz'")
    
    """b) Filtrar os registros dentro do intervalo de tempo fornecido."""
    df['Data'] = pd.to_datetime(df['Data'])
    data_inicio = df['Data'].min()
    data_final = data_inicio + pd.Timedelta(minutes=intervalo_minutos)
    
    df_intervalo = df[(df['Data'] >= data_inicio) & (df['Data'] <= data_final)]

    if df_intervalo.empty:
        raise ValueError("Nenhum dado encontrado no intervalo de tempo fornecido")
    """
    c) Calcular o fator de potência médio durante o período, usando a fórmula: 
    Fator de Potência = Potencia_W / (Tensao_V * Corrente_A).
    obs: Usei o decimal para por mais precisão nos cálculos.
    """ 
    df_intervalo['Fator_Potencia'] = df_intervalo.apply(
        lambda row: Decimal(row['Potencia_W']) / (Decimal(row['Tensao_V']) * Decimal(row['Corrente_A'])), axis=1
    )
    
    print('Tabela atualizada com valor de Fator de Potência dentro do intervalo:\n')
    print(df_intervalo)
    print()
   
    fator_potencia_soma = df_intervalo['Fator_Potencia'].sum()
    fator_potencia_medio = fator_potencia_soma / Decimal(len(df_intervalo))
    """
    d) Criar a função para retornar o fator de potência médio calculado para a primeira leitura do csv usando a função criada.
    Fiquei em dúvida se eu deveria criar uma função para retornar, ou esta deveria retornar.
    Então, implante a reposta nesta função. 

    """
    return f"O fator de potência médio total para a primeira leitura é {fator_potencia_medio:.6f}"


""""Chamada da função com a quantidade de tempo que quero, no caso é em minutos a partir
da primeira data.
"""
def main():
    resultado = calcular_fator_potencia('medicoes_eletricas.csv', 15)
    print(resultado)

if __name__ == '__main__':
    main()
import csv

"""
Nome: Matheus Mozart da Silva Neves Borges
linkedin: https://www.linkedin.com/in/matheus-mozart-borges
whatsapp: https://wa.me/5569993655504
email: mmsnborges@gmail.com
"""

"""
1 - Leitura e Análise de Arquivo CSV:

a) Leitura do arquivo medicoes_eletricas.csv com qualquer biblioteca:
Escolhida csv, pois a panda será usada na questão 2.
"""
print('1 - Leitura e Análise de Arquivo CSV:')
print('*******************************************************************************')
print('')
print('a) Leitura do arquivo medicoes_eletricas.csv com qualquer biblioteca:')
print('Resposta: Feita com a biblioteca csv')
print('')
try:
    with open('medicoes_eletricas.csv') as data:
        csv_data = csv.reader(data)
        """
        1 - Leitura e Análise de Arquivo CSV:
        b) Exibir as 5 primeiras linhas do arquivo: .
        """
        print('*******************************************************************************')
        print('b) Exibir as 5 primeiras linhas do arquivo: ')    
        for i, row in enumerate(csv_data):
            if i < 5:
                print(f' {i + 1}ª Linha --> {row}')
            else:
                break
except FileNotFoundError:
    print("O arquivo 'medicoes_eletricas.csv' não foi encontrado.")

"""
1 - Leitura e Análise de Arquivo CSV:
c) Calcular e exibir a média da potência (Potencia_W) durante o período registrado no CSV.
"""
print('*******************************************************************************')
print('c) Calcular e exibir a média da potência (Potencia_W) durante o período registrado no CSV.')
print('')
try:
    with open('medicoes_eletricas.csv') as data:
        csv_data = csv.DictReader(data)
        valor = 0
        count = 0
        for row_data in csv_data:
            try:
                valor += float(row_data['Potencia_W'])
                count += 1
            except ValueError:
                print(f"Valor inválido encontrado para 'Potencia_W': {row_data['Potencia_W']}")
        
        if count > 0:
            media = valor / count
            print(f'A média da Potencia_W é: {media:.2f}')
        else:
            print("Nenhum dado disponível para calcular a média.")
except FileNotFoundError:
    print("O arquivo 'medicoes_eletricas.csv' não foi encontrado.")

"""
1 - Leitura e Análise de Arquivo CSV:
d) Identificar e exibir o valor máximo de tensão (Tensao_V) registrado e em que data ocorreu.
"""
print('*******************************************************************************')
print('d) Identificar e exibir o valor máximo de tensão (Tensao_V) registrado e em que data ocorreu.')
print('')
valor_maximo = float('-inf')      
data_valor_maximo_tensao_v = ''

try:
    with open('medicoes_eletricas.csv') as data:
        csv_data = csv.DictReader(data)
        for row_data in csv_data:
            try:
                valor_tensao_v = int(row_data['Tensao_V'])
                if valor_tensao_v > valor_maximo:          
                    valor_maximo = valor_tensao_v  
                    data_valor_maximo_tensao_v = row_data['Data']
            except ValueError:
                print(f"Valor inválido encontrado para 'Tensao_V': {row_data['Tensao_V']}")
            except KeyError:
                print("Coluna 'Tensao_V' não encontrada no arquivo CSV.")
    
    if valor_maximo != float('-inf'):
        print(f"Valor máximo da tensão_v é {valor_maximo} e ocorreu no dia {data_valor_maximo_tensao_v}")
    else:
        print("Nenhum valor válido de tensão encontrado.")
except FileNotFoundError:
    print("O arquivo 'medicoes_eletricas.csv' não foi encontrado.")

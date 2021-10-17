## Consolidando arquivos
import os
import pandas as pd
pasta = 'C:/Users/AlexA/OneDrive/Área de Trabalho/Filiais 2'
df = pd.DataFrame()
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        endereco = os.path.join(diretorio, arquivo)
        dados = pd.read_excel(endereco)
        df = df.append(dados)
df.to_excel('C:/Users/AlexA/OneDrive/Área de Trabalho/Filiais 2/Teste.xlsx', index= False)
print("Concluido")

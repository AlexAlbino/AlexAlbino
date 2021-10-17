## Consolidando arquivos
import os
import pandas as pd
pasta = 'endereço do diretório'
df = pd.DataFrame()
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        endereco = os.path.join(diretorio, arquivo)
        dados = pd.read_excel(endereco)
        df = df.append(dados)
df.to_excel('caminho onde deseja salvar o novo arquivo' & /nome_arquivo.xlsx', index= False)
print("Concluido")

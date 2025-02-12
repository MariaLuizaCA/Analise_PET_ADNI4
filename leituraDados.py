# LINKS PARA SE BASEAR: 
# https://docs.python.org/3/library/os.html#os.walk (biblioteca)
# https://www.kaggle.com/code/rude009/working-with-dicom-data  (DICOM)
# pip install pydicom

import os #biblioteca para manipular arquivos e diretórios
import pydicom 
import pandas as pd

caminhoADMI4 = r"C:\Users\Maria Luíza\Documents\GitHub\Analise_PET_ADNI4\Exames de diagnóstico_dataset" 
# o 'r' é para raw code, já que o \ serve para os caracteres especiais no string, isso evita que ele interprete como Unicode
caminhoArquivoDcm = r"C:\Users\Maria Luíza\Documents\GitHub\Analise_PET_ADNI4\Exames de diagnóstico_dataset\ADNI\941_S_6575\PET_Brain_DYNAMIC_4X5MIN\2024-11-27_15_30_39.0\I11067772\ADNI_941_S_6575_PT_PET_Brain_DYNAMIC_4X5MIN_br_raw_20241204190854236_35.dcm"

# temos que fazer percorrer por todas as subpastas(os.walk). 
# root é a pasta atual. 
# dirs lista de subpastas da pasta atual. 
# files lista de arquivos da pasta atual

dados_selecionados = []

#como acessar as pastas como se fosse uma árvore de diretórios 
for root, dirs, files in os.walk(caminhoADMI4):
    for file in files:
        if file.endswith(".dcm"):
            caminho = os.path.join(root, file)
            ds = pydicom.dcmread(caminho) #acessar os arquivos DICOM e ds retorna TODOS os metadados
            #teste de organização de dados
            dados = {
                "Paciente" : getattr(ds, "PatientName", "Desconhecido"),
                "ID" : getattr(ds, "PatientID", "Desconhecido"),
                "Data do exame" : getattr(ds, "StudyDate", "Desconhecido"),
                "Modalidade" : getattr(ds, "Modality", "Desconhecido")
            }
            dados_selecionados.append(dados)
df = pd.DataFrame(dados_selecionados)
print(df)
df.to_csv("dados_exames.csv", index = False)
#preciso analisar dados para entender se a saida está certa

    #caminho = [file for file in files if file.endswith(".dcm")] #filtra apenas os arquivos q eu preciso analisar (DICOM)
    #print(f"Pasta: {root}") #teste para mostrar o funcionamento
    #for file in files[:5]: #percorrer os arquivos da pasta atual (só mostrar 5 pq são muitos)
        #print (f" - {file}")
    #print("-"*40) #separa os resultados




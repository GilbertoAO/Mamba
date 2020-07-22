import csv
import os

unidades = list()
cafs = list()
descr = list()
skus = list()
pesos_desenhos = list()
pesos_reais = list()
caminho = os.path.dirname(os.path.dirname(__file__)) + '/data'
arquivo = os.path.join(caminho, 'Monitoramento_resumo.csv')

with open(arquivo, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =';')
    next(csv_reader)
    for line in csv_reader:
        #unidades;cafs;Descrição;PRODUTO;Peso Desenho;Peso Real
        unidades.append(line[0])
        cafs.append(line[1])
        descr.append(line[2])
        skus.append(line[3])
        pesos_desenhos.append(line[4].replace(',','.'))
        pesos_reais.append(line[5].replace(',','.'))




def get_unidade(i):
    return unidades[i]

def get_caf(i):
    return cafs[i]

def get_descr(i):
    return descr[i]


def get_sku(i):
    return skus[i]

def get_peso_desenho(i):
    return pesos_desenhos[i]

def get_peso_real(i):
    return pesos_reais[i]

def get_tamanho():
    return len(unidades)


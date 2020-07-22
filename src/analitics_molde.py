from csv_to_python import *
from modelo_moldes import * 


def setup():
    produtos = list()
    for i in range(get_tamanho()):
        produtos.append(Produto(get_sku(i), get_caf(i), get_peso_real(i), get_peso_desenho(i), get_descr(i)))
    return produtos


def lista_sobrepeso(produtos):
    indices_fora = list()
    print("#### Lista com os produtos que estão com pesos acima de 5% ####")
    print("  SKU  -  CAF - P. Desenho - P. Real - Dif - Diferença em %")

    i=0
    cont = 0 
    for produto in produtos:
        i+=1
        if produto.passou_do_limite:
            indices_fora.append(i)
            print(f'{produto.sku}, {produto.caf}, {produto.peso_desenho}, {produto.peso_real}, {produto.sobrepeso: .3f}, {produto.porcentos_fora: .3f}%')
        cont+=1


def busca_por_caf(produtos, caf):
    for produto in produtos:
        if produtos.caf == caf:
            return produto
    return False

def busca_por_sku(produtos, sku):
    for produto in produtos:
        if produto.sku == sku:
            return produto
    return False









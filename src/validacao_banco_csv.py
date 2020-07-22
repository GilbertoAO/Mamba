#script para validar as descrições contidas no banco com as descrições contidas na planilha.
#O objetivo do script é ser executado uma vez, e mostrar as diferenças entre as descrições. Se as descrições forem iguais na comparação bruta "==" ela não precisa ser analisar

#Script rodado uma vez, analise dos resultados foi feita e é possível concluir que os dados  do csv são iguais aos do bd. 


import mysql.connector
from setup_bd import *
from csv_to_python import *
from analitics_molde import *

cnx = mysql.connector.connect(host= host(),
                                port= port(),
                                user= user(),
                                password= password(),
                                database= database()
                                
                             )

dbcursor = cnx.cursor()

dbcursor.execute(f"select codigo, descricao from prod_roteiro")

dbresultado = dbcursor.fetchall()

produtos = setup()

for linha in dbresultado:
    db_sku = str(linha[0])
    db_descr = linha[1]
    produto = busca_por_sku(produtos, db_sku)
    if produto:
        if len(produto.descricao)>len(db_descr):
            tamanho = len(db_descr)
            if not produto.descricao[:tamanho] == db_descr:
                print('csv>db')
                print(f"csv: {produto.descricao} - db: {db_descr}")
        elif len(produto.descricao)<len(db_descr):
            tamanho = len(produto.descricao)
            if not produto.descricao == db_descr[:tamanho]:
                print('db>csv')
                print(f"csv: {produto.descricao} - db: {db_descr}")
        else:
            
            if not produto.descricao == db_descr:
                print('db = csv')
                print(f"csv: {produto.descricao} - db: {db_descr}")
                


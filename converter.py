import pandas as pd

exemplo = """V (V)&  I (mA)& m (cm) &R ($\Omega$)\\ \hline 
         0,473&  159,8&  29,5    
&2,959"""

def table2list(table:str):
    lista = []
    objeto = ""
    register = True
    first_step = True
    for i in table:
        if i.isdigit():
            register = True

        if register:
            if i == "&":
                lista.append(objeto.replace("\n",""))
                objeto = ""
            else:
                if i == " ":
                    continue
                else:
                    objeto += i
            if "\\\\" in objeto:
                lista.append(objeto.replace("\\\\",""))
                objeto = ""
                if first_step == True:
                    num_colunas = len(lista)
                    first_step = False
                register = False

    if objeto != "":
        lista.append(objeto)
    return lista,num_colunas

def table2Dataframe(table:str):
    lista,num_colunas = table2list(table)
    nome_colunas = lista[:num_colunas]
    elem_colunas = [float(i.replace(",",".")) for i in lista[num_colunas:]]
    colunas = [[] for i in range(num_colunas)]
    for i in range(num_colunas):
        multiplo = 0
        while True:
            try:
                colunas[i].append(elem_colunas[i + num_colunas * multiplo])
                multiplo +=1
            except:
                break

    return pd.DataFrame({i: j for i,j in zip(nome_colunas,colunas)})
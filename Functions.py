import numpy as np
def clean_float(texto):
    texto = str(texto)
    texto = texto.replace('R$', ' ')
    texto = texto.replace(',', '.')
    texto = texto.strip()
    texto = float(texto)
    return texto

def clean_competition(texto):
    texto = str(texto)
    texto = texto.replace(".com.br", " ")
    texto = texto.replace(".com", " ")
    texto = texto.replace("ô", "o")
    texto = texto.replace("ê", "e")
    texto = texto.strip()
    texto = texto.lower()

    return texto


def data_cleaning(table):
    table['Codigo'].dropna(inplace=True)
    table = table.fillna(0)
    table['Codigo'] = table['Codigo'].astype(str)


    # filling the nan's with the price of the products that have prices and are the same product that the one that have the nan only dfferent because of the color
    for i in range(len(table)):
        if i > 0 and table['Codigo'][i]:
            if table['Codigo'][i][:-1] == table['Codigo'][i - 1][:-1]:
                if table['Preco Concorrencia'][i] == 0:
                    table['Preco Concorrencia'][i] = table['Preco Concorrencia'][i - 1]
                if table['Preco Concorrencia'][i - 1] == 0:
                    table['Preco Concorrencia'][i - 1] = table['Preco Concorrencia'][i]
                if table['Concorrencia'][i] == 0:
                    table['Concorrencia'][i] = table['Concorrencia'][i - 1]
                if table['Concorrencia'][i - 1] == 0:
                    table['Concorrencia'][i - 1] = table['Concorrencia'][i]
    for i in range(len(table)):
        if i < 464:
            if table['Codigo'][i][:-1] == table['Codigo'][i + 1][:-1]:
                if table['Preco Concorrencia'][i] == 0:
                    table['Preco Concorrencia'][i] = table['Preco Concorrencia'][i + 1]
                if table['Preco Concorrencia'][i + 1] == 0:
                    table['Preco Concorrencia'][i + 1] = table['Preco Concorrencia'][i]
                if table['Concorrencia'][i] == 0:
                    table['Concorrencia'][i] = table['Concorrencia'][i + 1]
                if table['Concorrencia'][i + 1] == 0:
                    table['Concorrencia'][i + 1] = table['Concorrencia'][i]
    for i in range(len(table)):
        if table['Preco Concorrencia'][i] == 0:
            table['Preco Concorrencia'][i] = table['P.Venda'][i]
        if table['Concorrencia'][i] == 0:
            table['Concorrencia'][i] = 'Inexistente'
    return table

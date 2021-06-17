import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import schedule
import time
import pywhatkit
import matplotlib.pyplot as plt
import csv

now = datetime.now()
ano = int(now.strftime('%y'))
mes = int(now.strftime('%m'))
dia = int(now.strftime('%d'))
hora = int(now.strftime('%H'))
minutos = int(now.strftime('%M'))
Horario = float(f'{hora}.{minutos}')
key = 'GKA00KD2N9MQAZSJ'

ts =TimeSeries(key, output_format='pandas')

def price__():
    contador = 0
    dicionario = {

    }
    p = pd.read_csv('B:\Arquivos+csv\data.csv')
    Data_ = open('B:\Arquivos+csv\data.csv')
    c = sum(1 for line in Data_)
    while contador < c-1:
        conversão = f'{p.iloc[contador, 0]}.SA'
        data, meta = ts.get_daily(conversão)
        ultimo_preço = float(data.iloc[0, 3]) 
        dicionario[f'{p.iloc[contador, 0]}'] = ultimo_preço
        contador += 1
    return (dicionario)

def price_2(ticker):
    data, meta = ts.get_daily(ticker)
    ultimo_preço = float(data.iloc[0, 3]) 
    return ultimo_preço

def send_message():
    contador2 = 0
    timer = 0
    Data_2 = open('B:\Arquivos+csv\ telefone.csv')
    d = sum(1 for line in Data_2)
    l = pd.read_csv('B:\Arquivos+csv\ telefone.csv')
    while contador2 < d-1:
        conversão2 = str(f'+{l.iloc[contador2, 0]}')
        pywhatkit.sendwhatmsg(conversão2, f'O preço das suas ações são: \n{price__()}\n{hora}:{minutos} -> {dia}/{mes}/{ano}', hora, minutos+1+timer, 10)
        contador2 += 1
        timer += 1
        time.sleep(5)

def introdução():
    print('1 - Se quer adicionar uma ação a sua carteira')
    print('2 - Se quer trocar de telefone')
    print('3 - Se quer adicionar um telefone')
    print('4 - Se quer fechar o programa')
    x = int(input('?: '))
    while x != 1 and x != 2 and x != 3 and x != 4:
        print('Colque um número válido!\n') 
        print('1 - Se quer adicionar uma ação a sua carteira')
        print('2 - Se quer trocar de telefone')
        print('3 - Se quer adicionar um telefone')
        print('4 - Se quer fechar o programa')
        x = int(input('?: '))

    if x == 1:
        m = (input('Qual ticker você quer adicionar? (Coloque o ticker correto, se não erros poderão aparecer no futuro): ')).upper()
        ticker1 = str(f'{m}.SA')
        tabela = [[m, f'{dia}/{mes}/{ano}', price_2(ticker1)]]
        Data_ = open('B:\Arquivos+csv\data.csv', 'a')
        escritor = csv.writer(Data_, lineterminator='\n')
        escritor.writerows(tabela)
        Data_.close()

    elif x == 2:
        contador3 = 0
        g = str(input('Qual telefone você quer trocar? (Coloque como no exemplo: (country_code)(DDD)(digitos)'))
        Data_3 = pd.read_csv('B:\Arquivos+csv\ telefone.csv')
        Data_2 = open('B:\Arquivos+csv\ telefone.csv', 'r')
        n = str(input('Qual seu telefone? (Coloque como no exemplo: (country_code)(DDD)(digitos)'))
        d = sum(1 for line in Data_2)
        while contador3 < d-1:
            o = str(Data_3.iloc[contador3, 0])
            if o == g:
                Data_3.at[1, 'Telefone'] = f'{n}'
                print(Data_3)
                Data_3.to_csv('B:\Arquivos+csv\ telefone.csv', index=False)
            contador3 += 1

    elif x == 3:
        n = str(input('Qual seu telefone? (Coloque como no exemplo: +(country_code)(DDD)(digitos)'))
        tabela = [[n]]
        Data_ = open('B:\Arquivos+csv\ telefone.csv', 'a')
        escritor = csv.writer(Data_, lineterminator='\n')
        escritor.writerows(tabela)
        Data_.close() 

introdução()

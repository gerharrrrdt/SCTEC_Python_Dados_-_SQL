# ATIVIDADE EM ANDAMENTO

# Importação das bibliotecas necessárias para o projeto
import csv
import os
from datetime import date, datetime, timedelta

# Criação de variáveis para declarar o nome do arquivo criado, os campos dentro do arquivo
#   e definindo a duração total da jornada de trabalho como 8h
ARQUIVO_CSV = "cadastro_matriculas.csv"
CAMPOS = ["matricula", "nome", "data", "entrada", "saida_almoco", "retorno_almoco", "saida"]
JORNADA_PADRAO = timedelta(hours=8)

CREDENCIAIS = {
    "001": {"nome": "Aline", "senha": "123"},
    "002": {"nome": "Beatriz", "senha": "123"},
    "004": {"nome": "Cristiano", "senha": "123"},
    "005": {"nome": "Denis", "senha": "123"},
}

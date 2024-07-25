#exercicios
# 1 - crie um formulario em html para cadastro de livros - ok feito aula 24

# 2 -  
import pandas as pd
caminho_arquivo = r"C:\Users\Aluno\Downloads\tabela livros.csv"
df = pd.read_csv(caminho_arquivo)
#print(df)

# exercicio 3

import csv

class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo

livro0 = Livro(" O burrinho pedres1", "guimaraes rosa", "ficção", 1946, "sim")
livro1 = Livro(" O burrinho pedres2", "guimaraes rosa", "ficção", 1946, "sim")
livro2 = Livro(" O burrinho pedres3", "guimaraes rosa", "ficção", 1946, "sim")
livro3 = Livro(" O burrinho pedres4", "guimaraes rosa", "ficção", 1946, "sim")

lista_de_livros = [livro0, livro1, livro2, livro3]

for livro in lista_de_livros:

    print(f"Livro: {livro.titulo}, Autor: {livro.autor}, Categoria: {livro.categoria}, Ano: {livro.ano}, Ativo: {livro.ativo}")

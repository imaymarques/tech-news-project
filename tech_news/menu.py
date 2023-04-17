import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories

OPTIONS = {
    "0": "Digite quantas notícias serão buscadas:",
    "1": "Digite o título:",
    "2": "Digite a data no formato aaaa-mm-dd:",
    "3": "Digite a categoria:",
    "5": "Encerrando script\n",
}


def get_methods(value):
    if value == "0":
        amount = input(OPTIONS[value])
        return get_tech_news(int(amount))
    if value == "1":
        title = input(OPTIONS[value])
        return search_by_title(title)
    if value == "2":
        date = input(OPTIONS[value])
        return search_by_date(date)
    if value == "3":
        category = input(OPTIONS[value])
        return search_by_category(category)


# Requisitos 11 e 12
def analyzer_menu():
    options = ["0", "1", "2", "3", "4", "5"]
    while True:
        value = input("""Selecione uma das opções a seguir:
            0 - Popular o banco com notícias;
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por categoria;
            4 - Listar top 5 categorias;
            5 - Sair.""")
        if value not in options:
            sys.stderr.write("Opção inválida\n")
        elif value == "4":
            top_5_categories()
        else:
            result = get_methods(value)
            if result:
                print(result)

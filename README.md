# simple-web-scrapping

# 📚 Books to Scrape - Coleta e Visualização de Categorias

Este projeto realiza **web scraping** no site [Books to Scrape](https://books.toscrape.com/), extraindo as categorias de livros e a quantidade de títulos em cada uma delas.  
Os dados são organizados em um **DataFrame Pandas** e visualizados em um **gráfico de barras** mostrando as 10 maiores categorias.

---

##  Funcionalidades
- Extração automática das categorias de livros do site.
- Coleta da quantidade total de livros em cada categoria.
- Organização em **DataFrame** para fácil manipulação.
- Visualização das 10 categorias com mais livros por meio de um gráfico de barras.

---

##  Tecnologias Utilizadas
- **Python 3**
- [Requests](https://pypi.org/project/requests/) → Requisições HTTP.
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) → Extração e parsing do HTML.
- [Pandas](https://pypi.org/project/pandas/) → Organização dos dados.
- [Matplotlib](https://pypi.org/project/matplotlib/) → Geração do gráfico.

---
##  Exemplo de Saída

**Tabela gerada:**
| Categoria           | Quantidade |
|---------------------|------------|
| Travel              | 11         |
| Mystery             | 30         |
| Historical Fiction  | 20         |
| Sequential Art      | 77         |
| Classics            | 19         |
| Philosophy          | 7          |
| Romance             | 22         |
| Womens Fiction      | 13         |
| Fiction             | 68         |
| Childrens           | 20         |

<img width="417" height="390" alt="image" src="https://github.com/user-attachments/assets/7d683910-7502-45c7-b66f-e14bf99f43ba" />

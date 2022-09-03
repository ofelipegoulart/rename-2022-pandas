
# Painel RENAME 2022 [Scrapping]

Esse repositório contém todos os arquivos os quais foram utilizados para obter os dados do arquivo PDF onde está a Relação dos Medicamentos Essenciais 2022, lista divulgada anualmente pelo Ministério da Saúde
que inclui os medicamentos e insumos hospitalares disponibilizados pela rede pública de saúde em todo território nacional.

## Ferramentas Utilizadas

Apesar dos scripts do repositório estarem em Python, a obtenção dos dados se deu pelo [Tabula](https://tabula.technology/), software responsável por extrair dados de tabelas de arquivos em formato pdf. Depois da extração, os dados foram tratados pelos algoritmos em Python pela biblioteca Pandas.

## Implementações Futuras

O final do projeto se dará pela criação do script - também em Python - que transforma o arquivo resultado pelo programa de tratamento dos dados em um arquivo SQL, que será aproveitadoo pelo Painel RENAME 2022 a fim de realizar as consultas sobre os insumos e medicamentos.

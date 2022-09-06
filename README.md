
# Painel RENAME 2022 [Scrapping]

Esse repositório contém todos os arquivos os quais foram utilizados para obter os dados do arquivo PDF onde está a Relação dos Medicamentos Essenciais 2022, lista divulgada anualmente pelo Ministério da Saúde
que inclui os medicamentos e insumos hospitalares disponibilizados pela rede pública de saúde em todo território nacional.

## Ferramentas Utilizadas

Apesar dos scripts do repositório estarem em Python, a obtenção dos dados se deu pelo [Tabula](https://tabula.technology/), software responsável por extrair dados de tabelas de arquivos em formato pdf. Depois da extração, os dados foram tratados pelos algoritmos em Python pela biblioteca Pandas. Em seguida, com a planilha CSV criada, um outro script foi implementado com o objetivo de inserir os dados da planilha dentro de um banco de dados, para que se possa posteriormente trabalhar as informações dentro da nossa aplicação web.

## Finalização do Projeto

O repositório foi finalizado após o deploy do banco de dados em uma instância de banco de dados da AWS (RDS).

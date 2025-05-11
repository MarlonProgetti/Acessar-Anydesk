# Acessar Anydesk

## 📖 Descrição

**Acessar Anydesk** é um aplicativo em Python com interface gráfica que permite acessar remotamente computadores de pontos de venda (PDVs) usando o AnyDesk.  
Através de uma planilha do Excel contendo os IDs de cada PDV, o usuário pode buscar rapidamente um posto, selecionar o PDV desejado e iniciar a conexão com apenas um clique.

## 🚀 Funcionalidades

- Interface amigável com Tkinter
- Leitura automatizada de dados em Excel com pandas
- Execução automática do AnyDesk com subprocess
- Digitação de senha automatizada (opcional, via pyautogui)
- Verificações de erros para entrada inválida

## 📦 Requisitos

- Python 3.x
- Biblioteca `pandas`
- Biblioteca `pyautogui`
- Biblioteca `tkinter` (já vem com Python)
- Planilha Excel com os dados de acesso (nome do posto + colunas para PDV)

- ## 🛠 Instalação

Clone este repositório e instale as dependências com:

- ```bash
- pip install pandas pyautogui

## 📁 Estrutura esperada do Excel

- A planilha deve conter uma coluna NOME DO POSTO e colunas com os nomes dos PDVs, como PDV1, PDV2, etc.

- Exemplo:

  NOME DO POSTO      	PDV1	        PDV2
  NOMEDOPOSTO        	123456789	    987654321

## ▶️ Como usar
  
-  Execute o programa:
-  python acessar_anydesk.py
-  Preencha os campos com o nome do posto e o número do PDV desejado.
-  O programa abrirá o AnyDesk com o código correspondente automaticamente.

## ⚠️ Observações

-  O caminho para o executável do AnyDesk pode variar. Certifique-se de ajustar no código se necessário.
-  Certifique-se de que a planilha Excel esteja atualizada e com os nomes corretos dos postos e PDVs.

## 🧑‍💻 Autor

-  Desenvolvido por Marlon Progetti.

# Projeto de Análise de Sentimentos em Português com FastAPI e LeIA

## Descrição

Este projeto oferece uma API REST para análise de sentimentos em textos curtos em português, utilizando a biblioteca LeIA (Léxico para Inferência Adaptada), que é um fork do VADER adaptado para o português brasileiro. A API é construída com FastAPI e inclui validação para limitar a entrada a no máximo 280 caracteres.

Um cliente Python interativo acompanha o projeto, permitindo enviar textos dinamicamente para análise. Essa solução é 100% local, gratuita, rápida e fácil de usar.

## Funcionalidades

- Endpoint `/sentiment` que recebe texto (max 280 caracteres) e retorna as pontuações de sentimento: positivo, negativo, neutro e composto.
- Validação de entrada com mensagens de erro claras.
- Cliente interativo para testes no terminal.
- Compatibilidade total com textos em português, incluindo suporte para emojis e linguagem coloquial.

## Estrutura do Projeto

```
meu_projeto_api/
├── README.md
├── requirements.txt
├── server/
│   └── app/
│       ├── __init__.py
│       └── main.py
└── client/
    └── main.py
```

## Pré-requisitos

- Python 3.10 ou superior
- Ambiente virtual recomendado

## Instalação

1. Clone o repositório

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ou
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando o projeto

### Iniciar o servidor

```bash
uvicorn server.app.main:app --reload
```

O servidor ficará disponível em `http://127.0.0.1:8000`.

### Usar o cliente interativo

Em outro terminal, execute:

```bash
python client/main.py
```

Digite frases em português (máximo 280 caracteres) para receber as análises de sentimento. Digite `sair` para encerrar.

## Exemplo de resposta da API

```json
{
  "scores": {
    "neg": 0.2,
    "neu": 0.6,
    "pos": 0.2,
    "compound": 0.3
  }
}
```

## Sobre a LeIA

LeIA é um coletor léxico de polaridade treinado para português, baseado no VADER, que entende nuances da língua portuguesa, inclusive emojis e expressões comuns.

Mais informações: [LeIA no PyPI](https://pypi.org/project/leia-br/)

## Considerações Finais

Este projeto é ideal para aplicações que precisam de análise de sentimentos rápida, local e em português, sem dependências de APIs externas.

Projeto baseado no modelo VADER em pt-BR, feito pelo autor: [LeIA](https://github.com/rafjaa/LeIA)

***

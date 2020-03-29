# Desafio TECH GS

Projeto simples, de demonstração de conhecimento

## Getting Started

A execução é muito fácil, basta apenas efetuar o build do docker e rodar a imagem!


### Prerequisites

Docker > version 18.09.9-ce

### Installing

Execute o comando em uma máquina com Docker instalado:

```
docker build -t desafio-tech .
```

Lembrando que é necessário estar na pasta raiz do projeto no terminal.

## Running a application

Para executar o programa e todos os métodos, basta:

```
docker run desafio-tech
```

Os paramos podem ser alterados em:

```
fundo_zarathustra.rentabilidade_periodo('2019-01-02', '2019-01-31')
```

Ou seja, data_inicio e data_fim

## Running the tests

Para executar os testes, basta:

```
docker run desafio-tech /bin/bash -c "./test.sh"
```

## Authors

* **Gustavo A. Ronconi**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
# G45_Programacao_dinamica_PA-26.1

## Selos Mínimos – Combinação Ótima com Programação Dinâmica

**Número da Lista**: 45<br>
**Conteúdo da Disciplina**: Programação Dinâmica<br>

## Alunos

| Matrícula | Aluno |
| -- | -- |
| 20/2016909 | Marcelo Adrian Ribeiro de Araujo |
| 24/2015924 | Maria Eduarda de Jezus Guimarães |

## Sobre

Este projeto resolve o problema da **quantidade mínima de selos** necessária para totalizar um valor exato, utilizando **programação dinâmica**. Dado um valor inteiro (em centavos) e uma lista de denominações de selos disponíveis, o algoritmo calcula a menor combinação possível de selos para atingir aquele valor.

A abordagem clássica de DP (Coin Change) constrói uma tabela `dp` de tamanho `valor+1`, onde `dp[i]` armazena o menor número de selos para formar o montante `i`. A solução é reconstruída a partir das escolhas registradas durante o preenchimento.

O projeto conta com uma **interface web** desenvolvida em Flask que expõe uma API e serve o frontend interativo. O usuário informa o valor a selar e as denominações disponíveis e recebe, de forma clara e com visual temático, a quantidade mínima de selos e a combinação exata utilizada.

## Screenshots

<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;align-items:flex-start;">
  <!-- Adicione capturas de tela aqui, se disponíveis -->
  <!-- <img src="Frontend/screenshots/print1.png" alt="Tela principal" style="width:48%;max-width:600px"> -->
  <!-- <img src="Frontend/screenshots/print2.png" alt="Resultado" style="width:48%;max-width:600px"> -->
</div>

*Ainda não adicionado.*

## Instalação

**Linguagem**: Python 3<br>
**Framework**: Flask<br>

### Pré-requisitos

- Python 3 instalado.
- Estar na pasta `Frontend/` do projeto.
- Instalar o Flask (e quaisquer outras dependências, embora apenas Flask seja necessário).

### Comando para executar

1. Acesse o diretório do frontend:

```bash
cd Frontend
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale o Flask:

```bash
pip install flask
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000
```

## Uso

### Interface Web

Abra `http://127.0.0.1:5000/` no navegador.

Preencha o campo **Valor a selar (centavos)** com o valor desejado (ex: 150).

Preencha o campo **Selos disponíveis (centavos)** com as denominações separadas por vírgula (ex: 10, 20, 50).

Clique em **Calcular Combinação Mínima**.

O resultado exibirá:

- A quantidade mínima de selos necessária.
- A lista de selos que compõem a solução (cada um representado em centavos).

Em caso de erro ou impossibilidade de formar o valor, uma mensagem explicativa será mostrada.

### Modo API

A aplicação também expõe um endpoint HTTP para consumo externo:

```http
GET /api/solve?valor=150&denominacoes=10,20,50
```

Retorna um JSON com a mesma estrutura da função `resolver_selos`:

```json
{
  "possivel": true,
  "minimo": 3,
  "combinacao": [50, 50, 50],
  "denominacoes": [10, 20, 50],
  "erro": null
}
```

## Vídeo de Apresentação

Ainda não adicionado.

## Outros

- A lógica de programação dinâmica está isolada no arquivo `Backend/solver.py`, dentro da função `resolver_selos`.
- O frontend consome a API via JavaScript assíncrono (`fetch`) e segue o mesmo padrão de outros projetos da dupla.
- O design utiliza uma paleta de cores inspirada em tons de ciano e rosa, garantindo legibilidade e contraste adequados.
- Não há dependência de datasets externos; toda a entrada é fornecida pelo usuário.
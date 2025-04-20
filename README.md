# 💰 Simulador de Depósitos Sequenciais

Este é um programa simples em Python feito para ajudar no planejamento de metas de economia baseadas em desafios de depósitos progressivos, como o famoso "Desafio dos 100 Depósitos", "300 Depósitos", "500 Depósitos", entre outros.

## 🧠 Motivação

A ideia surgiu após ver um desafio de economia no TikTok, onde cada número de uma tabela representa o valor de um depósito. Por exemplo: depósito 1 = R$1, depósito 2 = R$2, ..., depósito 300 = R$300, totalizando um valor considerável ao final do desafio.

Fazer esses cálculos manualmente na calculadora pode ser trabalhoso, principalmente quando há a necessidade de excluir valores específicos ou simular o quanto seria possível economizar com um valor disponível. Por isso, este script facilita esse processo.

## ⚙️ Funcionalidades

- **Modo 1**: Calcular o total de depósitos entre dois valores definidos.
- **Modo 2**: Informar um valor total disponível e ver até qual depósito ele cobre.
- **Exclusões**: É possível excluir valores específicos da contagem (ex: pular depósitos de R$10, R$20 etc).

## ▶️ Como usar

1. Execute o script `deposito_calculadora.py`
2. Escolha uma das opções:
   - `1` para calcular o valor total entre dois depósitos
   - `2` para simular até onde seu dinheiro cobre os depósitos sequenciais
3. Informe os valores conforme solicitado
4. Veja o resultado direto no terminal

## 📝 Exemplo de uso

```text
Informe o valor do primeiro depósito: R$ 1
Informe o valor do último depósito: R$ 300
Deseja excluir algum valor? 10,20,30

Total acumulado entre R$ 1 e R$ 300: R$ 44.715,00
Depósitos considerados: [1, 2, 3, ..., 9, 11, ..., 299]

## 📎 Planilha do Desafio

Para acompanhar visualmente o progresso do desafio, você pode baixar ou visualizar a planilha oficial em PDF:

📄 [Clique aqui para acessar o arquivo PDF no repositório](desafio-300-depositos.pdf)

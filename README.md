# **Sistema de Gerenciamento de Pedidos**

## **Descrição**

Este projeto implementa um sistema de gerenciamento de pedidos que simula o fluxo de pedidos de clientes, incluindo o cálculo de totais, notificações, pagamentos e atualizações de status.

---

## **Funcionalidades**

- **Cadastro de Clientes e Itens**: Gerencia informações de clientes e produtos.

- **Gerenciamento de Pedidos**: Suporte para pedidos de entrega e retirada.

- **Sistema de Pagamento**: Simulação do processamento de pagamentos.

- **Notificações**: Envio de notificações por e-mail e SMS.

- **Atualização de Status**: Rastreamento e notificação do status do pedido.

---

## **Tecnologias Utilizadas**

- **Python 3.10+**

- Padrões de Projeto: _Factory Method, Template, Strategy, Facade, Observer_.

- Princípios **SOLID**.

---

## **Estrutura do Projeto**

```

.
├── cliente.py
├──item.py
├── main.py
├── notificação/
│ ├── notificacao.py
│ ├── notificacao_email.py
│ ├── notificação_sms.py
│ └── notificacao_facade.py
├── observador/
│ └── coletor_status.py
├── pagamento/
│ ├── pagamento.py
│ ├── pagamento_cartao.py
│ └── pagamento_pix.py
├── pedido/
│ ├── pedido.py
│ ├── pedido_delivery.py
│ └── pedido_retirada.py
└── README.md
```

---

## **Como executar**

1. Acesse o arquivo `main.py`.

2. Execute o programa:
```bash
python main.py
```

---

## **Exemplos de uso**

- **Cadastrar cliente e itens**:
Crie um cliente e adicione itens ao pedido.

- **Criar pedido**:
Escolha entre _entrega_ ou _retirada_.

- **Efetuar pagamento**:
Simule pagamentos via Pix ou cartão.

- **Receber notificações**:
Os clientes recebem notificações sobre o status do pedido.

---

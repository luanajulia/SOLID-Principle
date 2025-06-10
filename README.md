# **Order Management System**

## **Description**

This project implements an order management system that simulates a flow of customer orders, including calculation of totals, notifications, payment and status updates.

---

## **Features**

- **Customer and Item Registration**: Manages customer and product information.
- **Order Management**: Support for delivery and pick-up orders.
- **Payment System**: Simulation of payment processing.
- **Notifications**: Sending notifications by email and SMS.
- **Status Update**: Tracking and notification of order status.
---

## **Technologies Used**

- **Python 3.10+**
- Design Patterns: _Factory Method, Template, Strategy, Facade, Observer_.
- **SOLID** Principles.

---

## **Project Structure**

```
.
├── cliente.py
├── item.py
├── main.py
├── notificacao/
│   ├── notificacao.py
│   ├── notificacao_email.py
│   ├── notificacao_sms.py
│   └── notificacao_facade.py
├── observador/
│   └── observador_status.py
├── pagamento/
│   ├── pagamento.py
│   ├── pagamento_cartao.py
│   └── pagamento_pix.py
├── pedido/
│   ├── pedido.py
│   ├── pedido_delivery.py
│   └── pedido_retirada.py
└── README.md
```

---

## **How ​​to Run**

1. Access the `main.py` file.
2. Run the program:
```bash
python main.py
```

---

## **Example of Use**

- **Register Customer and Items**:
Create a customer and add items to the order.
- **Create Order**:
Choose between _delivery_ or _pickup_.
- **Make Payment**:
Simulate payments via Pix or Card.
- **Receive Notifications**:
Customers receive notifications about the order status.

---


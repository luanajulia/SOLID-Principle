from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus


cliente = Cliente("Luana", "Iraja")
item = Item("hamburger", 20)
item_um = Item("pizza", 30)
itens = [item, item_um]
taxa_entrega = 10.0

pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = "O Pagamento foi confirmado"
MENSAGEM_PREPARANDO = "O Pedido esta sendo Preparado!"
MENSAGEM_ENVIADO = "O Pagamento saiu para entrega"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO

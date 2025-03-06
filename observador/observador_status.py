class ObservadorStatus:
    def __init__(self, notificacoes):
        self.notificacoes = notificacoes


    def atualizar(self, pedido):
        mensagem = f"O status do Pedido foi atualizado: {pedido.status}"
        self.notificacoes.enviar_notificacoes(pedido.cliente, mensagem)
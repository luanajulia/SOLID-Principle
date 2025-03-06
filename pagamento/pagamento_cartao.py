from pagamento.pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Processando Pagamento de R$: {valor:.2f} via Cartão.")
    
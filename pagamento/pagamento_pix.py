from pagamento.pagamento import Pagamento

class PagamentoPix(Pagamento):
    def processar(self, valor):
        print(f"Processando Pagamento de R$: {valor:.2f} via Pix.")
    
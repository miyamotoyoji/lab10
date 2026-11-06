"""Exercício 10.5 - Refatoração de Produto.

Code smells no original:
- Divergent Change / Large Class: Produto muda por três motivos distintos
  (regra de imposto, persistência e formato XML) -> viola o SRP.
- Magic Number: 1.15.
- (Extra) SQL montado por concatenação de string: vulnerável a SQL Injection.
  Aqui o INSERT continua apenas impresso, mas com placeholders.

Refatorações aplicadas: Extract Class (CalculadoraDeImposto,
ProdutoRepository, ProdutoXmlExporter) e Replace Magic Number with Constant.
Produto passa a ser só dados.
"""

ALIQUOTA_IMPOSTO = 0.15


class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco


class CalculadoraDeImposto:
    def __init__(self, aliquota=ALIQUOTA_IMPOSTO):
        self.aliquota = aliquota

    def preco_com_imposto(self, produto):
        return produto.preco * (1 + self.aliquota)


class ProdutoRepository:
    def salvar(self, produto):
        sql = "INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?);"
        params = (produto.id_produto, produto.nome, produto.preco)
        print(sql, params)
        return sql, params


class ProdutoXmlExporter:
    def exportar(self, produto):
        return (
            f"<produto><id>{produto.id_produto}</id>"
            f"<nome>{produto.nome}</nome>"
            f"<preco>{produto.preco}</preco></produto>"
        )

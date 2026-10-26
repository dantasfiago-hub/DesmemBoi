import cortes


pecas = {
    "dianteiro": "Dianteiro",
    "traseiro": "Traseiro",
    "ponta_de_agulha_com_fraldinha": "Ponta de agulha com fraldinha",
    "ponta_de_agulha_sem_fraldinha": "Ponta de agulha sem fraldinha",
}


def ler_numero(mensagem):
    return float(input(mensagem).strip().replace(",", "."))


def calcular_cortes(pesos_pecas, valores_totais_pecas):
    precos_por_kg = {}
    for peca in pecas:
        peso = pesos_pecas[peca]
        if peso < 0:
            raise ValueError(f"O peso de {pecas[peca]} não pode ser negativo.")
        if peso > 0:
            precos_por_kg[peca] = valores_totais_pecas[peca] / peso

    cortes_calculados = {}
    for codigo, dados_corte in cortes.cortes_carne.items():
        fatores = dados_corte["fatores_peso"]
        pecas_aplicaveis = [
            peca for peca, fator in fatores.items() if fator != 0
        ]
        if not pecas_aplicaveis:
            raise ValueError(f"O corte {codigo} não possui fator de peso.")

        quantidade_total = sum(
            fatores[peca] * pesos_pecas[peca] for peca in pecas_aplicaveis
        )
        precos_disponiveis = [
            precos_por_kg[peca]
            for peca in pecas_aplicaveis
            if peca in precos_por_kg
        ]
        preco_por_unidade = (
            sum(precos_disponiveis) / len(precos_disponiveis)
            if precos_disponiveis
            else None
        )
        valor_total = (
            quantidade_total * preco_por_unidade
            if preco_por_unidade is not None
            else None
        )

        cortes_calculados[codigo] = {
            "corte": dados_corte["corte"],
            "quantidade_total": quantidade_total,
            "valor_total": valor_total,
            "preco_por_unidade": preco_por_unidade,
        }

    return cortes_calculados
5

def exportar_cortes_txt(cortes_calculados, caminho="cortes_calculados.txt"):
    with open(caminho, "w", encoding="utf-8", newline="\n") as arquivo:
        for codigo, dados_corte in cortes_calculados.items():
            quantidade_total = dados_corte["quantidade_total"]
            if quantidade_total == 0:
                continue

            quantidade = format(quantidade_total, ".4f")
            quantidade = quantidade.rstrip("0").rstrip(".").replace(".", ",")
            valor_unitario = dados_corte["preco_por_unidade"]
            if valor_unitario is None:
                valor_unitario = ""
            else:
                valor_unitario = format(valor_unitario, ".4f")
                valor_unitario = (
                    valor_unitario.rstrip("0").rstrip(".").replace(".", ",")
                )
            arquivo.write(f"{codigo};{quantidade};1;{valor_unitario}\n")

pesos_pecas = {}
valores_totais_pecas = {}
for chave, nome in pecas.items():
    pesos_pecas[chave] = ler_numero(f"Digite o peso do corte {nome} (kg): ")
    if pesos_pecas[chave] > 0:
        valores_totais_pecas[chave] = ler_numero(
            f"Digite o valor total do corte {nome} (R$): "
        )
    else:
        valores_totais_pecas[chave] = 0


cortes_calculados = calcular_cortes(pesos_pecas, valores_totais_pecas)
exportar_cortes_txt(cortes_calculados)
for codigo, dados_corte in cortes_calculados.items():
    print(f"{codigo}: {dados_corte}")
print("Arquivo cortes_calculados.txt exportado com sucesso.")

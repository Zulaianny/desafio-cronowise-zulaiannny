#1.1 Fila de processamento

def ordenar_solicitacoes(lista):
    lista_ordenada = sorted(
        lista,
        key=lambda x: (
            0 if x["tipo"] == "URGENTE" else 1,
            x["timestamp"]
        )
    )
    
    return [item["id"] for item in lista_ordenada]

solicitacoes = [
    { "id": 1, "tipo": "NORMAL",  "timestamp": 10 },
    { "id": 2, "tipo": "URGENTE", "timestamp": 20 },
    { "id": 3, "tipo": "NORMAL",  "timestamp": 15 },
    { "id": 4, "tipo": "URGENTE", "timestamp": 5  }
]

resultado_ordenacao = ordenar_solicitacoes(solicitacoes)

print(resultado_ordenacao)

#1.2 Detecção de anomalia

def verificar_alertas(tempos):
    alertas = []
    contador = 0

    for i in range(len(tempos)):
        if tempos[i] > 2000:
            contador += 1
            if contador == 3:
                alertas.append(i)
        else:
            contador = 0

    return alertas

tempos = [300, 2100, 2300, 2500, 400, 2100, 2800, 2200]

resultado_alertas = verificar_alertas(tempos)

print(resultado_alertas)
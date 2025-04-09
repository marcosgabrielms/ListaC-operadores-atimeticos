print("Simulador de Fatura de Cartão de Crédito")
print("------------------------------------------")

# Entrada (Usuário digita o valor total da fatura)

fatura = float(input("Valor total da fatura (R$): "))

print("\nInforme os dois pagamentos simulados:")

p1 = float(input("Pagamento no Plano 1 (R$): "))
p2 = float(input("Pagamento no Plano 2 (R$): "))

meses = int(input("\nMeses sem pagar o saldo restante: "))

# Taxas mensais que os bancos cobram por atraso 
juros = 0.12
multa = 0.02
mora = 0.01

# Saldo devedor com proteção contra valores negativos 
# Se o pagamento for maior que a fatura, o saldo vira zero
saldo1 = (fatura - p1) * ((fatura - p1) > 0)
saldo2 = (fatura - p2) * ((fatura - p2) > 0)

# Juros compostos acumulados
fator = (1 + juros + multa + mora) ** meses

# Valor final da dívida
final1 = saldo1 * fator
final2 = saldo2 * fator

# Crescimento percentual (divida em porcentagem)
cres1 = ((final1 - saldo1) / (saldo1 + 0.0001)) * 100
cres2 = ((final2 - saldo2) / (saldo2 + 0.0001)) * 100

# Resultados (Resumo do planos)
print("\n--- RESULTADO FINAL ---")

print("\nPlano 1:")
print(f"Pagamento: R$ {p1:.2f}")
print(f"Saldo inicial: R$ {saldo1:.2f}")
print(f"Fatura ao final de {meses} meses: R$ {final1:.2f}")
print(f"Aumento percentual: {cres1:.2f}%")

print("\nPlano 2:")
print(f"Pagamento: R$ {p2:.2f}")
print(f"Saldo inicial: R$ {saldo2:.2f}")
print(f"Fatura ao final de {meses} meses: R$ {final2:.2f}")
print(f"Aumento percentual: {cres2:.2f}%")

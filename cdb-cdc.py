print("Simulador de Investimento CDB e Empréstimo CDC\n")

# Simulação do CDB
print(">>> SIMULAÇÃO CDB <<<")

valor = float(input("Informe o valor a ser investido (R$): "))
taxa_cdb = float(input("Informe a taxa de juros anual do CDB (%): "))
ano_final = int(input("Ano de vencimento: "))
ano_atual = int(input("Ano atual: "))

tempo_cdb = ano_final - ano_atual
juros_cdb = taxa_cdb / 100

# Fórmula de juros compostos: M = P * (1 + i)^t
montante_cdb = valor * (1 + juros_cdb) ** tempo_cdb
rendimento_cdb = montante_cdb - valor

print("\nResultado da aplicação CDB:")
print(f"Valor investido: R$ {valor:.2f}")
print(f"Prazo: {tempo_cdb} anos")
print(f"Montante final: R$ {montante_cdb:.2f}")
print(f"Rendimento: R$ {rendimento_cdb:.2f}")

# Simulação do CDC 
print("\n>>> SIMULAÇÃO CDC <<<")

taxa_cdc = float(input("Informe a taxa de juros mensal do empréstimo (%): "))
parcelas = int(input("Informe o número de parcelas (ex: 24, 36, 60): "))

taxa_cdc_mensal = taxa_cdc / 100
# Fórmula da parcela fixa de financiamento 
parcela = valor * ((taxa_cdc_mensal * (1 + taxa_cdc_mensal) ** parcelas) / ((1 + taxa_cdc_mensal) ** parcelas - 1))
total_cdc = parcela * parcelas
juros_cdc_total = total_cdc - valor

print("\nResultado do empréstimo CDC:")
print(f"Valor financiado: R$ {valor:.2f}")
print(f"Nº de parcelas: {parcelas}")
print(f"Valor de cada parcela: R$ {parcela:.2f}")
print(f"Montante total pago: R$ {total_cdc:.2f}")
print(f"Total de juros pagos: R$ {juros_cdc_total:.2f}")

# Lucro do Banco 
lucro_banco = juros_cdc_total - rendimento_cdb

print("\n>>> RESUMO FINAL <<<")
print(f"Lucro do banco na operação: R$ {lucro_banco:.2f}")

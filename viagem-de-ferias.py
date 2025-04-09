print("------ Simulador de Viagem com Carro Híbrido (BYD) ------")

# Coleta de informações
km_viagem = float(input("Informe a distância total da viagem (km): "))
valor_gas = float(input("Preço do litro da Gasolina (R$): "))
valor_alc = float(input("Preço do litro do Álcool (R$): "))
porcentagem_eletrico = float(input("Percentual da viagem com motor elétrico (%): "))

# Cálculo da parte da viagem
porcentagem_combustao = 100 - porcentagem_eletrico
km_combustao = km_viagem * (porcentagem_combustao / 100)

# Consumo médio do carro
km_por_litro_gas = 12                       # padrão para gasolina
km_por_litro_alc = km_por_litro_gas * 0.8   # 80% da gasolina

# Quantidade de litros necessários
litros_gas = km_combustao / km_por_litro_gas
litros_alc = km_combustao / km_por_litro_alc

# Custos 
gasto_gas = litros_gas * valor_gas
gasto_alc = litros_alc * valor_alc

# Resultado 
print("\n>>> Estimativa de Combustível <<<\n")

print("Com GASOLINA:")
print(" - Distância com combustível:", round(km_combustao, 2), "km")
print(" - Litros necessários:", round(litros_gas, 2), "L")
print(" - Gasto estimado: R$", round(gasto_gas, 2))

print("\nCom ÁLCOOL:")
print(" - Distância com combustível:", round(km_combustao, 2), "km")
print(" - Litros necessários:", round(litros_alc, 2), "L")
print(" - Gasto estimado: R$", round(gasto_alc, 2))

print("\n----------------------------------------------------------")

def obter_taxa_iva(codigo_produto):
    return int(codigo_produto % 100)

def calcular_preco_final(preco_sem_iva, taxa_iva):
    preco_com_iva = preco_sem_iva * (1 + taxa_iva / 100)
    return round(preco_com_iva)

codigo_produto = int(input("Digite o código do produto (11 dígitos): "))
preco_sem_iva = float(input("Digite o preço do produto sem IVA: "))

taxa_iva = obter_taxa_iva(codigo_produto)
preco_final = calcular_preco_final(preco_sem_iva, taxa_iva)

print(f"O produto com código {codigo_produto}, tem a taxa de IVA = {taxa_iva}% e o preço final é de {preco_final} euros.")

def exibir_componentes(numero):
    parte_inteira = int(numero)
    print(f"Parte inteira: {parte_inteira}")
    
    parte_decimal = int((numero * 1000) % 1000)
    print(f"Parte decimal: {parte_decimal}")
    
    todos_algarismos = [
        parte_inteira // 100, 
        (parte_inteira // 10) % 10, 
        parte_inteira % 10, 
        parte_decimal // 100, 
        (parte_decimal // 10) % 10, 
        parte_decimal % 10
    ]
    print(f"Todos os algarismos: {', '.join(map(str, todos_algarismos))}")

# Usei este numero como exemplo
numero = 123.456
exibir_componentes(numero)

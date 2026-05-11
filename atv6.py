#exercício 1
número_1 = input('Primeiro número: ')
número_2 = input('Segundo número: ')

if número_1 > número_2:
    print(f'{número_1} é o maior!')
elif número_1 < número_2:
    print(f'{número_2} é o maior!')
#exercício 2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
else:
    print("O maior número é:", num2)
#exercício 3
valor = float(input("Digite um valor: "))

if valor >= 0:
    print("O valor é positivo.")
else:
    print("O valor é negativo.")
#exercício 4
letra = input("Digite F ou M: ").upper()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido.")
#exercício 5
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
#exercício 6
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print("O maior número é:", maior)
#exercício 7
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Definindo maior e menor inicialmente
maior = num1
menor = num1

# Verificando o maior
if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

# Verificando o menor
if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print("Maior número:", maior)
print("Menor número:", menor)
#exercício 8
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

menor = produto1
produto = "Produto 1"

if produto2 < menor:
    menor = produto2
    produto = "Produto 2"

if produto3 < menor:
    menor = produto3
    produto = "Produto 3"

print(f"Você deve comprar o {produto}, pois é o mais barato.")
#exercício 9
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista = [num1, num2, num3]

lista.sort(reverse=True)

print("Números em ordem decrescente:")
print(lista)
#exercício 10

turno = input("Digite o turno em que você estuda (M/V/N): ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
#exercício 11

salario = float(input("Digite o salário do colaborador: R$ "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print("\n--- Resultado do Reajuste ---")
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
#exercício 12
valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas

# INSS fixo de 10%
inss = salario_bruto * 0.10

# Sindicato fixo de 3%
sindicato = salario_bruto * 0.03

# Imposto de Renda
if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

ir = salario_bruto * (ir_percentual / 100)

# FGTS (não descontado)
fgts = salario_bruto * 0.11

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("\n--- Folha de Pagamento ---")
print(f"Salário Bruto: (R$ {valor_hora:.2f} * {horas:.0f}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%)                 : R$ {ir:.2f}")
print(f"(-) INSS (10%)                 : R$ {inss:.2f}")
print(f"(-) Sindicato (3%)             : R$ {sindicato:.2f}")
print(f"FGTS (11%)                     : R$ {fgts:.2f}")
print(f"Total de descontos             : R$ {total_descontos:.2f}")
print(f"Salário Líquido                : R$ {salario_liquido:.2f}")
#exercício 13
numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Valor inválido!")
#exercício 14
numero = int(input("Digite um número de 1 a 7: "))

dias = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]

if 1 <= numero <= 7:
    print(dias[numero - 1])
else:
    print("Valor inválido!")
#exercício 15
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# Verificando se forma triângulo
if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

else:
    print("Os valores não formam um triângulo.")
#exercício 16
a = float(input("Digite o valor de a: "))

# Verificação se é equação do 2º grau
if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) - (4 * a * c)

    print(f"Delta = {delta:.2f}")

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui apenas uma raiz real:")
        print(f"x = {x:.2f}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("A equação possui duas raízes reais:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
#exercício 17
ano = int(input("Digite um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
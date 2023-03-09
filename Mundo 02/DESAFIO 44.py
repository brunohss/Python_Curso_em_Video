#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

print('\n\033[0;33m====== DESAFIO 44 ======\033[m')

valor=float(input('\nDigite o valor que ser pago:'))
modo=float(input('Digite o metodo que ira ser pago:'))
imc=peso/(altura*altura)
print(f'Seu IMC = {imc :.2f}, na classificação da tabela vc esta :')
if imc < 18.5 : print('Abaixo do peso')
elif imc < 25 : print('Peso ideal')
elif imc < 30 : print('Sobrepeso')
elif imc < 40 : print('Obesidade')
else : print('Obesidade Mórbida')
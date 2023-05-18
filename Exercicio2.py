preco = float(input('Digite o preço de um produto: '))
vdesconto = float(input('Digite o percentual de desconto(0-100%): '))

desconto = preco * (vdesconto / 100)
final = preco - desconto

print('O preço do produto é {}. O Desconto aplicado é de {} % e o valor final é {}'.format(preco,vdesconto,final))
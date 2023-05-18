quantidadeKm = int(input('Digite a quantidade de km percorridos: '))
quantidadeDiasAlugado = int(input('Digite a quantidade de dias que ficou alugado: '))

precoPorDia = quantidadeDiasAlugado * 60
precoPorKm = quantidadeKm * 0.15
totalPagar = precoPorKm + precoPorDia

print('O valor á pagar é de {} por {} dias de aluguel mais {} por {} quilometros rodados e o total é de: {}'.format(precoPorDia,quantidadeDiasAlugado,precoPorKm,quantidadeKm,totalPagar))
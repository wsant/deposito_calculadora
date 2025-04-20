print('=== Simulador de Depósitos Sequenciais ===\n')
print('Escolha uma opção:')
print('1 - Calcular o valor total entre dois depósitos')
print('2 - Informar um valor disponível e ver até qual depósito ele cobre')

opcao = input('\nDigite 1 ou 2: ')

if opcao == '1':
    menor = int(input('\nInforme o valor do primeiro depósito: R$ '))
    maior = int(input('Informe o valor do último depósito: R$ '))
    excluir = input('Deseja excluir algum valor? (Separe com vírgulas, ex: 10,20,30). Pressione Enter para ignorar: ')

    excluidos = list(map(int, excluir.split(','))) if excluir else []

    soma = 0
    lista_utilizada = []
    inicio = menor

    if menor >= maior:
        print('\n[ERRO] O valor inicial deve ser menor que o valor final.')
    else:
        while menor <= maior:
            if menor not in excluidos:
                soma += menor
                lista_utilizada.append(menor)
            menor += 1

        soma_formatada = f'{soma:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f'\nTotal acumulado entre R$ {inicio} e R$ {maior - 1}: R$ {soma_formatada}')
        print(f'Depósitos considerados: {lista_utilizada}')

elif opcao == '2':
    valor_total = int(input('\nInforme o valor que você tem disponível: R$ '))
    menor = int(input('Informe o valor inicial dos depósitos: R$ '))
    excluir = input('Deseja excluir algum valor? (Separe com vírgulas, ex: 10,20,30). Pressione Enter para ignorar: ')

    excluidos = list(map(int, excluir.split(','))) if excluir else []

    soma = 0
    lista_utilizada = []

    while soma + menor <= valor_total:
        if menor not in excluidos:
            soma += menor
            lista_utilizada.append(menor)
        menor += 1

    print(f'\nCom R$ {valor_total}, você consegue fazer {len(lista_utilizada)} depósitos:')
    print(f'Depósitos realizados: {lista_utilizada}')
    print(f'Total acumulado: R$ {soma}')

else:
    print('\n[ERRO] Opção inválida. Reinicie o programa e escolha 1 ou 2.')

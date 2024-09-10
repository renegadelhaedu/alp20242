saq = int(input('diga o valor'))

if(saq >= 10 and saq <= 600 ):
    qtde100 = saq // 100
    saq = saq - (qtde100 * 100)

    qtde50 = saq // 50
    saq = saq - (qtde50 * 50)

    qtde10 = saq // 10
    saq = saq - (qtde10 * 10)

    qtde5 = saq // 5
    saq = saq - (qtde5 * 5)

    qtde1 = saq // 1
    saq = saq - (qtde1 * 1)

    print(f'notas de 100: {qtde100}')
    print(f'notas de 50: {qtde50}')
    print(f'notas de 10: {qtde10}')
    print(f'notas de 5: {qtde5}')
    print(f'notas de 1: {qtde1}')
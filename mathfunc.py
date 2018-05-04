def nod(message):
    
    numbers = [int(x) for x in message.split(' ')[1:]]
    for_msg = f'GCD of numbers {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_NOD = f'GCD of number {c} it is this number {c}.'
        else:
            while len(numbers) != 1:
                a = numbers[0]
                b = numbers[1]
                while a!= 0 and b!=0:
                    if a > b:
                        a %= b
                    else:
                        b %= a
                c = a + b
                del numbers[0]
                del numbers[0]
                numbers.insert(0, c)
                message_NOD = f'{for_msg} = {c}.'
                
    return message_NOD
                
                
def nok(message):
    
    numbers = [int(x) for x in message.split(' ')[1:]]
    for_msg = f'LCM of numbers {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_NOK = f'LCM of number {c} it is this number {c}.'
        else:
            while len(numbers) != 1:
                a = numbers[0]
                b = numbers[1]
                ab = a * b
                while a != 0 and b != 0:
                    if a > b:
                        a %= b
                    else:
                        b %= a
                c = ab // (a + b)
                del numbers[0]
                del numbers[0]
                numbers.insert(0, c)  
                message_NOK = f'{for_msg} = {c}.'
                
    return message_NOK

                
def factor(message):
    
    number = int(message.split()[1])
    for_msg = number
    i = 2
    factor = []
    
    while number > 1:
        while number % i == 0:
            factor.append(i)
            number //= i
        i += 1
        
    message_factor = f'Factorization of number {for_msg} = {factor}.'
    
    return message_factor


def polynoms_add(message):
    
    polynoms = message.split('/polynoms_add ')[1]
    poly_1 = polynoms.split(' + ')[0]
    poly_2 = polynoms.split(' + ')[1]
    coef_1 = [int(x) for x in poly_1.split(' ')[0:]]
    coef_2 = [int(x) for x in poly_2.split(' ')[0:]]
    msg = f'Sum of polynomials with coefficients {coef_1} and {coef_2}'

    if len(coef_1) < len(coef_2):
        while len(coef_1) != len(coef_2):
            coef_1.insert(0, 0)
    else:
        while len(coef_1) != len(coef_2):
            coef_2.insert(0, 0)
        
    sum_coef = [coef_1[i] + coef_2[i] for i in range(len(coef_1))]
    message_poly_sum = f'{msg} is polynomial with coefficients {sum_coef}.'
    
    return message_poly_sum


def polynoms_sub(message):
    
    polynoms = message.split('/polynoms_sub ')[1]
    poly_1 = polynoms.split(' - ')[0]
    poly_2 = polynoms.split(' - ')[1]
    coef_1 = [int(x) for x in poly_1.split(' ')[0:]]
    coef_2 = [int(x) for x in poly_2.split(' ')[0:]]
    msg = f'Subtraction of polynomials with coefficients {coef_1} and {coef_2}'

    if len(coef_1) < len(coef_2):
        while len(coef_1) != len(coef_2):
            coef_1.insert(0, 0)
    else:
        while len(coef_1) != len(coef_2):
            coef_2.insert(0, 0)
        
    sub_coef = [coef_1[i] - coef_2[i] for i in range(len(coef_1))]
    message_poly_sub = f'{msg} is polynomial with coefficients {sub_coef}.'
    
    return message_poly_sub

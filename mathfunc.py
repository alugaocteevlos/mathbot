def nod(message):
    
    numbers = [int(x) for x in message.text.split(' ')[1:]]
    for_msg = f'НОД чисел {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_NOD = f'НОД числа {c} есть само это число, т.е. {c}.'
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
    
    numbers = [int(x) for x in message.text.split(' ')[1:]]
    for_msg = f'НОК чисел {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_NOK = f'НОК числа {c} есть само это число, т.е. {c}.'
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
    
    number = int(message.text.split()[1])
    for_msg = number
    i = 2
    factor = []
    
    while number > 1:
        while number % i == 0:
            factor.append(i)
            number //= i
        i += 1
        
    message_factor = f'Факторизация числа {for_msg} = {factor}.'
    
    return message_factor
import re


def gcd(message):
    
    numbers = [int(x) for x in message.split(' ')[1:]]
    for_msg = f'GCD of numbers {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_gcd = f'GCD of number {c} it is this number {c}.'
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
                message_gcd = f'{for_msg} = {c}.'
                
    return message_gcd
                
                
def lcm(message):
    
    numbers = [int(x) for x in message.split(' ')[1:]]
    for_msg = f'LCM of numbers {numbers}'
    
    for i in numbers:
        if len(numbers) == 1:
            c = numbers[0]
            message_lcm = f'LCM of number {c} it is this number {c}.'
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
                message_lcm = f'{for_msg} = {c}.'
                
    return message_lcm

                
def factor(message):
    
    number = int(message.split()[1])
    for_msg = number
    i = 2
    factor = []
    
    if number > 0:
        while number > 1:
            while number % i == 0:
                factor.append(i)
                number //= i
            i += 1
            
    elif number < 0:
        num = -number
        while num > 1:
            while num % i == 0:
                factor.append(i)
                num //=i
            i += 1
        tmp = factor[0]
        factor[0] = -tmp
        
    if len(factor) <= 1:
        message_factor = f'{for_msg} - prime number.'
    else:
        message_factor = f'Factorization of number {for_msg} = {factor}.'
    
    return message_factor


def polynoms_add(message):
    
    polynoms = message.split('/polynoms_add ')[1]
    poly_1, poly_2 = polynoms.split(')+(')[0:2]
    coef_1 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", poly_1)]
    coef_2 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", poly_2)]
    msg = f'Sum of polynomials with coefficients {coef_1} and {coef_2}'

    if len(coef_1) < len(coef_2):
        while len(coef_1) != len(coef_2):
            coef_1.insert(0, 0)
    else:
        while len(coef_1) != len(coef_2):
            coef_2.insert(0, 0)
        
    sum_coef = [coef_1[i] + coef_2[i] for i in range(len(coef_1))]
    message_poly_add = f'{msg} is polynomial with coefficients {sum_coef}.'
    
    return message_poly_add


def polynoms_sub(message):
    
    polynoms = message.split('/polynoms_sub ')[1]
    poly_1, poly_2 = polynoms.split(')-(')[0:2]
    coef_1 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", poly_1)]
    coef_2 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", poly_2)]
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


def polynoms_mul(message):
    
    polynoms = message.split('/polynoms_mul ')[1]
    polynom_1, polynom_2 = polynoms.split('*')[0:2]
    coef_1 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", polynom_1)]
    coef_2 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", polynom_2)]
    for_msg = f'Multiplication of polynomials with coefficients {coef_1} and {coef_2}'
    
    coefs = []
    for i in range(len(coef_1)*len(coef_2)):
        coefs.append([])
        
    m = len(coef_1) + len(coef_2) - 1
    i = 0
    j = 0
    
    while i < len(coef_1):
        k = 0
        while k < len(coef_2):
            coefs[j] = [0 for i in range(m-1)]
            coefs[j].insert(i+k, coef_1[i]*coef_2[k])
            k += 1
            j += 1
        i += 1
            
    n = 0      
    coef_mul = [0 for i in range(m)]
    
    while n < len(coefs):
        coef_mul = [coef_mul[i] + coefs[n][i] for i in range(m)]
        n += 1
        
    if coef_mul[0] == 0:
        while coef_mul[0] == 0:
            del coef_mul[0]
        
    msg_poly_mul = f'{for_msg} is polynomial with coefficients {coef_mul}.'
    
    return msg_poly_mul


def polynoms_div(message):
    
    polynoms = message.split('/polynoms_div ')[1]
    polynom_1, polynom_2 = polynoms.split('/')[0:2]
    coef_1 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", polynom_1)]
    coef_2 = [int(x) for x in re.findall(r"[*-][0-9]+|[0-9]+", polynom_2)]
    for_msg = f'Division of polynomials with coefficients {coef_1} and {coef_2}'
    
    if len(coef_2) > len(coef_1):
        msg_poly_div = f'{for_msg} is impossible, because power of second polynomial is greater.'
    else:    
        p = 0
        s = len(coef_1) - len(coef_2) + 1    
        coef_div = [0 for i in range(s)]
    
        while p < len(coef_div):
        
            n = coef_1[0] / coef_2[0]
            coef_div.insert(p, n)
            del coef_div[len(coef_div)-1]
        
            coefs = []
            for i in range(len(coef_2)):
                coefs.append([])
        
            m = len(coef_div) + len(coef_2) - 1
            j = 0    
    
            while j < len(coef_2):
                coefs[j] = [0 for i in range(m)]
                coef_tmp = [0 for i in range(len(coef_div)-1)]
                tmp = coef_div[p]
                coef_tmp.insert(p, tmp)
                del coef_tmp[len(coef_tmp)-1]
                for i in coef_tmp:
                    ics = coef_tmp.index(i) + j
                    coefs[j][ics] = i*coef_2[j]
                j += 1
        
            n = 0
            coef_mul = [0 for i in range(m)]
    
            while n < len(coefs):
                coef_mul = [coef_mul[i] + coefs[n][i] 
                            for i in range(len(coefs[n]))]
                n += 1
        
            if p + 1 != len(coef_div):
                if coef_mul[0] == 0:
                    while coef_mul[0] == 0:
                        del coef_mul[0]
                           
            coef_sub = []
        
            if len(coef_mul) < len(coef_1):      
                while len(coef_1) != len(coef_mul):
                    coef_mul.append(0)
            
            coef_sub = [coef_1[i] - coef_mul[i] 
                        for i in range(len(coef_1))]
        
            if coef_sub[0] == 0:
                while coef_sub[0] == 0:
                    del coef_sub[0]
                
            coef_1 = coef_sub
            p += 1
        
        if len(coef_1) == len(coef_2):
            d = 0
            while coef_1[0] != 0:
                d += 1
                if coef_1[0] > 0:
                    coef_1 = [coef_1[i] - coef_2[i] 
                              for i in range(len(coef_1))]
                elif coef_1[0] < 0:
                    coef_1 = [coef_1[i] + coef_2[i] 
                              for i in range(len(coef_1))]
                if coef_1[0] == 0:
                    break
            if len(coef_div) != s:
                if d != 0:
                    coef_div.append(d)
                
        cd = [int(x) for x in coef_div]
    
        if coef_1 == [0 for i in range(len(coef_1))]:
            rm = 'remainder is not.'
        else:
            while coef_1[0] == 0:
                del coef_1[0]
            rem = [int(x) for x in coef_1]
            if len(rem) == 1:
                rm = f'remainder is {rem[0]}.'
            else:
                rm = f'remainder is {rem}.'
    
        msg_poly_div = f'{for_msg} is polynomial with coefficients {cd} and {rm}'
    
    return msg_poly_div


def euclidean_algorithm(a, b):
    
    if not b:
        return (1, 0, a)
    
    y, x, gcd = euclidean_algorithm(b, a%b)
    
    return (x, y - (a // b) * x, gcd)


def lin_dep(message):
    
    numbers = [int(x) for x in message.split(' ')[1:3]]
    for_msg = f'Linear decomposition of numbers {numbers[0]} and {numbers[1]}'
    
    answer = [int(x) for x in euclidean_algorithm(numbers[0], numbers[1])]
    check_gcd = answer[0]*numbers[0] + answer[1]*numbers[1]
    
    coefs = f'{answer[0]}*{numbers[0]} + {answer[1]}*{numbers[1]}'
    msg_lin_dep = f'{for_msg} is {coefs} = {check_gcd}.'
    
    return msg_lin_dep

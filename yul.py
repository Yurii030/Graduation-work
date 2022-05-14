from unittest import result


def xy_add(num1,num2):
    result = num1+num2
    return result
def xy_sub(num1,num2):
    result = num1-num2
    return result
def xy_mul(num1,num2):
    result = num1 * num2
    return result

def xy_div(num1,num2):
    result = num1/num2
    return result

N1 = input ("첫번째 값입력 :")
N2= input ("두번째 값입력 :")
print("두수의 합은 :",xy_add(N1,N2))
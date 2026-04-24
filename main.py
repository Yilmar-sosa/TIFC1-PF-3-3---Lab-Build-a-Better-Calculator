



def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
       total += num
    return total

def multiplymultiplenumbers(numbers):
    total = 0 
    for num in numbers:
       total *= num
    return total

def isiteven(num): 
    if isinstance(num, int) and num % 2 == 0:
        return True
    else:
        return False

def isitaninteger(num):
    if isinstance(num, int):
        return True
    else:
        return False
def main():
    print("Calculadora mejorada")
    nums = [5,8,10,13]

    print("suma", addmultiplenumbers(nums))
    print("multiplicacion", multiplymultiplenumbers(nums))
    print("¿Es par?", isinstance(3))
    print("¿Es entero?", isinstance(5))

    if __name__=="__main__":
      main()
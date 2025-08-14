num=1
primos=[]
nprimo=int(input('introduzca hasta que numero impar quiere sumar: '))
while True:
    
    if len(primos)!=nprimo:
        for i in range(1,num+1):
            if i == 1 & num==i:
                primos.append(num)
            elif num%i==0 & i==num:
                primos.append(num)
                break
            
        num=num+1
    else:
        break

    
listSum = sum(primos)
print(primos)
print(f"Suma de los numeros -> {listSum}")
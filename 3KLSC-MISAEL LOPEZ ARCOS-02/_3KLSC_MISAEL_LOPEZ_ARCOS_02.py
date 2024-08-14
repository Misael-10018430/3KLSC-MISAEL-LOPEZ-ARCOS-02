
NUM = 8
nums = [0]*NUM
total = 0
for i in range (NUM):
    nums[i] = int(input("POR FAVOR INTRODUZCA EL NUMERO: "))
    total += nums[i]
    print ("El totoal de numeros es: ",total)
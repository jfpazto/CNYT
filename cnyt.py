import math
def suma(arr1,arr2):
    return [int(arr1[0])+int(arr2[0]),int(arr1[1])+int(arr2[1])]
def resta(arr1,arr2):
    return [int(arr1[0])-int(arr2[0]),int(arr1[1])-int(arr2[1])]
def multiplicacion(arr1,arr2):
    return [(int(arr1[0])*int(arr2[0]))-(int(arr1[1])*int(arr2[1])),(int(arr1[0])*int(arr2[1]))+(int(arr1[1])*int(arr2[0]))]
def conjugado(arr1):
    return [int(arr1[0]),int(arr1[1])*-1]
def division(arr1,arr2):
    conju=conjugado(arr2)
    divisor=multiplicacion(arr1,conju)
    dividendo=multiplicacion(arr2,conju)
    if dividendo[0] != 0:
        return [divisor[0]/dividendo[0],divisor[1]/dividendo[0]]
    else:
        print("ERROR, no se puede dividir por cero")
def modulo(arr1):
    return [math.sqrt(int(arr1[0])**2+int(arr1[1])**2)]
def Bin_polar(arr1):
    mod=modulo(arr1)
    direc=math.atan(arr1[1]/arr1[0])
    return [mod,direc]


print(Bin_polar([-3,-2]))

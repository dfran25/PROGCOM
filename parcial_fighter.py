def crear_salon1(n):
    salon1 ={}
    
    for i in range(1, n+1):
        salon1[i]=[]
    return salon1
def crear_salon2(n):
    salon2={}
    
    for i in range(1,n+1):
        salon2[i]=[]
    return salon2
def crear_salon3(n):
    salon3={}

    for i in range(1+n+1):
        salon3[i]=[]
    return salon3

estudiantes1=int(input("Ingrese la cantidad de estudiantes del salon1 "))
salon1=crear_salon1(estudiantes1)
estudiantes2=int(input("Ingrese la cantidad de estudiantes del salon2 "))
salon2=crear_salon2(estudiantes2)
estudiantes3=int(input("Ingrese la cantidad de estudiantes del salon3 "))
salon3=crear_salon3=(estudiantes3)

print(salon1)
print(salon2)
print(salon3)


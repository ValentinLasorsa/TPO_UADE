import os 
import random
huesped=1
print("-Bienvenido al hotel, usted es el "+str(huesped)+" huesped-")
dni=int(input("Ingrese su DNI, sin puntos y todo junto "))
while dni>0:
    huesped+=1
    nReserva=random.randint(1, 100)
    nombre=input("¿Cómo se llama? ")
    apellido=input("¿Y su apellido? ")
    trabajo=input("¿A qué se dedica? ")
    telefono=int(input("Ingrese su teléfono sin prefijos y todo junto "))
    direccion=input("Digame su dirección ")
    tipoHabitacion = int(input("¿Qué tipo de habitación prefiere? Estándar(1), Premium(2), King(3): "))
    while tipoHabitacion != 1 and tipoHabitacion != 2 and tipoHabitacion != 3:
        tipoHabitacion = int(input("¡Ingrese tipo de habitación válida! Estándar(1), Premium(2), King(3): "))
    dias=int(input("¿Cuantos días tiene pensado quedarse? "))
    noches=dias-1
    if tipoHabitacion ==1:
        precio=noches*100000
    elif tipoHabitacion ==2:
        precio=noches*200000
    elif tipoHabitacion ==3:
        precio=noches*350000
    if dias>=7:
        dto=(17*precio)/100
        precio=precio-dto    
    subtotal=precio
    SiONoCochera=input("¿Va a desear el uso de una cochera? SI o NO (respete mayúsculas) ")
    while SiONoCochera != "SI" and SiONoCochera != "NO":
        SiONoCochera=input("¿Va a desear el uso de una cochera? SI o NO (respete mayúsculas) ")
    if SiONoCochera == "SI":
        cochera=int(input("Ingrese si desea una común(1) o techada(2) "))
        while cochera!=1 and cochera!=2:
            cochera=int(input("Ingrese si desea una común(1) o techada(2) "))
        if cochera == 1:
            precio=precio+15000*dias
        else:
           precio=precio+35000*dias
    print("\033[1m-Datos del hotel-\033[0m ")
    print("\033[1m-Sus datos-\033[0m Nombre:",nombre,"Apellido:",apellido, "DNI:"+str(dni)+" Ocupación:",trabajo,"Teléfono:"+str(telefono)+" Dirección:",direccion)
    print("\033[1mRESERVA\033[0m")
    print("Número de reserva:"+str(nReserva)+" Tipo de habitación:"+str(tipoHabitacion)+" Cantidad de días a hospedarse:",dias,"Subtotal:"+str(subtotal)+"$ Alquiler de cocheras:",SiONoCochera,"Tiene un descuento de:"+str(dto)+"$ Total:"+str(precio)+"$") 
    input("\033[1mPresione enter para continuar\033[0m")
    os.system('cls')    
    print("-Bienvenido al hotel, usted es el "+str(huesped)+" huesped-")
    dni=int(input("Ingrese su DNI, sin puntos y todo junto "))
if huesped==1:
    print("¡No se han ingresado datos!")
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')    
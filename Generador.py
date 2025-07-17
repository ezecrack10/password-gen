import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"  
longitud = int(input("Este es el generador de contraseñas\n¿Cuantos caracteres debe tener tu contraseña? ")) 
contraseña = "" 

for i in range(longitud): 
    contraseña += random.choice(caracteres) 

print("Tu contraseña generada es:", contraseña)

import random as r

character = '+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890'
pass_lenght = int(input('Introdusca la longitud de la clave'))

password = ''

for i in range (pass_lenght):
    password += r.choice(character)

print(password)

a = len(password)
print('Cantidad de caracteres:', a)

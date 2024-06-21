# 1stProject
meme_dict = {'XD': 'Se usa cuando algo es gracioso',
             'POSSER': 'fan por moda',
             'CHAMBA': 'trabajar',
             'FANBOY': 'es un fan ciego'
            }
for i in range(5):
    word = input('Qué palabra quieres aprender?').upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Aún falta agregar elementos al diccionario')

print('¡Bienvenido!')
print('¡Este es un quiz diseñado para saber tu nivel de ignorancia!')
print('¡Participa y descubre qué tan idiota eres!')
playing = input('¿Quieres jugar un juego? :} ')
print(playing)

if playing.lower() != 'si':
    quit()

print('¡Bien! ¡Juguemos!')
puntaje = 0

answer = input('¿Cuál es el quinto planeta del sistema solar? ')
if answer.lower() == 'jupiter':
    print('¡Correcto!')
    print('Júpiter es el planeta más grande del sistema solar y el quinto en orden de lejanía al Sol.')
    puntaje += 1
else:   
    print('¡Incorrecto!')
    print('¡Ush que brut@!')

answer = input('¿Cuál es el país más extenso del mundo? ')
if answer.lower() == 'rusia':
    print('¡Correcto!')
    print('Rusia es el país más extenso del mundo. La Federación de Rusia cuenta con una superficie de 17 098 242 km².')
    puntaje += 1
else:   
    print('¡Incorrecto!')
    print('¡A repetir primaria parce!')

answer = input('¿Cuál es el elemento más abundante en el universo? ')
if answer.lower() == 'hidrogeno':
    print('¡Bien!')
    print('El hidrógeno es el elemento químico más abundante del universo, suponiendo más del 75 % en materia normal por masa y más del 90 % en número de átomos.')
    puntaje += 1
else:   
    print('¡Incorrecto!')
    print(':}')

answer = input('¿Quién es el sapo hijueputa más grande de Colombia? ')
if answer.lower() == 'uribe':
    print('¡Correcto!')
    print('URIBE PARACO HIJUEPUTA!!')
    puntaje += 1
else:   
    print('¡Incorrecto!')
    print('¡MONGOLOIDE, LE PONOGO 0 POR BRUTO!')
print('Obtuviste un puntaje de ' + str(puntaje) + ' respuestas correctas!')
print('Obtuviste un puntaje de ' + str((puntaje / 4) * 100) + '%.')


#import ColabTurtle.Turtle as t
#t.initializeTurtle(initial_speed=10)

clientInput =  "f100r90f100r90f100r90f100"
allowedLetters = ['f', 'b', 'r', 'l']

#Podriamos validar que la entrada (input) del usuario deba comenzar si o si con letra.

#creamos dos listas una para los movimientos y otra para la cantidad de movimiento, lo asociamos segun la posición
cantMovementsList = []
movementsList = []
cantMovements = ''
movement= ''
for i in clientInput:
    if (i in allowedLetters):
        movementsList.append(i)
        if(cantMovements != ''):
            cantMovementsList.append(int(cantMovements))
            cantMovements = ''
    else: 
        cantMovements = cantMovements + i
#agregamos la ultima cantidad de movimiento
cantMovementsList.append(cantMovements)

print(cantMovementsList)
print(movementsList)

#luego recorremos la lista con el mismo indice, por eso usamos while y hacemos que la turtle haga lo suyo
j= 0
while(j< len(movementsList)):
    if (movementsList[j] == 'f'):
        #t.forward() 
        print("f: ", cantMovementsList[j])
    elif (movementsList[j] == 'b'):
        #t.backward() 
        print("b: ", cantMovementsList[j])
    elif (movementsList[j] == 'r'):
        #t.right() 
        print("r ", cantMovementsList[j])
    elif (movementsList[j] == 'l'):
        #t.left() 
        print("l: ", cantMovementsList[j])
    j+=1



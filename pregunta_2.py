
lista_persona=[]

sw = True


def listar_persona():
    if len(lista_persona) == 0:
        print('Lista vacia')
    else:
        print(lista_persona)


def agregar_persona():
    persona = input('Ingrese datos de la persona ')
    lista_persona.append(persona)
    print('Persona agregada!')


def persona_existente(persona):
    if persona in lista_persona:
        return True
    else:
        return False


def buscar_persona():
    persona_buscar = input('Ingrese la persona a buscar: ')
    if persona_existente(persona_buscar):
        print('La persona esta registrada')
    else:
        print('No existe la persona')

def eliminar_persona():
    persona_eliminar = input('Ingrese el nombre de la persona a Eliminar ')
    if persona_existente(persona_eliminar):
        print('eliminada')
        lista_persona.remove(persona_eliminar)
    else:
        print('La persona no esta registrada')

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')




#La interfaz del usuario
menu = '''
======= Tiendita ======
1. Listar Persona
2. Agregar Persona
3. Buscar Persona
4. Borrar Persona
5. Salir
'''


while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        listar_persona()
    elif opcion == 2:
        agregar_persona()
    elif opcion == 3:
        buscar_persona()
    elif opcion is 4:
        eliminar_persona()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()






def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')


# La interfaz del usuario
menu = '''
======= Tiendita ======
1. Listar Frutas
2. Agregar Fruta
3. Buscar Fruta
4. Borrar Fruta
5. Salir
'''

# is == ; not is !=

while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        listar_frutas()
    elif opcion == 2:
        agregar_fruta()
    elif opcion == 3:
        buscar_fruta()
    elif opcion is 4:
        eliminar_fruta()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()
bandas=[]


#construyendo la interfaz

print("ALTAVOZ ES TU VOZ")
print("*****************")

opcion=100
while(opcion!=5):

    print("1.Registrar banda")
    print("2.Buscar banda")
    print("3.Mostrar banda")
    print("4.Modificar banda")
    print("5.salir")

    opcion=int(input("Digita una opción: "))

    if opcion == 1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("digita el id: "))
        banda["nombre"]=int(input("Nombre de la banda: "))
        banda["genero"]=int(input("Genero de la banda: "))
        banda["clasificacion"]=int(input("Clasificacion de la banda: "))
        banda["tiempo"]=int(input("cuánto tiempo se presentará: "))
        banda["costo"]=int(input("cuánto cuesta la presentación: $"))
            
            # AGRGEGANDO UN DICCIONARIO A UNA LISTA
        bandas.append(banda)

    elif opcion == 2:
        
        bandaBuscada=input("Digite el nombre de la banda que está buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #COMO LO ENCONTRÉ, MUESTRO LOS DATOS de bandauxiliar
                print(f"id:{bandAuxiliar["id"]} --- nombre: {bandAuxiliar["nombre"]}")
                
            else:
                print("parce siga buscando... ")

    elif opcion == 3:
        
        print(bandas)

    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass
        
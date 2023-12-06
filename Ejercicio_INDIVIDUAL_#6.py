# Gerardo Fernandez 
# En este programa seras capaz de analizar estadísticas interesantes sobre tus Pokemons y asi ser el mejor!

# Importar modulos
import func_pandas

# Declarar variables
seguir_en_programa = True

# Programa principal
while seguir_en_programa == True:

    print("")
    print("### BIENVENIDO ###")
    print("¿Qué desea hacer?")
    print("1. Contar cuantos Pokemons hay en total")
    print("2. Realizar un conteo por Type 1")
    print("3. Contar cuántos Pokemons tiene Type 2")
    print("4. Encontrar el Type 1 con mayor HP promedio")
    print("5. Encontrar el Type 1 con ataque promedio")
    print("6. Contar cuantos Pokemos tienen defensa arriba de 50 y menor de 100")
    print("7. Encontrar al top 10 de Pokemons con velocidad ataque más rápido")
    print("8. Encontrar al top 10 de Pokemons con velocidad de defensa más lento")
    print("9. Mostrar un histograma de las velocidades")
    print("10. Contar la cantidad de Pokemons por Generación")
    print("11. Mostrar la información de los Pokemons que son legendarios")
    print("12. Mostrar un grafico de barras ensañando cuantos pokemons hay de cada tipo basado en tipo 1")
    print("13. Salir")
    print("")

    opcion = input("Seleccione una opción válida: ")

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)
    
    # Opcion 1: Contar cuantos Pokemons hay en total
    if opcion == 1:
        func_pandas.contar_pokemos()

    # Opcion 2: Realizar un conteo por Type 1
    if opcion == 2:
        func_pandas.contar_tipo1()

    # Opcion 3: Contar cuántos Pokemons tienen Type 2
    if opcion == 3:
        func_pandas.contar_tipo2()

    # Opcion 4: Encontrar el Type 1 con mayor HP promedio
    if opcion == 4:
        func_pandas.tipo1_HP()

    # Opcion 5: Encontrar el Type 1 con ataque promedio
    if opcion == 5:
        func_pandas.tipo1_attack()
    
    # Opcion 6: Contar cuantos Pokemos tienen defensa arriba de 50 y menor de 100
    if opcion == 6:
        func_pandas.def_50_100()
    
    # Opcion 7: Encontrar al top 10 de Pokemons con velocidad ataque más rápido
    if opcion == 7:
        func_pandas.top10_spattack()
    
    # Opcion 8: Encontrar al top 10 de Pokemons con velocidad de defensa más lento
    if opcion == 8:
        func_pandas.top10_spdef()

    # Opcion 9: Mostrar un histograma de las velocidades
    if opcion == 9:
        func_pandas.histrograma_vel()
    
    # Opcion 10: Contar la cantidad de Pokemons por Generación
    if opcion == 10:
        func_pandas.contar_generacion()
    
    # Opcion 11: Mostrar la información de los Pokemons que son legendarios
    if opcion == 11:
        func_pandas.poke_legendario()
    
    # Opcion 12: Mostrar un grafico de barras ensañando cuantos pokemons hay de cada tipo basado en tipo 1
    if opcion == 12:
        func_pandas.tipo1_grafico()()
    
    # Opción 13: Salir del programa
    if opcion == 13:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")        
    else:
        print("Seleccione una opción válida.")
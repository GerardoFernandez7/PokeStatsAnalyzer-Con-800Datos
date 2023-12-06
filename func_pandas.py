# Importar modulos
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("Pokemon.csv")

# Funciones
def contar_pokemos():
    num_poke = df['Name'].count()
    print("")
    print("En total hay " +  str(num_poke) + " pokemons")

def contar_tipo1():
    tipo1 = df['Type 1'].count()
    print("")
    print("Hay " + str(tipo1) + " pokemos de Tipo 1")

def contar_tipo2():
    tipo2 = df['Type 2'].count()
    print("")
    print("Hay " + str(tipo2) + " pokemos de Tipo 2")

def tipo1_HP():
    max_HP = df.loc[df['HP'].idxmax(), 'Type 1']
    print("")
    print("El pokemon tipo 1 con mayor HP promedio es " + str(max_HP))

def tipo1_attack():
    maxt_attack = df.loc[df['Attack'].idxmax(), 'Type 1']
    print("")
    print("El pokemon tipo 1 con mayor ataque promedio es " + str(maxt_attack))

def def_50_100():
    pokemon_defensa = df.loc[(df['Defense'] > 50) & (df['Defense'] < 100)]
    num_pokemon_defensa = pokemon_defensa['Name'].count()
    print("")
    print("Hay", num_pokemon_defensa, "Pokemons con defensa mayor a 50 y menor a 100")

def top10_spattack():
    top = df.sort_values('Sp. Atk', ascending=False)
    top_10 = top.head(10)
    print("")
    print(top_10[['Name', 'Sp. Atk']])

def top10_spdef():
    orden_df = df.sort_values('Sp. Def')
    topdef_10 = orden_df.head(10)
    print("")
    print(topdef_10[['Name', 'Sp. Def']])

def histrograma_vel():
    speed = df['Speed']
    plt.hist(speed, bins=30)
    # Agregar un título y etiquetas a los ejes
    plt.title('Histograma de Velocidades')
    plt.xlabel('Velocidad')
    plt.ylabel('Pokemons')
    # Mostrar el histograma
    plt.show()

def contar_generacion():
    generaciones = df['Generation'].value_counts()
    print("")
    print(generaciones)

def poke_legendario():
    legendario = df.loc[df["Legendary"] == True]
    print("")
    print(legendario)    

def tipo1_grafico():
    tipos_pokemon = df.groupby('Type 1').size().reset_index(name='Cantidad')
    plt.bar(tipos_pokemon['Type 1'], tipos_pokemon['Cantidad'])
    plt.xticks(rotation=90)
    plt.xlabel('Tipo de Pokémon')
    plt.ylabel('Cantidad')
    plt.title('Distribución de los tipos de Pokémon')
    plt.show()
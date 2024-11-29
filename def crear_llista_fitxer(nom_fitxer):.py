def crear_llista_fitxer(nom_fitxer):
    """Llegeix un fitxer i retorna una llista de paraules."""
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.read()  # Llegeix el contingut del fitxer
            llista_paraules = contingut.split()  # Divideix el contingut en paraules
        return llista_paraules
    except FileNotFoundError:
        print("El fitxer no s'ha trobat.")
        return []
    except Exception as e:
        print(f"Ha ocorregut un error: {e}")
        return []

# Prova de la funció
# Assegura't de crear un fitxer de text amb algunes paraules per a la prova
nom_fitxer = 'exemple.txt'

# Exemple de contingut del fitxer 'exemple.txt':
# Hola món, aquest és un exemple de fitxer.
# Conté diverses paraules que seran llegides.

llista = crear_llista_fitxer(nom_fitxer)
print(llista)  # Imprimeix la llista de paraules llegides del fitxer
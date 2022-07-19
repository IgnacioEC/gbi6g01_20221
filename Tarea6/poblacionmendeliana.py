# FUNCIÓN 1. de generación de una población con alelos al azar
import scipy # para números aleatorios

def build_population(N, p):
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

# FUNCIÓN 2. Conteo de frecuencia de pares de alelos
def compute_frequencies(population):
    """ 
    Cuenta los genotipos y devuelve un diccionario de frecuencias genotípicas.
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# FUNCIÓN 3. Reproducción de la población en el modulo del PoblacionMendeliana

def reproduce_population(population):
    """ Crear nueva generación a través de la reproducción. Para cada uno de N nuevos descendientes:
    - elegir a los padres al azar, 
    - la descendencia recibe un cromosoma de cada uno de los padres y dependiendo de la proporcionalidad,
    sus descendientes podrian resultar con caracteres domiantes, recesivos o heterocigotos.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # entero aleatorio entre 0 y N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # posible cromosoma venido de la madre
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #si descendencia == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation

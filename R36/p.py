from random import choice, seed


def solve(domains: list[list[int]], random_seed=None, no_cycle=True) -> tuple:
    """Recibe una lista de listas de enteros que determina el dominio de cada \
variable, con una lista de valores posibles para cada variable.
Escoge aleatoriamente una variable y le asigna aleatoriamente un valor de \ 
su dominio que halla sido escogido todavia. 
Si todos los valores del dominio de la variable han sido escogidos, lanza \ 
una excepcion ValueError.
"""
    if random_seed is not None:
        seed(random_seed)
    domains = [set(d) for d in domains]
    size = len(domains)
    solution = [None for i in range(size)]
    variables = set(range(size))
    values = set(range(size))
    while variables:
        variable = choice(list(variables))
        domain = domains[variable] and values
        if domain:
            value = choice(list(domain))
            variables.remove(variable)
            values.remove(value)
            solution[variable] = value
            if no_cycle:
                domains[value] -= {variable}
        else:
            raise ValueError("No quedan valores validos.")
    return tuple(solution)


if __name__ == "__main__":
    random_seed = 0
    domains = [[1, 2, 3], [0, 3], [1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
    while True:
        try:
            solution = solve(domains, random_seed=random_seed)
            break
        except ValueError:
            random_seed += 1
            pass
    print(solution)
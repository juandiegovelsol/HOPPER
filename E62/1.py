import numpy as np
import json

# Configuración de la semilla para la reproducibilidad
np.random.seed(42)

# Parámetros de las reacciones
num_reactions = 150
reactant_concentration_range = (0.01, 2)
reaction_rate_constant_range = (0.000001, 0.05)
temperature_range = (-234, 923)
catalyst_types = ['A', 'B', 'C', 'D', 'E', 'F']

# Función para calcular la velocidad de reacción usando la ecuación de la primera orden
def calculate_reaction_rate(concentration, rate_constant):
    return rate_constant * concentration

# Función para calcular la energía de activación usando la ecuación de Arrhenius
def calculate_activation_energy(temperature, rate_constant):
    # Constantes de Arrhenius (en J/mol)
    A = 8.314  # Constante de Boltzmann
    Ea_min = 40000  # Energía de activación mínima (en J/mol)
    Ea_max = 100000  # Energía de activación máxima (en J/mol)

    # Generar una distribución uniforme para la energía de activación
    activation_energy = np.random.uniform(Ea_min, Ea_max, num_reactions)
    
    # Calcular la energía de activación a la temperatura dada
    activation_energy = A * np.log(rate_constant) / temperature
    
    return activation_energy

# Función para calcular la eficiencia del catalizador
def calculate_catalyst_efficiency(rate_constant, activation_energy):
    # Fórmula arbitraria para la eficiencia del catalizador
    efficiency = 1 - (activation_energy / 100000) * rate_constant
    return efficiency

# Función para calcular el tiempo de vida media de la reacción
def calculate_half_life(rate_constant):
    return np.log(2) / rate_constant

# Generación de datos simulados
reactions_data = []

for _ in range(num_reactions):
    # Generar valores aleatorios para cada parámetro
    concentration = np.random.uniform(*reactant_concentration_range)
    rate_constant = np.random.uniform(*reaction_rate_constant_range)
    temperature = np.random.uniform(*temperature_range)
    catalyst_type = np.random.choice(catalyst_types)
    
    # Calcular los valores de las propiedades
    reaction_rate = calculate_reaction_rate(concentration, rate_constant)
    activation_energy = calculate_activation_energy(temperature, rate_constant)
    catalyst_efficiency = calculate_catalyst_efficiency(rate_constant, activation_energy)
    half_life = calculate_half_life(rate_constant)
    
    # Agregar el resultado a la lista de reacciones
    reactions_data.append({
        "reactant_concentration": concentration,
        "reaction_rate_constant": rate_constant,
        "temperature": temperature,
        "catalyst_type": catalyst_type,
        "reaction_rate": reaction_rate,
        "activation_energy": activation_energy,
        "catalyst_efficiency": catalyst_efficiency,
        "half_life": half_life
    })

# Calcular estadísticas resumidas
reaction_rates = [reaction["reaction_rate"] for reaction in reactions_data]
catalyst_efficiencies = [reaction["catalyst_efficiency"] for reaction in reactions_data]
half_lives = [reaction["half_life"] for reaction in reactions_data]

summary_statistics = {
    "reaction_rate": {
        "mean": np.mean(reaction_rates),
        "median": np.median(reaction_rates),
        "std_dev": np.std(reaction_rates)
    },
    "catalyst_efficiency": {
        "mean": np.mean(catalyst_efficiencies),
        "median": np.median(catalyst_efficiencies),
        "std_dev": np.std(catalyst_efficiencies)
    },
    "half_life": {
        "mean": np.mean(half_lives),
        "median": np.median(half_lives),
        "std_dev": np.std(half_lives)
    }
}

# Guardar los datos en un archivo JSON
output_file = 'reactions_data.json'
with open(output_file, 'w') as f:
    json.dump({
        "reactions": reactions_data,
        "summary_statistics": summary_statistics
    }, f, indent=4)

print(f"Datos generados y guardados en '{output_file}'")
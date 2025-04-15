import numpy as np
import json

# Configuración de la semilla para la reproducibilidad
np.random.seed(42)

# Rango de valores para los datos simulados
reactant_concentration_range = (0.01, 2.0)
reaction_rate_constant_range = (0.000001, 0.05)
temperature_range = (-234, 923)
catalyst_type_range = ['A', 'B', 'C', 'D', 'E', 'F']

# Generación de datos simulados para 150 reacciones químicas
num_reactions = 150
data = {
    "reactions": [],
    "summary_statistics": {
        "reaction_rate": {
            "mean": 0.0,
            "median": 0.0,
            "std_dev": 0.0
        },
        "catalyst_efficiency": {
            "mean": 0.0,
            "median": 0.0,
            "std_dev": 0.0
        },
        "half_life": {
            "mean": 0.0,
            "median": 0.0,
            "std_dev": 0.0
        }
    }
}

for _ in range(num_reactions):
    # Generación de valores aleatorios para cada parámetro
    reactant_concentration = np.random.uniform(*reactant_concentration_range)
    reaction_rate_constant = np.random.uniform(*reaction_rate_constant_range)
    temperature = np.random.uniform(*temperature_range)
    catalyst_type = np.random.choice(catalyst_type_range)

    # Cálculo de la velocidad de reacción usando la ecuación de la primera orden
    reaction_rate = reaction_rate_constant * np.exp(-reaction_rate_constant * temperature)

    # Cálculo de la energía de activación usando la ecuación de Arrhenius (ejemplo con constante A y B)
    A = 80000  # Constante preexpansiva (en J/mol)
    B = 15000  # Intercepto en el logaritmo (en J/mol)
    activation_energy = A * np.log(reaction_rate_constant) + B

    # Cálculo de la eficiencia del catalizador (ejemplo con valor arbitrario)
    catalyst_efficiency = 0.07  # Valor arbitrario para eficiencia

    # Cálculo del tiempo de vida media de la reacción
    half_life = np.log(2) / reaction_rate

    # Adición de los datos simulados a la lista de reacciones
    data["reactions"].append({
        "reactant_concentration": reactant_concentration,
        "reaction_rate_constant": reaction_rate_constant,
        "temperature": temperature,
        "catalyst_type": catalyst_type,
        "reaction_rate": reaction_rate,
        "activation_energy": activation_energy,
        "catalyst_efficiency": catalyst_efficiency,
        "half_life": half_life
    })

    # Actualización de estadísticas resumidas
    data["summary_statistics"]["reaction_rate"]["mean"] += reaction_rate
    data["summary_statistics"]["reaction_rate"]["median"] += np.median(reaction_rate)
    data["summary_statistics"]["reaction_rate"]["std_dev"] += np.std(reaction_rate)
    data["summary_statistics"]["catalyst_efficiency"]["mean"] += catalyst_efficiency
    data["summary_statistics"]["catalyst_efficiency"]["median"] += np.median(catalyst_efficiency)
    data["summary_statistics"]["catalyst_efficiency"]["std_dev"] += np.std(catalyst_efficiency)
    data["summary_statistics"]["half_life"]["mean"] += half_life
    data["summary_statistics"]["half_life"]["median"] += np.median(half_life)
    data["summary_statistics"]["half_life"]["std_dev"] += np.std(half_life)

# Restar la suma total de cada estadística para obtener las medias finales
for key in ["reaction_rate", "catalyst_efficiency", "half_life"]:
    data["summary_statistics"][key]["mean"] /= num_reactions
    data["summary_statistics"][key]["median"] /= num_reactions
    data["summary_statistics"][key]["std_dev"] /= num_reactions

# Guardar los datos en un archivo JSON
with open('simulated_reactions.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Datos simulados y estadísticas guardados en 'simulated_reactions.json'")

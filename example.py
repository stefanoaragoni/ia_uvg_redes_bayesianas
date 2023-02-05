from ia_uvg_redes_bayesianas.bayesian import Bayesian

#The format must be the following:
    # [variable | evidence, probability]
    # The evidences of each list (if they exist) must be ordered alphabetically

model = [
    ['B', 0.001],
    ['!E', 0.998],
    ['A | !B, !E', 0.001],
    ['A | B, !E', 0.94],
    ['!A | !B, E', 0.71],
    ['!A | B, E', 0.05],
    ['J | !A', 0.05],
    ['!J | A', 0.1],
    ['M | !A', 0.01],
    ['!M | A', 0.3]
]

bayes = Bayesian(model)

print("\nRed Bayesiana: ",bayes.get_string_representation())

print("\nCompletamente Observable: \t",bayes.is_fully_observed())

print("\nFactores de Probabilidad: \t")
factors = bayes.get_factors()
for factor in factors:
    print(factor, '\n')

print("\nInferencia de 'J', {'B': 1, 'E': 1}\n",bayes.get_inference('J', {'B': 1, 'E': 1}))

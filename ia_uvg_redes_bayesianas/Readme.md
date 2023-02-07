# Laboratorio 2 - Inteligencia Artificial

Este laboratorio es una implementacion de las redes bayesianas en python. La librería, con nombre Bayesian que utiliza la libería de pgmpy para poder hacer todos los análisis de las redes bayesianas.

Los métodos que se encuentran en esta librería son:

- `Constructor`: Al crear la red bayesiana es necesario enviar el modelo de la red bayesiana como el siguiente ejemplo:

model = [
        [['B', 0.001],
        ['!E', 0.998]],
        [['!A | !B, E', 0.71],
        ['!M | A', 0.3],
        ['!A | B, E', 0.05],
        ['J | !A', 0.05],
        ['M | !A', 0.01],
        ['A | !B, !E', 0.001],
        ['A | B, !E', 0.94],
        ['!J | A', 0.1]]]
        
- `create_nodes()`:  Es una función que se ejecuta dentro del constructor para poder crear todos los nodos ingresados en el constructor

- `create_edges()`:  Es una función que se ejecuta dentro del constructor para poder crear todos las relaciones entre los nodos ingresados en el constructor

- `create_cpds`:  Este método utiliza los nodos enviados como modelo para crear todas las tablas de
distribución condicional de probabilidad. El método crea la tabla para cada variable 
por medio de los datos del modelo,
permitiendo crear un objeto de tipo `TabularCPD` que se almacena en una lista de todas las tablas.

- `create_bayesian`: Se configura el objeto `BayesianNetwork` de `pgmpy`, definiendo el grafo dirigido
de la red bayesiana y las distribuciones de probabilidades condicionales creadas con `create_cpds`.

- `get_string_representation`: Devuelve una representación de las relaciones de los nodos.

- `is_fully_observed()`:  Este método toma devuleve un True o False dependiendo si la red bayesiana cumple con los requsitos de ser una red completamente observable.

- `get_factors()`:  Devuleve todo las probabilidades asociadas a cada nodo dentro de la red bayesiana.

- `get_inference(node, evidence)`:  Recibe un nodo y su evidencia para calcular una inferencia probabilistica sobre el nodo dado utilizando el algoritmo de enumeración.
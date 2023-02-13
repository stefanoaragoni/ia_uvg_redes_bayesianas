## Arquitectura

**Problema**: 
- Dada una serie de probabilidades, queremos ser capaces de construir una red bayesiana que nos permita realizar inferencias en función de lo que sabemos.

**Entrada y salida**:
- Como entrada recibimos un arreglo de arreglos en donde sabemos la probabilidad de la ocurrencia o no ocurrencia de cierto evento y la probabilidad de la ocurrencia o no ocurrencia en función de otros eventos. Esto se recibe de esta manera porque nos permite navegar de manera organizada y ligera las diferentes probabilidades a la hora de construir la red.
- Como salida tenemos el modelo de la red bayesiana con diferentes métodos incorporados que nos permite saber información de esta misma
  - Hay tres métodos que funcionan leyendo la entrada del arreglo, dos creando los nodos y ejes de la red bayesiana en función de lo que leen y un último que crea la distribución de la probabilidad condicional. Este último crea una tabla que nos permite ver todas las posibles combinaciones de probabilidad condicional.
  - Un último método de creación es utilizado para integrar las probabilidades condicionales, los nodos y los ejes en un sólo modelo de manera que este queda completo y pueda ser consultado para toda la información de la red.
  - Un método booleano es creado para indicar si la red bayesiana es completamente observable. Para esto, se compara con el largo descrito por la red como tal contra la cantidad de nodos que tienen una probabilidad condicional definida. En cuyo caso discrepe, se considera que la red no está completamente observable.
  - Existen tres métodos que devuelven información al respecto del modelo de la red. Uno de estos devuelve una representación en forma de cadenas de caracteres; una funcionalidad visual para el usuario. Otro método permite ver la probabilidad de cada uno de los nodos de la red. El último método utiliza la eliminación de variables a la hora de buscar la probabilidad de cierto evento asumiendo que ocurra otro suceso.

**Rendimiento**:
- Las inferencias son acertadas, además de que el modelo representa de manera fiel a la red bayesiana que se le es alimentada por el usuario. La exactitud que brinda esta arquitectura es alcanzada a través de las diferentes técnicas de manejo de redes bayesianas en clase.
- El tiempo de ejecución no es lento gracias a la separación de trabajos en diferentes métodos junto con uso de estructuras de datos básicas tales como arreglos. 

**Recursos**:
- Se utilizan las siguientes librerías para lograr un funcionamiento óptimo:
  - "math” se utiliza para que el límite superior de la probabilidad sea lo suficientemente alto para las diferentes iteraciones que se realizan.
  - “pgmpy” es una librería que sirve para el manejo de modelos probabilísticos, haciéndola una buena utilidad para el manejo de información en formato de arreglos, entre ellos brindando la capacidad de hacer una inferencia con el bloqueo de variables.[^1]
  - “numpy” es usada para el manejo de operaciones matemáticas entre arreglos.

[^1]:[Documentación de pgmpy](https://pgmpy.org)

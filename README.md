# Experimento Doble Rendija
>El experimento de la doble rendija fue realizado por primera vez en 1801 por Tomas Young, este comprobó un patrón de interferencias en la luz procedente de una fuente lejana al difractarse en el paso por dos rejillas. El experimento también puede realizarse con electrones, protones o neutrones, produciendo patrones de interferencia similares a los obtenidos cuando se realiza con luz.
# Materiales 🧰
1.	Papel Aluminio
2.	Bisturí
3.	Cinta adhesiva
4.	Portaobjetos de microscopio
5.	Caja de zapatos
6.	Pistola de silicona
7.	Laser
8.	Palo de valso
9.	Base para portaobjetos (Caja de Tictac)

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/WhatsApp%20Image%202022-10-04%20at%201.55.01%20PM.jpeg)
![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/WhatsApp%20Image%202022-10-04%20at%2012.41.54%20PM.jpeg)
# Procedimiento
1.	Colocamos el portaobjetos sobre el papel aluminio y cortamos un trozo a medida, posteriormente este trozo a medida es importante adherirlo con cinta al portaobjetos con el fin de que este no se mueva.
2.	Con ayuda de un bisturí hacemos dos cortes paralelos sobre el papel aluminio adherido al portaobjetos. Tenemos que asegurarnos que la distancia entre los cortes sea mínima, esto porque a la hora de apuntar con el laser el haz de luz debe poder penetrar ambas rendijas.
3.	Con ayuda de un palo de valso creamos una superficie sobre la que va a reposar el láser. Una vez creada adherimos el laser y posteriormente la estructura a la superficie.
4.	 Con ayuda de una pequeña caja de plástico creamos la base para colocar el portaobjetos; luego ponemos el portaobjetos en nuestra base, y lo adherimos a la superficie de la caja. (Es importante que al encender el laser este penetre con el haz de luz las dos rendijas del portaobjetos, se recomienda probar con diferentes posiciones para cerciorarse de que todo esté perfectamente alineado).
# Resultados

## Diseño

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/WhatsApp%20Image%202022-10-04%20at%206.01.06%20PM.jpeg)
![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/WhatsApp%20Image%202022-10-04%20at%206.01.08%20PM%20(1).jpeg)

## Experimento

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/WhatsApp%20Image%202022-10-04%20at%202.19.13%20PM.jpeg)

## ¿Cómo nos ayuda a entender el multiverso?

Este experimento es una demostración del fenómeno cuántico conocido como interferencia. Hay que tener mucho cuidado con esta palabra ya que ha sido tema de debate dentro de la comunidad científica debido a que mientras unos creen en que esta interferencia es generada entre las ondas creadas a partir de la onda original al pasar por las rendijas mientras otros creen que esta interferencia es producto del choque del mismo fotón en múltiples universos.

# Explicacion

Para explicar lo que pasa en este experimento primero debemos representarlo en una matriz.

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/matrizImaginaria.png)

En este experimento es vital el uso de imaginarios ya que gracias a ellos podemos presenciar algebraicamente el fenómeno de interferencia. 
Después de dos clics la matriz quedo de la siguiente forma:

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/matrizImaginariaDosClicks.png)

vector estado:

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/vectorEstadoImaginario.png)

Ahora hablemos de la probabilidad, como los números complejos no pueden representar probabilidades entonces debemos modificar la matriz inicial obteniendo el modulo al cuadrado de cada elemento dejando el siguiente resultado:

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/matrizProbabilistica.png)

Esta matriz muestra las probabilidades del experimento. Ya que al existir dos rendijas tienen un 50% de probabilidad de pasar por alguna de las dos, pero no sabemos por cuál de los dos pasos, mientras que al considerar que cada receptor cuenta con 3 detectores siendo este representado con el 1/3. Ya el resto de detectores tiene el 100% de probabilidad de que el fotón se quede ahí.
Después de dos clics esta matriz queda de la siguiente forma:

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/matrizProbabilisticaDosClicks.png)

Ahora al comparar ambos vectores de estado, y de sacar el módulo al cuadrado del primer vector de estado, notamos una única diferencia

![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/vectorEstadoImaginarioModuloAlCuadrado.png) ![This is an image](https://github.com/Alvaradom08/experimentoDobleRendija/blob/master/Imagenes/vectorEstadoProbabilistico.png)
En la posición 5 el primer vector de estado hay un 0 mientras que en el otro vector tiene 1/3, viéndose de forma algebraica el fenómeno de interferencia.
# Libreria 
> clonamos la librerias para su uso
## Contenido
### DobleRendija.py
la cual tiene los procedimientos necesarios para el calculo del probabilidad del experimento 
### Calculadora.py
libreria de operaciones con imaginarios y matrices
### experimento.py
Atravez de pruebas unitarias se ejecuta el experimento 
## requisitos 
incluir en sus IDE´s las librerias de :
-matplotlib.pyplot 
-numpy
# Construido con
> PyCharm 2021.2 (Community Edition)
# Autores
- Jaime Nicolas Castro Acuña https://github.com/Nicolascastro25
- Juan Mateo Alvarado Montoya https://github.com/Alvaradom08



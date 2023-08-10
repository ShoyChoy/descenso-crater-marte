# Descenso al fondo de un cráter en Marte.

En este proyecto se emplearán algoritmos de búsqueda local para encontrar una ruta de descenso por un cráter en Marte. Los algoritmos a utilizar serán el recocido simulado y la búsqueda codiciosa (o greedy).

El mapa utilizado proviene del High Resolution Imaging Science Experiment ([HiRISE](https://www.uahirise.org/dtm/) de la Universidad de Arizona y corresponde a un cráter de la superficie marciana. 

<p align="center">
  <img src="https://github.com/ShoyChoy/planeacion-ruta-a-marte/blob/main/mapa_marte.jpg" />
</p>

## Restricciones 

Un explorador como el rover perseverance no puede escalar o trepar, por lo que se consideran como navegables aquellas superficies donde el cambio de altura no sea drástico. En este caso, la altura máxima navegable es de medio metro (de diferencia entre un pixel del mapa y otro).

## Contenido

* **load_crater_data.py:** Lee el archivo del mapa y lo procesa para visualizarlo de la siguiente forma:
<p align="center">
  <img src="https://github.com/ShoyChoy/planeacion-ruta-a-marte/blob/main/mapa_marte.jpg" />
</p>
* **greedyCrater.py:** Contiene la implementación de la búsqueda codiciosa.
* **recocidoCrater.py:** Contiene la implementación del recocido simulado.

## Resultados



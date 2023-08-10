# Descenso al fondo de un cráter en Marte.

En este proyecto se emplearán algoritmos de búsqueda local para encontrar una ruta de descenso por un cráter en Marte. Los algoritmos a utilizar serán el recocido simulado y la búsqueda codiciosa (o greedy).

El mapa utilizado proviene del High Resolution Imaging Science Experiment ([HiRISE](https://www.uahirise.org/dtm/) de la Universidad de Arizona y corresponde a un cráter de la superficie marciana. 

<p align="center">
  <img src="https://github.com/ShoyChoy/descenso-crater-marte/blob/main/crater3D.jpg" />
</p>

## Restricciones 

Un explorador como el rover perseverance no puede escalar o trepar, por lo que se consideran como navegables aquellas superficies donde el cambio de altura no sea drástico. En este caso, la altura máxima navegable es de medio metro (de diferencia entre un pixel del mapa y otro).

## Contenido

* **load_crater_data.py:** Lee el archivo del mapa y lo procesa para visualizarlo de la siguiente forma:
<p align="center">
  <img src="https://github.com/ShoyChoy/descenso-crater-marte/blob/main/crater2D.jpg" />
</p>

* **greedyCrater.py:** Contiene la implementación de la búsqueda codiciosa.
* **recocidoCrater.py:** Contiene la implementación del recocido simulado.

## Resultados

Como se puede observar en el [reporte](https://github.com/ShoyChoy/descenso-crater-marte/blob/main/Descenso%20al%20fondo%20del%20crater.pdf) el algoritmo de búsqueda codiciosa no es efectivo puesto que encuentra mínimos locales muy rápido, por el otro el recocido simulado sí logra llegar al fondo del cráter. Lo anterior se debe potencialmente al relieve irregular de la superficie.

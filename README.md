# CI5438 - Proyecto 3

El objetivo de este proyecto será la implementación del algoritmo de k-means para clustering, y la evaluación del mismo en el conjunto de datos usado anteriormente, iris.csv, así como para segmentación de imágenes.

## Parte 1: Implementación

Implemente el algoritmo de k-means para clustering visto en clases, en el lenguaje de su preferencia.

## Parte 2: Iris Dataset

Utilice su implementación de k-means sobre el dataset `iris.csv`[1] usado en el Proyecto 2 y en la Tarea 2. Asegúrese de remover las clases del conjunto, dado que queremos utilizar datos no etiquetados. Haga pruebas con k=2, k=3, k=4 y k=5.

¿La separación en clusters obtenida en cada uno de los casos tiene alguna relación con las clases originales? ¿Puede hacer alguna comparación con los resultados obtenidos al entrenar clasificadores supervisados anteriormente?

## Parte 3: Segmentación de Imagenes

Cada pixel en una imagen es un punto en un espacio tridimensional, conteniendo las intensidades de los canales de rojo, azul y verde (RGB). Por lo tanto, es posible ejecutar el algoritmo de k-means para asignar cada pixel en la imagen a uno de K clusters calculados. Si hacemos entonces una transformación, reemplazando cada pixel $x_i$ por el centroide $\mu_k$ del cluster al que fue asignado, entonces estaremos dibujando una nueva versión de la imagen, ahora usando una paleta de K colores.

Seleccione dos imágenes de su preferencia, aplique el procedimiento descrito con distintos valores de $k$, y renderice la imagen resultante. Comente el resultado obtenido.

## Entrega

Para la entrega del proyecto, haga fork de este repositorio. Su repositorio deberá contener todo el código usado para el proyecto, las imágenes generadas durante la Parte 3, y un informe discutiendo los detalles de su implementación, su proceso de preprocesamiento y su proceso de entrenamiento, así como las preguntas planteadas en el enunciado. Solo se corregirán los cambios hechos hasta el día viernes 8 de diciembre de 2023, inclusive.


[1] Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.

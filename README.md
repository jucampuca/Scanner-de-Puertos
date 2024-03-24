Este es un scanner de puertos realizado con Python y Nmap.

COMENZAMOS POR IMPORTAR LAS LIBRERIAS NECESARIAS PARA HACERLO PERSONALIZADO
![image](https://github.com/jucampuca/Scanner-de-Puertos/assets/41062976/e2fc2868-8ff5-4842-81ba-babafb221508)

Importamos nmap y pyfiglet como librerías necesarias para el proyecto.
- Documentación oficial de nmap: https://nmap.org/
- Documentación oficial de pyfiglet: https://pypi.org/project/pyfiglet/

1. Luego de importar las librerias vamos a crear una función que nos permita personalizar el texto que deseamos ver en nuestro scanner
![image](https://github.com/jucampuca/Scanner-de-Puertos/assets/41062976/aea96617-5517-4693-8a4d-c5d852851303)

- Como vemos en la imágen, tenemos una función llamada print_shade().
- Creamos una variable llamada ascii_art. Esta variable la llamamos de esta manera para tener mas claro que se trata de una función que usa los caractéres ASCII para formatear nuestro texto y asi poder crear la personalización de lo que deseamos.
- Tomamos la función figlet_format para crear arte ASCII a partir de texto.
- Luego imprimimos la variable y llamamos la función.

2. Luego creamos toda la lógica de nuestro scanner.
![image](https://github.com/jucampuca/Scanner-de-Puertos/assets/41062976/da8ec547-69ad-485c-8b67-d61fa82113c4)

- Creamos las variables a usar en nuestro programa.
- La variable host para el host que queremos escanear.
- La variable nm para llamar la función PortScanner() de nmap.
- La variable puertos abiertos para ver los puertos escaneados.
- La variable count, que será nuestro contador
- La variable results, que será la variable que nos dará el resultado cuando toma la variable host como argumento.

3. Con un bucle for, vamos a recorrer los puertos encontrados e ir iterando sobre ellos para ver si estan abiertos o cerrados.
![image](https://github.com/jucampuca/Scanner-de-Puertos/assets/41062976/1e698fdf-c553-47c4-af35-bc6ec8f113e1)

Este scanner de puertos es un scanner básico y puedes ajustarlo a tus necesidades a demás de personalizarlo como tu quieras.

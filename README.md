# OPTOGESTIÓN – Sistema de Gestión de Pacientes

## 1. Descripción del proyecto

OPTOGESTIÓN es una aplicación de consola desarrollada en Python para el Centro de Atención Optométrica. Su finalidad es facilitar el registro, la consulta y la organización de la información de los pacientes atendidos durante las jornadas de atención visual.

Este proyecto fue desarrollado como trabajo final de la asignatura **Programación I**.

## 2. Requisitos del sistema

- Python 3.9 o superior.
- Visual Studio Code (recomendado).
- No requiere instalar librerías externas.

## 3. Archivos del proyecto

El proyecto está compuesto por los siguientes archivos:

- `main.py`: contiene el código fuente y las funciones del sistema.
- `pacientes.json`: almacena la información de los pacientes registrados.
- `README.md`: contiene la descripción, las instrucciones y las funcionalidades del proyecto.

## 4. Cómo ejecutar el programa

1. Abrir Visual Studio Code.
2. Seleccionar **Archivo > Abrir carpeta**.
3. Abrir la carpeta donde se encuentran los archivos del proyecto.
4. Abrir el archivo `main.py`.
5. Seleccionar **Terminal > Nuevo terminal**.
6. Ejecutar el siguiente comando:

```bash
python3 main.py
```

7. Presionar ENTER para iniciar la interacción con el menú principal.

En algunos equipos, el comando para ejecutar Python puede ser `python main.py`.

## 5. Funcionalidades del sistema

El programa cuenta con un menú principal que permite realizar las siguientes operaciones:

**1. Registrar paciente**

Permite ingresar un nuevo paciente solicitando:
- Identificador único.
- Nombre completo.
- Edad.
- Sexo.
- Uso de corrección visual.

El sistema verifica que el identificador no esté repetido, que la edad se encuentre entre 1 y 120 años y que las respuestas sean válidas.

**2. Consultar paciente**

Permite buscar un paciente mediante su identificador y visualizar toda su información registrada.

**3. Mostrar pacientes registrados**

Presenta el identificador y el nombre de los pacientes almacenados, además del número total de registros.

**4. Buscar pacientes con corrección visual**

Muestra los pacientes que utilizan corrección visual, según la información registrada en el campo `usa_correccion`.

**5. Generar estadísticas**

Calcula:
- Número total de pacientes.
- Edad promedio de los pacientes.
- Cantidad de pacientes que utilizan corrección visual.
- Cantidad de pacientes que no utilizan corrección visual.

El programa verifica que existan pacientes antes de calcular el promedio para evitar una división entre cero.

**6. Salir**

Permite finalizar la ejecución del programa conservando los registros almacenados.

## 6. Almacenamiento de información

El sistema utiliza un archivo JSON llamado `pacientes.json` para almacenar la información.

Al iniciar, el programa lee los registros existentes. Si el archivo no existe o está vacío, carga cinco pacientes ficticios de prueba.

Cuando se registra un nuevo paciente, la información se guarda automáticamente en el archivo JSON, permitiendo conservar los datos para futuras ejecuciones.

## 7. Estructura de los datos

Cada paciente se almacena como un diccionario dentro de una lista.

Ejemplo de la estructura utilizada en Python:

```python
{
    "id": "P006",
    "nombre": "Carlos Ramírez",
    "edad": 35,
    "sexo": "Masculino",
    "usa_correccion": True
}
```

En el archivo JSON, los valores booleanos se representan como `true` y `false` (en minúscula).

## 8. Conceptos de programación utilizados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Variables y tipos de datos.
- Listas y diccionarios.
- Funciones.
- Condicionales `if`, `elif` y `else`.
- Ciclos `while` y `for`.
- Validación de datos.
- Manejo de excepciones.
- Lectura y escritura de archivos.
- Manejo de información en formato JSON.

## 9. Conclusión

OPTOGESTIÓN permite organizar y administrar de manera sencilla la información de los pacientes de un centro de atención optométrica. Su desarrollo permitió aplicar los conocimientos adquiridos en Programación I mediante el uso de estructuras de datos, funciones, validaciones y almacenamiento persistente en archivos JSON.

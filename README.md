[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)](#)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/RennfahrerU/Algoritmos-de-Encriptamiento/blob/main/LICENSE)

---

# 🔐 Algoritmos de Encriptamiento

¡Bienvenido! Este proyecto es una implementación sencilla y educativa de tres algoritmos de encriptación clásicos en Python, con una interfaz web hecha con Flask: **Cifrado César**, **Transposición** y **RSA**. Perfecto para aprender sobre criptografía o experimentar con estos algoritmos.

## 📝 Descripción del proyecto

Este repositorio contiene una implementación de tres algoritmos de encriptación que son un clásico en el estudio de la criptografía:

- **Cifrado César**: Un método simple que desplaza las letras del alfabeto un número fijo de posiciones.
- **Cifrado por Transposición**: Reorganiza las letras del mensaje según una clave numérica.
- **RSA**: Famoso algoritmo de criptografía asimétrica que usa números primos grandes para proteger mensajes.

Todo esto viene con una interfaz web amigable (gracias a Flask) y una versión de consola por si lo prefieres.

## 🌟 Características
- 🛠️ Implementación de los tres algoritmos (César, Transposición y RSA).
- 🌐 Interfaz web intuitiva para cifrar y descifrar mensajes.
- ⌨️ Modo consola (CLI) para los que prefieren lo clásico.
- 🔑 Generación automática de claves para RSA.
- 🇪🇸 Soporte para el alfabeto español con la "Ñ" incluida.

## 🛠️ Cómo instalarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Algoritmos-de-Encriptamiento.git
   cd Algoritmos-de-Encriptamiento
   ```

2. Asegúrate de tener **Python 3.6** o superior:
   ```bash
   python --version
   ```

3. Instala Pipenv para gestionar las dependencias necesarias.

    ```
    pip install pipenv
    ```

3. Instala las dependencias usando **pipenv**:
   ```bash
   pipenv install
   ```

## 🚀 Cómo usarlo

### 💻 Interfaz Web 
Ejecuta la aplicación Flask:
```bash
pipenv run python app.py
```
O, si prefieres activar el entorno virtual primero:
```bash
pipenv shell
python app.py
```

Abre tu navegador en [http://localhost:5000](http://localhost:5000) y disfruta de la interfaz gráfica. Es súper fácil: elige el algoritmo, escribe tu mensaje, selecciona cifrar o descifrar, ¡y listo!

### 🖥️ Interfaz de Consola (Old School)
Si te gusta la terminal, ejecuta:
```bash
pipenv run python main.py
```

El programa te pedirá un mensaje y aplicará los tres algoritmos automáticamente. Verás el mensaje cifrado y descifrado en acción.

#### Ejemplo en consola:
```
Ingresa tu mensaje: HOLA MUNDO

Cifrado César: OWSITCULW
Descifrado César: HOLAMUNDO

Cifrado Transposición: HUONLDAOM*
Descifrado Transposición: HOLAMUNDO

Cifrado RSA: [210781516, 270112935, 1336237868...]
Descifrado RSA: HOLA MUNDO
```

## 🔍 Los algoritmos en detalle

### 1. Cifrado César
- **Archivo**: `sustitucion.py`
- **Cómo funciona**: Desplaza las letras del alfabeto (A-Z + Ñ) un número fijo de posiciones (por defecto, 8).
- **Ejemplo**:
  ```python
  mensaje = "HOLA"
  desplazamiento = 8
  cifrado = sustitucion_cifrar(mensaje, desplazamiento)
  descifrado = sustitucion_descifrar(cifrado, desplazamiento)
  ```

### 2. Cifrado por Transposición
- **Archivo**: `transposicion.py`
- **Cómo funciona**: Reorganiza las letras en una matriz según una clave (por defecto, 5 columnas). Usa `*` para rellenar si es necesario.
- **Ejemplo**:
  ```python
  mensaje = "HOLA MUNDO"
  clave = 5
  cifrado = transposicion_cifrar(mensaje, clave)
  descifrado = transposicion_descifrar(cifrado, clave)
  ```

### 3. Cifrado RSA
- **Archivo**: `RSA.py`
- **Cómo funciona**: Usa criptografía asimétrica con claves públicas y privadas. Genera claves automáticamente (por defecto, 32 bits).
- **Ejemplo**:
  ```python
  bits = 32
  e, d, n = RSA.gen_keys(bits)
  cifrado = RSA_cifrar(mensaje, e, n)
  descifrado = RSA_descifrar(cifrado, d, n)
  ```

![Captura de pantalla de la app](/screenshot.jpeg)
## 📂 Estructura del proyecto

```
Algoritmos-de-Encriptamiento/
├── app.py              # La app web con Flask
├── main.py             # La versión de consola
├── sustitucion.py      # Cifrado César
├── transposicion.py    # Cifrado por transposición
├── RSA.py              # Cifrado RSA
├── util.py             # Funciones útiles
├── static/             # Archivos CSS y otros recursos web
├── templates/          # Plantillas HTML para la web
├── Pipfile             # Dependencias
├── Pipfile.lock        # Versiones fijas de dependencias
├── README.md           # ¡Este archivo!
└── .gitignore          # Archivos que Git ignora
```

## ⚠️ Nota de seguridad
Este proyecto es **solo para aprendizaje**. Los algoritmos aquí implementados (especialmente RSA con claves de 32 bits) **NO son seguros** para uso real:
- El cifrado César y Transposición son fáciles de romper con análisis de frecuencias.
- Las claves RSA de 32 bits son extremadamente débiles.
- No usamos técnicas avanzadas como padding o salt.

Si quieres criptografía seria, ¡usa bibliotecas probadas como `cryptography` o `pycryptodome`!

## 🤝 ¿Quieres contribuir?
¡Genial! Aquí te dejo los pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu cambio: `git checkout -b mi-nueva-funcion`.
3. Haz tus cambios y haz commit: `git commit -m "Agregué algo cool"`.
4. Sube tu rama: `git push origin mi-nueva-funcion`.
5. Abre un Pull Request y comenta tus cambios.

## 📜 Licencia
Este proyecto está bajo la **Licencia MIT**. Echa un vistazo al archivo `LICENSE` para más detalles.

## 📚 Recursos útiles
- [Cifrado César - Wikipedia](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar)
- [Cifrado por Transposición - Wikipedia](https://es.wikipedia.org/wiki/Cifrado_por_transposici%C3%B3n)
- [RSA - Wikipedia](https://es.wikipedia.org/wiki/RSA)

## 👨‍💻 Sobre mí
Hecho con mucho entusiasmo por **Yilver**. ¡Espero que te sea útil!
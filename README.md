# Chatbot de la Rugby World Cup 2027 con Azure AI Language Studio

## 📌 Descripción
Este proyecto es un **chatbot** desarrollado utilizando **Azure AI Language Studio** con **Conversational Language Understanding (CLU)**. Su objetivo es responder preguntas sobre la **Rugby World Cup 2027**, proporcionando información sobre ciudades anfitrionas, clasificación, turismo y equipos participantes.

El modelo de CLU ha sido entrenado con **intents, utterances y entidades** para ofrecer respuestas precisas según la consulta del usuario.

## 🚀 Tecnologías utilizadas
- **Azure AI Language Studio** (Conversational Language Understanding)
- **Python** (Interfaz de chatbot y API de Azure)
- **Streamlit** (Interfaz de usuario para interacción con el chatbot)
- **dotenv** (Gestión de variables de entorno)

## 📂 Estructura del Proyecto
El chatbot se divide en dos archivos principales:

1. **`rugbyclu.py`** → Contiene la lógica del chatbot y la salida se muestra en **terminal**.
2. **`streamlit_chatbot.py`** → Implementación en **Streamlit** para una **interfaz web interactiva**.

## 🏗️ Definición del Modelo en Azure AI Language Studio
El modelo ha sido entrenado con los siguientes componentes:

### 1️⃣ **Intents y Utterances**
Se han definido diversos **intents** con múltiples **utterances** (ejemplos de frases que los usuarios pueden usar).

#### 📍 **Ejemplo de Intents:**
- `Clasificación al Mundial`
  - ¿Cómo se clasifican los equipos?
  - ¿Cuáles son los criterios de clasificación?
- `Ciudades Anfitrionas`
  - ¿Dónde se jugará la final?
  - ¿Qué ciudades son sede del torneo?
- `Turismo en la Mundial`
  - ¿Qué lugares turísticos hay en Sídney?
  - ¿Dónde comer en Brisbane?
- `Equipos Participantes`
  - ¿Quiénes juegan en la Copa del Mundo de Rugby 2027?
  - ¿Qué equipos están en el torneo?

### 2️⃣ **Entidades y Sinónimos**
Se han definido entidades para mejorar la precisión del modelo.

#### 📌 **Ejemplo de Entidades (Lista de Sinónimos)**
- **Ciudades**
  - `Sídney`: Sydney, capital de Nueva Gales del Sur
  - `Melbourne`: Mel, ciudad cultural
- **Equipos de Rugby**
  - `Nueva Zelanda`: All Blacks, NZ Rugby
  - `Australia`: Wallabies, equipo australiano

#### 📌 **Ejemplo de Expresiones Regulares (Regex)**
- **Fecha de Partidos:** `\d{1,2} de (enero|febrero|marzo|abril|...) de 2027`
- **Marcadores de Partido:** `\d{1,2}-\d{1,2}`

## 🔧 Instalación y Configuración

 Clona este repositorio
```bash
git clone https://github.com/anaBorja/rugbyclu2.git
```

Si clonas este repositorio, debes crear un archivo **`.env`** en la raíz con las credenciales de los recursos de Azure. Este archivo debe contener:

```plaintext
LS_CONVERSATIONS_ENDPOINT=https://tu-endpoint.cognitiveservices.azure.com/
LS_CONVERSATIONS_KEY=tu-clave-secreta
```

Antes de ejecutar el chatbot, instala las dependencias necesarias ejecutando:
```bash
pip install -r requirements.txt
```

## 🎮 Uso del Chatbot

### 🖥️ Uso en Terminal
Para ejecutar el chatbot en la **terminal**, usa:
```bash
python rugbyclu.py
```

### 🌐 Uso en Interfaz Web
Para ejecutar la versión en **Streamlit**:
```bash
streamlit run streamlit_chatbot.py
```
Esto abrirá una interfaz web donde el usuario puede escribir su pregunta y recibir respuestas en JSON con los intents detectados y entidades extraídas.

Si solo deseas interactuar con la interfaz sin ejecutar el código, accede a este enlace:
[Chatbot Rugby World Cup 2027](https://clurugby.streamlit.app/)

## 🌍 Despliegue
El chatbot ha sido desplegado para permitir interacción directa sin necesidad de instalación local.

## 📚 Más información sobre CLU
Si quieres aprender más sobre **Conversational Language Understanding (CLU)** en Azure, visita este enlace:
[Microsoft Learning - CLU](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-language-understanding.html)

---

🚀 **Este chatbot ofrece una experiencia conversacional precisa sobre la Rugby World Cup 2027 utilizando inteligencia artificial en Azure.**


import streamlit as st
import json
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
from rugbyclu import get_tourism_info, get_qualification_info, get_host_city_info, get_news, get_team_info, normalize_city_name

# Cargar variables de entorno
load_dotenv()
ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')

# Crear cliente de Azure Language Service
client = ConversationAnalysisClient(
    ls_prediction_endpoint, AzureKeyCredential(ls_prediction_key))

# Columna derecha con sugerencias de preguntas
st.sidebar.header("Ejemplos de preguntas")

# Agregar las preguntas dentro de cajitas de colores
st.sidebar.markdown("""
<div style="background-color: #ff5722; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
   <ul> 
        <li>¿Cómo se clasifican los equipos para la Rugby World Cup 2027?  </li>
        <li>¿Cuáles son los criterios de clasificación para el Mundial de Rugby 2027? </li>                      
        <li>¿Cuántos equipos participan en el torneo y cómo se definen? </li>
        <li>¿Cómo afectan las eliminatorias al ranking mundial de rugby?</li>      
    </ul>
</div>
<div style="background-color: #e67e22; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
   <ul> 
        <li>¿Cuál es la sede principal del torneo?</li>
        <li>¿Cuáles son las ciudades sede de la Rugby World Cup 2027?</li>                      
        <li>¿Cuántos estadios se usarán en la Copa del Mundo de Rugby?</li>
        <li>¿Se podrá asistir a los partidos en todas las sedes?</li>      
    </ul>
</div>
<div style="background-color: #e59866 ; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
   <ul> 
        <li>¿Dónde comer en Melbourne?</li>
        <li>¿Hay tours guiados en Townsville?</li>                      
        <li>¿Cuántos estadios se usarán en la Copa del Mundo de Rugby?</li>
        <li>¿Dónde puedo ver vida silvestre en Adelaida?</li>
        <li> ¿Cuáles son los mejores parques de Brisbane?</li>
        <li>Lugares históricos para conocer en Perth.</li>                      
        <li>Lugares turísticos recomendados en Sídney. </li>       
    </ul>
</div>
<div style="background-color: #f0b27a; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
   <ul>
        <li>¿Dónde comer en Melbourne?</li>
        <li>¿Quiénes son los jugadores clave de Nueva Zelanda? </li>                      
        <li>¿Cuántos puntos tiene Italia en la clasificación? </li>
        <li>¿En qué grupo está Sudáfrica? </li> 
    </ul>   
</div>
<div style="background-color: #f5b041; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
     <ul> 
        <li>¿Los All Blacks ya están clasificados para el torneo? </li>
        <li>¿Qué torneos dan plazas para la Copa del Mundo? </li>                      
        <li>informacion sobre el quipo de red roses </li>
        <li>¿Cuáles son los criterios para clasificar a la Rugby World Cup? </li>      
    </ul>
</div>
""", unsafe_allow_html=True)


# Configuración de la app Streamlit
st.title("Chatbot Rugby World Cup 2027")
st.write("Haz una pregunta sobre la Rugby World Cup 2027")

# Entrada del usuario
userText = st.text_input("Escribe tu pregunta:")

if st.button("Enviar consulta") and userText:
    with client:
        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "es",
                        "text": userText
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": "RugbyConversacion",
                    "deploymentName": "rugbyCLU",
                    "verbose": True
                }
            }
        )
    
    # Obtener el intent y las entidades detectadas
    top_intent = result["result"]["prediction"]["topIntent"]
    confidence = result["result"]["prediction"]["intents"][0]["confidenceScore"]
    intents = result["result"]["prediction"]["intents"]
    entities = result["result"]["prediction"]["entities"]
    regex_expressions = result["result"]["prediction"].get("regexEntities", []) 

    # Construir JSON de salida
    response_json = {
        "query": userText,
        "prediction": {
            "topIntent": top_intent,
            "projectKind": "Conversation",
            "intents": [
                {
                    "category": intent["category"],
                    "confidenceScore": intent["confidenceScore"]
                } for intent in intents
            ],
            "entities": [
                {
                    "category": entity["category"],
                    "text": entity["text"],
                    "confidenceScore": entity["confidenceScore"]
                } for entity in entities
            ],
            "regexExpressions": [
            {
                "regexKey": regex["regexKey"],
                "pattern": regex["regexPattern"],
                "language": regex["language"]
            } for regex in regex_expressions
        ]
        }
    }
    

    # Obtener expresiones regulares desde extraInformation en entidades
    regex_expressions = []
    for entity in entities:
        if "extraInformation" in entity:
            for extra in entity["extraInformation"]:
                if extra["extraInformationKind"] == "RegexKey":
                    regex_expressions.append({
                        "regexKey": extra["key"],
                        "regexPattern": extra["regexPattern"],
                        "category": entity["category"],
                        "text": entity["text"],
                        "confidenceScore": entity["confidenceScore"]
                    })

    # Mostrar el JSON completo en una caja
    #st.subheader("Respuesta en JSON")
    #st.json(response_json)
    
    # Imprimir JSON completo para depuración
    st.subheader("🔍 JSON Completo de Azure CLU")
    st.json(result)  # Esto nos permitirá ver la estructura real del JSON

    # Mostrar entidades detectadas
    st.subheader("Entidades Detectadas")
    if entities:
        for entity in entities:
            st.write(f"- **{entity['category']}**: {entity['text']} (Confianza: {entity['confidenceScore']:.2f})")
    else:
        st.write("No se detectaron entidades en la consulta.")
    
   # Mostrar expresiones regulares detectadas en la interfaz
    st.subheader("Expresiones Regulares Detectadas")
    if regex_expressions:
        for regex in regex_expressions:
            st.write(f"- **{regex['regexKey']}**: {regex['regexPattern']} (Confianza: {regex['confidenceScore']:.2f}) - Texto detectado: {regex['text']}")
    else:
        st.write("No se detectaron expresiones regulares en la consulta.")
  
    # Mostrar información relevante según el intent detectado
    st.subheader("Información Adicional")
    if top_intent == 'Turismo en la Mundial':
        city = next((entity["text"] for entity in entities if entity["category"] == "ciudades"), None)
        if city:
            st.write(get_tourism_info(city))
        else:
            st.write("No se detectó una ciudad específica en la consulta.")
    elif top_intent == 'Clasificación al Mundial':
        st.write(get_qualification_info())
    elif top_intent == 'Ciudades Anfitrionas':
        city = next((entity["text"] for entity in entities if entity["category"] == "ciudades"), None)
        city = normalize_city_name(city) if city else None
        st.write(get_host_city_info(city))
    elif top_intent == 'Equipos Participantes':
        st.write(get_team_info(entities))
    elif top_intent == 'Noticias':
        st.write(get_news())

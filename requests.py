import requests

respuesta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:latest",
        "prompt": "Hola, ¿quien eres?",
        "stream": False
    }
)
datos = respuesta.json()
print(datos["response"])
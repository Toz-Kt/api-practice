import requests

while True:
    pregunta = input("Tú: ")
    if pregunta.lower() == "exit pls":
        print("Good bye")
        continue
        respuesta = requests.post(
        "http://localhost:11434/api/generate",
        json={
        "model": "llama3.1:latest",
        "prompt": pregunta,
        "stream": False})
        datos = respuesta.json()
        print(datos["response"])
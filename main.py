from speech import listen
from commands import execute_command
from assistant import process_with_phi3

print("Jarvis запущен. Говорите...")

while True:
    text = listen()
    if not text:
        continue

    if execute_command(text):
        pass  # команда выполнена
    else:
        process_with_phi3(text)

    # Выход
    if any(word in text.lower() for word in ["стоп", "выход", "пока"]):
        print("До свидания.")
        break
    
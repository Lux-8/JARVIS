import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Подстраиваюсь под шум...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Слушаю...")

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Ничего не услышал.")
            return None

    try:
        text = r.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {text}")
        return text
    except sr.UnknownValueError:
        print("Не понял.")
        return None
    except sr.RequestError:
        print("Нет связи с Google.")
        return None
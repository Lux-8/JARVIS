import ollama
import webbrowser

def process_with_phi3(text):
    try:
        response = ollama.generate(
            model="phi3",
            prompt=f"""
Ты — голосовой помощник. Пользователь сказал: "{text}"
Если это вопрос (что такое, как сделать), верни: SEARCH: <запрос>
Если это разговор, верни: CHAT: <ответ>

Примеры:
"что такое Python?" → SEARCH: что такое Python
"привет" → CHAT: Привет! Как я могу помочь?

Ответ:
"""
        )
        reply = response['response'].strip()
        print(f"Ollama: {reply}")

        first_line = reply.split('\n')[0].strip()

        if first_line.startswith("SEARCH:"):
            query = first_line.replace("SEARCH:", "", 1).strip()
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            print(f"🔍 Ищу: {query}")

        elif first_line.startswith("CHAT:"):
            answer = first_line.replace("CHAT:", "", 1).strip()
            print(f"💬 {answer}")

        else:
            print(f"⚠️ Не понял, ищу: {text}")
            url = f"https://www.google.com/search?q={text.replace(' ', '+')}"
            webbrowser.open(url)
            print(f"🔍 Ищу: {text}")

    except Exception as e:
        print(f"Ошибка Ollama: {e}")
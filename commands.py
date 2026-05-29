from config import APP_PATHS
import webbrowser
import subprocess
import os
from utils import close_app, type_text, press_enter, clear_text

def execute_command(text):
    text = text.lower().strip()

    # 🔁 Открыть приложение?
    for name in APP_PATHS:
        if name in text:
            path = APP_PATHS[name]
            try:
                if path.startswith("http"):
                    webbrowser.open(path)
                elif os.path.exists(path) or "." in path:
                    subprocess.Popen([path])
                else:
                    os.startfile(path)
                print(f"✅ Запущено: {name}")
                return True
            except Exception as e:
                print(f"❌ Не удалось запустить {name}: {e}")
                return True

    # 🔁 Закрыть приложение?
    close_keywords = ["закрой", "закрыть", "выключи", "убей", "закрой окно"]
    for keyword in close_keywords:
        if keyword in text:
            app_name = text.replace(keyword, "").strip()
            if app_name:
                close_app(app_name)
                return True

    # 🔁 Ввести текст?
    type_keywords = ["введи", "напиши", "набери", "печатай", "впиши"]
    for keyword in type_keywords:
        if keyword in text:
            text_to_type = text.replace(keyword, "", 1).strip()
            if text_to_type:
                type_text(text_to_type)
                return True

    # 🔁 Нажать Enter?
    if any(word in text for word in ["нажми enter", "отправь", "энтер", "отправить"]):
        press_enter()
        return True

    # 🔁 Очистить поле?
    if any(word in text for word in ["очисти", "стереть", "удали текст"]):
        clear_text()
        return True

    return False
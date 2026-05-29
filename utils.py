import pygetwindow as gw
import pyautogui
import time

# === Закрытие окна по названию ===
def close_app(app_name):
    try:
        windows = gw.getWindowsWithTitle("")
        closed = False
        for win in windows:
            if app_name.lower() in win.title.lower():
                win.close()
                print(f"❌ Окно '{win.title}' закрыто.")
                closed = True
        if not closed:
            print(f"Окно с названием '{app_name}' не найдено.")
    except Exception as e:
        print(f"Ошибка при закрытии окна: {e}")

# === Ввод текста без Enter ===
def type_text(text):
    time.sleep(0.5)
    pyautogui.typewrite(text, interval=0.05)
    print(f"⌨️ Напечатано: '{text}'")

# === Нажать Enter ===
def press_enter():
    pyautogui.press('enter')
    print("↩️ Нажат Enter")

# === Очистить поле ===
def clear_text():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    print("🧹 Поле очищено")
import pytesseract
import os
import pinyin
import keyboard
import pyperclip
import threading

from PIL import ImageGrab, Image

def ocr():
    pyperclip.copy('')
    m = 0
    while m == 0:
        try:
            im = ImageGrab.grabclipboard()
            im.save('temp.png','PNG')
            print("[+] Translating Image...")
            imgrey = im.convert('L')
            #imgrey.show()
            text = pytesseract.image_to_string(Image.open('temp.png'), lang='chi_sim')
            print("===================================================")
            print(pinyin.get(text), end='')
            print(text, end='')
            print("===================================================")
            m = 1
            pyperclip.copy('')
        except AttributeError:
            pass

def listener():
    print("[+] Go ahead, I'm listening...")
    keyboard.add_hotkey('win+shift+s', ocr)

    try:
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.remove_all_hotkeys()
        print("[+] Stopping listener.")

if __name__ == "__main__":
    k_thread = threading.Thread(target=listener)
    k_thread.start()
import pytesseract
import os
import pinyin
import keyboard
import pyperclip

from PIL import ImageGrab, Image

def ocr():
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
            pyperclip.copy('')
            m = 1
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            pass

print("[+] Go ahead, I'm listening...")
keyboard.add_hotkey("win+shift+s", ocr)
keyboard.wait()

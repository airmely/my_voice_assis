import os
from datetime import datetime


def off_computer():
    if os.name == "nt":   # Для Windows
        os.system("shutdown /s /f /t 0")

    else:
        print("Не удалось определить операционную систему.")


now = datetime.now().strftime('%I:%M %p')
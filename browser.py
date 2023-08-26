import webbrowser


def open_browser():
    webbrowser.open('https:/mail.ru')
    return 'Открываю'


def search_in_browser(query):
    query = query.replace("загугли", "").strip()
    search_url = f"https://ya.ru/search/?text={query}"
    webbrowser.open(search_url)
    return f'Ищу {query}'


def on_music():
    webbrowser.open("https://music.yandex.ru/neuromusic")
    return 'Включаю'
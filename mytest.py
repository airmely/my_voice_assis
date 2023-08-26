from gtts import gTTS

text = "Привет! Я ваш голосовой помощник."
tts = gTTS(text, lang="ru", slow=False)  # Здесь вы можете настроить язык и скорость
tts.save("output.mp3")  # Сохраняем сгенерированный голос в файл
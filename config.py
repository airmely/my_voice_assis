import openai
import decouple


openai.api_key = decouple.config('API_KEY')
db_password = decouple.config('DB_PASSWORD')


def dialog_with_chatgpt(message):
    message = message.replace("давай поговорим", "").strip()

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=1500,
    )

    return response['choices'][0]['text']

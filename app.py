import os
import openai
import re
import readline

openai.api_key = os.environ["OPENAI_API_KEY"]


def random_words():
    print("Generating now")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "いくつかの日本語のでたらめな文章を要素とする一つのpythonの配列を作ってください。"},
        ],
    )
    response = response.choices[0]["message"]["content"]
    formatted = re.sub('\n', "", response)
    if re.match('.*\[', formatted):
        string = re.search('\[.*\]', formatted).group()
        return eval(string)
    else:
        print("ChatGPTを用いた生成に失敗しました。")
        random_words()


while True:
    words_array = random_words()
    for i in words_array:
        print("Type this!!: {}".format(i))
        while True:
            user_input = input(">> ")
            if i == user_input:
                print("Succeeded!!\n")
                break
            else:
                print("\nDoes not match!! Type again!!: {}".format(i))


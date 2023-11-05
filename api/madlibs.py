import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_madlibs_template():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": "Design a short story that has blanks where key words will be placed. For each blank, specify the type of word required (e.g., noun, verb, adjective, etc.). The story should be coherent but leave room for a wide range of word choices that could make the final story humorous or absurd."
        }
      ],
      temperature=1
    )
    return response['choices'][0]['message']['content'].strip()


def extract_words_in_brackets(input_string):
    import re
    words = re.findall(r'\[(.*?)\]', input_string)
    for word in words:
        input_string = input_string.replace('['+word+']', '')
    return ', '.join(words)

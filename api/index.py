from flask import Flask
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/api/madlibs", methods=['GET'])
def return_madlibs_json():
    json = curate_madlibs()
    json['status'] = 'success'
    json['message'] = 'MadLibs story template'
    return json


@app.route("/api/test", methods=['GET'])
def test_flask():
    return {'status': 'success', 'message': 'test'}


def generate_madlibs_story():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",  # too slow ! 
      messages=[
        {
            "role": "user",
            "content": (
                "Design a short story that has blanks where key words will be "
                " placed. For each blank, specify the type of word required "
                "(e.g., noun, verb, adjective, etc.) in square brackets. The story should be "
                "coherent but leave room for a wide range of word choices "
                "that could make the final story humorous or absurd."
                )
        }
      ],
      temperature=1,
      max_tokens=250
    )
    return response['choices'][0]['message']['content'].strip()


def generate_madlibs_story_davinci():
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=(
          "Write a fun and silly story for kids."
          "It should be at least 10 sentences long, with at most 2 blanks per sentence."
          "Then, remove key words from the story, replacing them with blanks."
          "For each blank, specify the category of word required (e.g., proper noun, verb, adjective, etc.) in square brackets."
          "The story should be coherent but leave room for a wide range of word choices "
          "that could make the final story humorous or absurd."
      ),
      temperature=1,
      max_tokens=300
    )
    return response['choices'][0]['text'].strip()


def extract_words_in_brackets(input_string):
    import re
    if '[' in input_string:
        words = re.findall(r'\[(.*?)\]', input_string)
        for word in words:
            input_string = input_string.replace('['+word+']', '_')
    return input_string, ', '.join(words)


def curate_madlibs():
    story = generate_madlibs_story_davinci()  # generate_madlibs_story()
    story, blanks = extract_words_in_brackets(story)
    return {'story': story, 'blanks': blanks}


if __name__ == '__main__':
    app.run(port=5328)
    
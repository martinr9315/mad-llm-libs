import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_madlibs_story():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
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
          "Write a fun and silly story for kids that has blanks where key words will be placed."
          "It should be at least 5 sentences long, with at most 2 blanks per sentence."
          "For each blank, specify the type of word required (e.g., noun, verb, adjective, etc.) in square brackets."
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

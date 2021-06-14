import json
import os


class MadLibs:
    def __init__(self, word_descriptions, template) -> None:
        self.template = template
        self.word_descriptions = word_descriptions

    def get_words_from_user(self):
        words = []
        print("Please provide the following words: ")
        for desc in self.word_descriptions:
            user_input = input(desc + " ")
            words.append(user_input)
        return words

    @classmethod
    def from_json(cls, name="day_at_the_zoo.json", path="./templates"):
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_libs = cls(**data)
        return mad_libs

    def build_story(self):
        words = self.get_words_from_user()
        story = self.template.format(*words)
        return story

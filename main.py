menu_dict = {
    "1": "MadLibs",
    "2": "Number guessing",
    "3": "Rock paper scissors"
}

dict_keys = {
    "madlib" : "1",
    "guessing": "2",
    "rock_paper_scissor": "3"
}

def menu(menu_dict):
    user_choice = ""
    dict_keys = menu_dict.keys()
    for key, value in menu_dict.items():
        print(f"{key} _ {value}")
    while user_choice not in dict_keys:
        user_choice = input("Choose one ")
    return user_choice


def main():
    user_choice = menu(menu_dict)
    if user_choice == dict_keys["madlib"]:
        from models.MadLibs import MadLibs
        mad_libs = MadLibs.from_json()
        print(mad_libs.build_story())
    elif user_choice == dict_keys["guessing"]:
        from models.NumberGuessing import NumberGuessing
        number_guessing = NumberGuessing.guess()
        number_guessing.play()
    elif user_choice == dict_keys["rock_paper_scissor"]:
        from models.RockPaperScissor import RockPaperScissor
        rock_paper_scissor = RockPaperScissor()
        print(rock_paper_scissor.play())
main()

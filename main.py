from models.MadLibs import MadLibs

mad_libs = MadLibs.from_json()
print(mad_libs.build_story())
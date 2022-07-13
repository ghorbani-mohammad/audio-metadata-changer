import os
import eyed3

path = input("Please enter path of mp3 directory: ")
files = os.listdir(path)
eyed3.log.setLevel("ERROR")


for file in files:
    ext = file.split(".")[-1]
    audio_file = eyed3.load(path + file)
    os.rename(path + file, path + f"{audio_file.tag.title}.{ext}")

# License: MIT License
# Author: lazy fox chan
# Convert emoji list from opencc project repo
import urllib.request
import opencc


EMOJI_CATEGORY_URL = "https://github.com/rime/rime-emoji/raw/master/opencc/emoji_category.txt"
EMOJI_WORD_URL = "https://github.com/rime/rime-emoji/raw/master/opencc/emoji_word.txt"
EMOJI_CATEGORY_ORIG_FILE_NAME = "emoji_category.txt.orig"
EMOJI_WORD_ORIG_FILE_NAME = "emoji_word.txt.orig"
EMOJI_CATEGORY_FILE_NAME = "emoji_category_tongpin.txt"
EMOJI_WORD_FILE_NAME = "emoji_word_tongpin.txt"


# Download
print("Start download: " + EMOJI_CATEGORY_URL)
urllib.request.urlretrieve(EMOJI_CATEGORY_URL, EMOJI_CATEGORY_ORIG_FILE_NAME)
print("Download complete: " + EMOJI_CATEGORY_ORIG_FILE_NAME)
print("Start download: " + EMOJI_WORD_URL)
urllib.request.urlretrieve(EMOJI_WORD_URL, EMOJI_WORD_ORIG_FILE_NAME)
print("Download complete: " + EMOJI_WORD_ORIG_FILE_NAME)


# Load files
emoji_category_input_file = open(EMOJI_CATEGORY_ORIG_FILE_NAME, "r", encoding="utf-8")
emoji_word_input_file = open(EMOJI_WORD_ORIG_FILE_NAME, "r", encoding="utf-8")

emoji_category_tmp = emoji_category_input_file.read()
emoji_word_tmp = emoji_word_input_file.read()

emoji_category_input_file.close()
emoji_word_input_file.close()


# Convert format
converter = opencc.OpenCC('s2twp.json')

emoji_category = ""
for line in emoji_category_tmp.splitlines():
    converted = converter.convert(line)
    if line.split("\t")[0] == converted.split("\t")[0]:
        emoji_category = emoji_category + converted + "\n"
    else:
        emoji_category = emoji_category + converted + "\n"
        emoji_category = emoji_category + line + "\n"
emoji_word = ""
for line in emoji_word_tmp.splitlines():
    converted = converter.convert(line)
    if line.split("\t")[0] == converted.split("\t")[0]:
        emoji_word = emoji_word + converted + "\n"
    else:
        emoji_word = emoji_word + converted + "\n"
        emoji_word = emoji_word + line + "\n"


# Output files
emoji_category_output_file = open(EMOJI_CATEGORY_FILE_NAME, "w", encoding="utf-8")
emoji_word_output_file = open(EMOJI_WORD_FILE_NAME, "w", encoding="utf-8")

emoji_category_output_file.write(emoji_category)
emoji_word_output_file.write(emoji_word)

emoji_category_output_file.close()
emoji_word_output_file.close()


print("DONE!")

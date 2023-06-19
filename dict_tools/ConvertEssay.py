# License: MIT License
# Author: lazy fox chan
# Convert essay from McBopomofo project repo and CC-CEDICT
import urllib.request
import zipfile
import re


PHRASE_URL = "https://github.com/openvanilla/McBopomofo/raw/master/Source/Data/phrase.occ"
PHRASE_FILE_NAME = "phrase.occ"
CEDICT_URL = "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip"
CEDICT_ZIP_FILE_NAME = "cedict_1_0_ts_utf-8_mdbg.zip"
CEDICT_FILE_NAME = "cedict_ts.u8"
OUTPUT_FILE_NAME = "essay_tongpin.txt"
essay_list = []


def add_one(arg_str):
    return str(int(arg_str) + 1)


def remove_duplicates(arg_list):
    return_list = []
    tmp_dict = {}

    # Get maximum value
    for input_list_line in arg_list:
        key = input_list_line[0]
        if key not in tmp_dict.keys():
            tmp_dict[key] = input_list_line[1]
            continue
        if int(tmp_dict[key]) < int(input_list_line[1]):
            tmp_dict[key] = input_list_line[1]

    # Create list
    for input_list_line in arg_list:
        key = input_list_line[0]
        if key not in tmp_dict.keys():
            continue
        return_list.append([input_list_line[0], tmp_dict[key]])
        del tmp_dict[key]

    return return_list


# Download
print("Start download: " + PHRASE_URL)
urllib.request.urlretrieve(PHRASE_URL, PHRASE_FILE_NAME)
print("Download complete: " + PHRASE_FILE_NAME)

print("Start download: " + CEDICT_URL)
urllib.request.urlretrieve(CEDICT_URL, CEDICT_ZIP_FILE_NAME)
print("Download complete: " + CEDICT_ZIP_FILE_NAME)
with zipfile.ZipFile(CEDICT_ZIP_FILE_NAME) as zf:
    zf.extract(CEDICT_FILE_NAME)


# Load McBopomofo phrase file
phrase_input_file = open(PHRASE_FILE_NAME, "r", encoding="utf-8")
for line in phrase_input_file:
    line = line.replace("  ", "\t").replace("\n", "")
    word = line.split("\t")
    essay_list.append([word[0], add_one(word[1])])
phrase_input_file.close()


# Load CEDICT file
cedict_input_file = open(CEDICT_FILE_NAME, "r", encoding="utf-8")
for line in cedict_input_file:
    word = line.split(" ")[0]
    if len(word) != 1 and not(bool(re.search("([0-9]|[a-zA-Z]|#|!)", word))):
        if "，" in word:
            for divided_word in word.split("，"):
                essay_list.append([divided_word, "0"])
        elif "·" in word:
            for divided_word in word.split("·"):
                essay_list.append([divided_word, "0"])
        else:
            essay_list.append([word, "0"])
cedict_input_file.close()


# Remove duplicates (keep maximum score)
essay_list = remove_duplicates(essay_list)


# Output files
output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf-8")
for line in essay_list:
    output_file.write(line[0] + "\t" + line[1] + "\n")
output_file.close()


print("DONE!")

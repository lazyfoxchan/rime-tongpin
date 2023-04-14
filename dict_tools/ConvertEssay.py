# License: GNU Lesser General Public License v3.0
# Author: lazy fox chan
# Convert dict from essay project repo
import urllib.request
import zipfile
import opencc
import re


ESSAY_URL = "https://github.com/rime/rime-essay/raw/master/essay.txt"
ESSAY_ORIG_FILE_NAME = "essay.txt.orig"
ESSAY_FILE_NAME = "essay_tongpin.txt"
CEDICT_URL = "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip"
CEDICT_ZIP_FILE_NAME = "cedict_1_0_ts_utf-8_mdbg.zip"
CEDICT_FILE_NAME = "cedict_ts.u8"
ESSAY_EX_FILE_NAME = "tongpin.essayex.dict.yaml"
ESSAY_EX_FILE_HEADER = \
"""# Rime dictionary
# encoding: utf-8

---
name: tongpin.essayex
version: "1.0"
sort: by_weight
use_preset_vocabulary: false
...

"""


def remove_duplicates(arg_list):
    return_list = []
    tmp_dict = {}

    for input_list_line in arg_list:
        key = input_list_line[0]
        if key not in tmp_dict.keys():
            tmp_dict[key] = input_list_line[1]
            continue
        if int(tmp_dict[key]) < int(input_list_line[1]):
            tmp_dict[key] = input_list_line[1]

    for input_list_line in arg_list:
        key = input_list_line[0]
        if key not in tmp_dict.keys():
            continue
        return_list.append([input_list_line[0], tmp_dict[key]])
        del tmp_dict[key]

    return return_list


# Download
print("Start download: " + ESSAY_URL)
urllib.request.urlretrieve(ESSAY_URL, ESSAY_ORIG_FILE_NAME)
print("Download complete: " + ESSAY_ORIG_FILE_NAME)
print("Start download: " + CEDICT_URL)
urllib.request.urlretrieve(CEDICT_URL, CEDICT_ZIP_FILE_NAME)
print("Download complete: " + CEDICT_ZIP_FILE_NAME)
with zipfile.ZipFile(CEDICT_ZIP_FILE_NAME) as zf:
    zf.extract(CEDICT_FILE_NAME)


# Load essay file
essay_input_file = open(ESSAY_ORIG_FILE_NAME, "r", encoding="utf-8")
essay_tmp = essay_input_file.read()
essay_input_file.close()


# Convert by OpenCC
converter = opencc.OpenCC('s2twp.json')
essay_tmp2_list = []
before_list = {}
for line in essay_tmp.splitlines():
    word = line.split("\t")[0]
    score = line.split("\t")[1]
    converted = converter.convert(word)
    if word == converted:
        essay_tmp2_list.append([word, str(int(score) + 1)])
    else:
        essay_tmp2_list.append([converted, str(int(score) + 1)])
        essay_tmp2_list.append([word, score])
        before_list[word] = None


# Set the score of OpenCC word to 0
essay_list = []
for line in essay_tmp2_list:
    if line[0] in before_list:
        essay_list.append([line[0], "0"])
    else:
        essay_list.append([line[0], line[1]])


# Load CEDICT file and marge list
cedict_list = []
cedict_input_file = open(CEDICT_FILE_NAME, "r", encoding="utf-8")
for line in cedict_input_file:
    word = line.split(" ")[0]
    if len(word) != 1 and not(bool(re.search("([0-9]|[a-zA-Z]|#|!)", word))):
        if "，" in word:
            for divided_word in word.split("，"):
                cedict_list.append([divided_word, "0"])
        elif "·" in word:
            for divided_word in word.split("·"):
                cedict_list.append([divided_word, "0"])
        else:
            cedict_list.append([word, "0"])
cedict_input_file.close()
essay_list = essay_list + cedict_list


# Remove duplicates (keep maximum score)
essay_list = remove_duplicates(essay_list)


# Add 不 and 一 variation
variation_list = []
for line in essay_list:
    if line[0] == "不":
        variation_list.append(["不", "bu2", str(int(line[1]) - 1)])
    if line[0] == "一":
        variation_list.append(["一", "yi2", str(int(line[1]) - 1)])


# File output
essay_output_file = open(ESSAY_FILE_NAME, "w", encoding="utf-8")
for line in essay_list:
    essay_output_file.write(line[0] + "\t" + line[1] + "\n")
essay_output_file.close()

essay_ex_output_file = open(ESSAY_EX_FILE_NAME, "w", encoding="utf-8")
essay_ex_output_file.write(ESSAY_EX_FILE_HEADER)
for line in variation_list:
    essay_ex_output_file.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\n")
essay_ex_output_file.close()


print("DONE!")

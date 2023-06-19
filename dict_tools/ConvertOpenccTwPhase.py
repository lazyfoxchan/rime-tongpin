# License: MIT License
# Author: lazy fox chan
# Convert TWPhrases lists from opencc project repo
import urllib.request
import opencc


IT_URL = "https://github.com/BYVoid/OpenCC/raw/master/data/dictionary/TWPhrasesIT.txt"
NAME_URL = "https://github.com/BYVoid/OpenCC/raw/master/data/dictionary/TWPhrasesName.txt"
OTHER_URL = "https://github.com/BYVoid/OpenCC/raw/master/data/dictionary/TWPhrasesOther.txt"
IT_ORIG_FILE_NAME = "TWPhrasesIT.txt.orig"
NAME_ORIG_FILE_NAME = "TWPhrasesName.txt.orig"
OTHER_ORIG_FILE_NAME = "TWPhrasesOther.txt.orig"
IT_FILE_NAME = "TWPhrasesIT_tongpin.txt"
NAME_FILE_NAME = "TWPhrasesName_tongpin.txt"
OTHER_FILE_NAME = "TWPhrasesOther_tongpin.txt"


# Download
print("Start download: " + IT_URL)
urllib.request.urlretrieve(IT_URL, IT_ORIG_FILE_NAME)
print("Download complete: " + IT_ORIG_FILE_NAME)
print("Start download: " + NAME_URL)
urllib.request.urlretrieve(NAME_URL, NAME_ORIG_FILE_NAME)
print("Download complete: " + NAME_ORIG_FILE_NAME)
print("Start download: " + OTHER_URL)
urllib.request.urlretrieve(OTHER_URL, OTHER_ORIG_FILE_NAME)
print("Download complete: " + OTHER_ORIG_FILE_NAME)


# Load files
it_input_file = open(IT_ORIG_FILE_NAME, "r", encoding="utf-8")
name_input_file = open(NAME_ORIG_FILE_NAME, "r", encoding="utf-8")
other_input_file = open(OTHER_ORIG_FILE_NAME, "r", encoding="utf-8")

it_tmp = it_input_file.read()
name_tmp = name_input_file.read()
other_tmp = other_input_file.read()

it_input_file.close()
name_input_file.close()
other_input_file.close()


# Convert format
converter = opencc.OpenCC('t2tw.json')

it = ""
for line in it_tmp.splitlines():
    converted = converter.convert(line)
    if line.split("\t")[0] == converted.split("\t")[0]:
        it = it + converted + " " + converted.split("\t")[0] + "\n"
    else:
        it = it + converted + " " + converted.split("\t")[0] + "\n"
        it = it + line + " " + line.split("\t")[0] + "\n"
name = ""
for line in name_tmp.splitlines():
    converted = converter.convert(line)
    if line.split("\t")[0] == converted.split("\t")[0]:
        name = name + converted + " " + converted.split("\t")[0] + "\n"
    else:
        name = name + converted + " " + converted.split("\t")[0] + "\n"
        name = name + line + " " + line.split("\t")[0] + "\n"
other = ""
for line in other_tmp.splitlines():
    converted = converter.convert(line)
    if line.split("\t")[0] == converted.split("\t")[0]:
        other = other + converted + " " + converted.split("\t")[0] + "\n"
    else:
        other = other + converted + " " + converted.split("\t")[0] + "\n"
        other = other + line + " " + line.split("\t")[0] + "\n"


# Output files
it_output_file = open(IT_FILE_NAME, "w", encoding="utf-8")
name_output_file = open(NAME_FILE_NAME, "w", encoding="utf-8")
other_output_file = open(OTHER_FILE_NAME, "w", encoding="utf-8")

it_output_file.write(it)
name_output_file.write(name)
other_output_file.write(other)

it_output_file.close()
name_output_file.close()
other_output_file.close()


print("DONE!")

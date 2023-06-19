# License: MIT License
# Author: lazy fox chan
# Convert dict from McBopomofo project repo
import urllib.request
import convrules
import re


BPM_BASE_URL= "https://github.com/openvanilla/McBopomofo/raw/master/Source/Data/BPMFBase.txt"
BPM_BASE_FILE_NAME = "BPMFBase.txt"
BPM_MAPPINGS_URL= "https://github.com/openvanilla/McBopomofo/raw/master/Source/Data/BPMFMappings.txt"
BPM_MAPPINGS_FILE_NAME = "BPMFMappings.txt"

OUTPUT_FILE_NAME = "tongpin.McBopomofo.dict.yaml"
OUTPUT_FILE_HEADER = \
"""# Rime dictionary
# encoding: utf-8
#
# This file was converted from the McBopomofo project
# https://github.com/openvanilla/McBopomofo/blob/master/LICENSE.txt
## 
## MIT License
## 
## Copyright (c) 2011-2023 Mengjuei Hsieh et al.
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

---
name: tongpin.McBopomofo
version: "1.0"
sort: by_weight
use_preset_vocabulary: false
...

"""
bpm_list = []


def jhuyin2tongpin(arg_list):
    return_list = []

    for word in arg_list:
        tongpin = word[1]
        # Convert 注音一式 to 華語通用拼音
        for convert_rule in convrules.CONVERT_RULES:
            tongpin = tongpin.replace(convert_rule[0], convert_rule[1])

        # Skip bad data
        if bool(re.search(convrules.JHUYIN_REGEXP, word[0])) or bool(re.search(convrules.JHUYIN_REGEXP, tongpin)):
            print("Skip: " + word[0] + "  " + word[1])
            continue

        return_list.append([word[0], tongpin])

    return return_list


# Download
print("Start download: " + BPM_BASE_URL)
urllib.request.urlretrieve(BPM_BASE_URL, BPM_BASE_FILE_NAME)
print("Download complete: " + BPM_BASE_FILE_NAME)

print("Start download: " + BPM_MAPPINGS_URL)
urllib.request.urlretrieve(BPM_MAPPINGS_URL, BPM_MAPPINGS_FILE_NAME)
print("Download complete: " + BPM_MAPPINGS_FILE_NAME)


# Load McBopomofo files
input_file = open(BPM_BASE_FILE_NAME, "r", encoding="utf-8")
for line in input_file:
    line = line.replace("\n", "")
    word = line.split(" ")
    bpm_list.append([word[0], word[1]])
input_file.close()

input_file = open(BPM_MAPPINGS_FILE_NAME, "r", encoding="utf-8")
for line in input_file:
    line = line.replace("\n", "")
    word = line.split(" ", 1)
    bpm_list.append([word[0], word[1]])
input_file.close()


# 注音一式 -> 華語通用拼音
bpm_list = jhuyin2tongpin(bpm_list)


# Output files
output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf-8")
output_file.write(OUTPUT_FILE_HEADER)
for word in bpm_list:
    output_file.write(word[0] + "\t" + word[1] + "\n")
output_file.close()


print("DONE!")

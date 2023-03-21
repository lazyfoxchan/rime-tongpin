# License: GNU Lesser General Public License v3.0
# Author: lazy fox chan
import convcommon


OUTPUT_FILE_NAME = "tongpin.revised.dict.yaml"
OUTPUT_FILE_HEADER = \
"""# Rime dictionary
# encoding: utf-8
#
# IMPORTANT:
# The dictionary YOU converted (重編國語辭典修訂本) is licensed under CC BY-NC-ND 3.0 TW by Taiwanese Ministry of Education.
# This modified file can ONLY be used for private use.
# https://creativecommons.org/licenses/by-nc-nd/3.0/tw/
#

---
name: tongpin.revised
version: "1.0"
sort: by_weight
use_preset_vocabulary: false
...

"""


def convert(df):
    """Convert 重編國語辭典修訂本. no return.

    Args:
        df (pandas.core.frame.DataFrame): 重編國語辭典修訂本 pandas.core.frame.DataFrame
    """
    # Get data from excel DataFrame
    word_list = get_dict_data(df)

    # convert 注音一式 to 通用拼音
    word_list = convcommon.jhuyin2tongpin(word_list)

    # Write dict file
    output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf-8")
    output_file.write(OUTPUT_FILE_HEADER)
    for word in word_list:
        output_file.write(word[0] + "\t" + word[1] + "\n")
    output_file.close()


def get_dict_data(df):
    """Get words data from excel DataFrame

    - Get 字詞名 and 注音一式
    - Get the correct 注音一式 of 異體字
    - Split idioms
    - Remove bad data

    Args:
        df (pandas.core.frame.DataFrame): 重編國語辭典修訂本 pandas.core.frame.DataFrame
    Returns:
        list: [[字詞名, 注音一式], [字詞名, 注音一式]...]
    """
    csv_data_list = []
    yitizih_data_list = []
    return_list = []

    # Get 字詞名 and 注音一式 (except 異體字)
    for data in df.itertuples():
        csv_data_list.append([data.字詞名, data.注音一式])

    # Get 異體字 and 注音一式
    for data in df.itertuples():
        if "」的異體字。" in data.釋義:
            jhengti = data.釋義.replace("「", "").replace("」的異體字。", "")  # Get 正字
            for word in csv_data_list:
                if word[0] == jhengti:
                    yitizih_data_list.append([data.字詞名, word[1]])

    # Marge 異體字
    for yitizih_data in yitizih_data_list:
        csv_data_list.append(yitizih_data)

    # Remove bad data and split idioms
    for word in csv_data_list:
        # Remove no 注音一式 data
        if type(word[1]) == float:
            continue
        # Remove not unicode data
        if ".gif" in word[0]:
            continue
        # Split containing 「，」 words
        if "，" in word[0]:
            word_name_list = word[0].split("，")
            jhuyin_list = word[1].split("　，　")
            for i in range(len(word_name_list)):
                return_list.append([word_name_list[i], jhuyin_list[i]])
        else:
            return_list.append(word)

    return return_list

# License: GNU Lesser General Public License v3.0
# Author: lazy fox chan
import convrules


def jhuyin2tongpin(arg_list):
    """Convert 注音一式 to 通用拼音 in list

    Args:
        arg_list (list): [[字詞名, 注音一式], [字詞名, 注音一式]...]
    Returns:
        list: [[字詞名, 通用拼音], [字詞名, 通用拼音]...]
    """
    return_list = []

    for word in arg_list:
        tongpin = word[1]
        # fix 兒化音
        try:
            if tongpin[-1] == "ㄦ" and tongpin[-2] != " ":
                tongpin = tongpin[:-1] + " ㄦ"
        except IndexError:
            pass
        # Convert 注音一式 to 通用拼音
        for convert_rule in convrules.CONVERT_RULES:
            tongpin = tongpin.replace(convert_rule[0], convert_rule[1])
        return_list.append([word[0], tongpin])

    return return_list

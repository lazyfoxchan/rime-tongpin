# rime-tongpin
Tongyong Pinyin schema for Rime IME.  
中州韻輸入法引擎華語通用拼音方案。  

# Function
* Display tones hint
* Display Taiwanese Mandarin hints
* Convert to emoji
* Output 臺灣正體/台灣民間字體/日本新字体/简体
* Input tones using only 26 keys
  * `q` = `1st tone`
  * `x` = `2nd tone`
  * `qq` = `3rd tone`
  * `xx` = `4th tone`
  * `v` = `5th tone`

## How to install
IMPORTANT:  
For licensing reasons, This repository cannot distribute converted dictionary files. Users must convert the dictionary files from 教育部國語辭典 on the userself computer.

### How to convert dictionary files

#### Dependencies
* Python3
  * pandas
  * openpyxl
  * xlrd  
    ```
    pip install pandas openpyxl xlrd
    ```

#### Need files 
1. Clone or download this repository.
2. Copy the following files into the `convert_dict` directory:
    * `dict_revised_2015_XXXXXXXX.xlsx` in `dict_revised_2015_XXXXXXXX.zip`
      * [DL link](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_reviseddict_download.html)
    * `dict_concised_2014_XXXXXXXX.xlsx` in `dict_concised_2014_XXXXXXXX.zip`
      * [DL link](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_concised_download.html)
    * `dict_idioms_2020_XXXXXXXX.xls` in `dict_idioms_2020_XXXXXXXX.zip`
      * [DL link](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_idiomsdict_download.html)

    IMPORTANT:  
    These files(教育部國語辭典) are licensed under [CC BY-NC-ND 3.0 TW](https://creativecommons.org/licenses/by-nd/3.0/tw/) by Taiwanese Ministry of Education. If you convert these files, you may use them for private use only.

#### Convert
```
$ cd {$YOUR DIRECTORY}/rime-tongpin/convert_dict/
$ python ConvertDict.py ./dict_revised_2015_XXXXXXXX.xlsx ./dict_concised_2014_XXXXXXXX.xlsx ./dict_idioms_2020_XXXXXXXX.xls
```

### Load schema
1. Install [Rime IME](https://rime.im/download/)
2. Copy the following files into the Rime IME user directory in your environment:  
    * opencc/*
    * essay_tongpin.txt
    * tongpin.schema.yaml
    * tongpin.dict.yaml
    * tongpin.user.dict.yaml
    * tongpin.essayex.dict.yaml
    * tongpin.revised.dict.yaml (you converted)
    * tongpin.concised.dict.yaml (you converted)
    * tongpin.idioms.dict.yaml (you converted)
3. After copying the files, need to redeploy.

## License
Author: lazy fox chan  
License: [GNU Lesser General Public License v3.0](https://github.com/lazyfoxchan/rime-tongpin/blob/master/LICENSE)

`essay_tongpin.txt` was converted from [rime-essay](https://github.com/rime/rime-essay)  
License: [GNU Lesser General Public License v3.0](https://github.com/rime/rime-essay/blob/master/LICENSE)

`emoji_category_tongpin.txt` and `emoji_word_tongpin.txt` was converted from [rime-emoji](https://github.com/rime/rime-emoji)  
License: [GNU Lesser General Public License v3.0](https://github.com/rime/rime-emoji/blob/master/LICENSE)

`TWPhrasesIT_tongpin.txt` and `TWPhrasesName_tongpin.txt` and `TWPhrasesOther_tongpin.txt` was converted from [OpenCC](https://github.com/BYVoid/OpenCC)  
License: [Apache License 2.0](https://github.com/BYVoid/OpenCC/blob/master/LICENSE)

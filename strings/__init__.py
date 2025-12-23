import os
from typing import List

import yaml

LOGGERS = "Branded_king__robot"

languages = {}
languages_present = {}


def get_string(lang: str = "ar"):
    return languages[lang]


for filename in os.listdir(r"./strings/langs/"):
    # تحميل اللغة العربية مرة واحدة
    if "ar" not in languages:
        languages["ar"] = yaml.safe_load(
            open(r"./strings/langs/ar.yml", encoding="utf8")
        )
        languages_present["ar"] = languages["ar"]["name"]

    if filename.endswith(".yml"):
        language_name = filename[:-4]

        # تجاهل أي ملف لغة غير العربية
        if language_name != "ar":
            continue

        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )

    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("في مشكلة داخل ملف اللغة، تأكد إن ar.yml سليم.")
        exit()

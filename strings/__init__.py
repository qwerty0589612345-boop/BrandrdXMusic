import yaml

LOGGERS = "Branded_king__robot"

languages = {}
languages_present = {}


def get_string(lang: str = "ar"):
    return languages["ar"]


# تحميل اللغة العربية فقط
with open("./strings/langs/ar.yml", encoding="utf8") as f:
    languages["ar"] = yaml.safe_load(f)
    languages_present["ar"] = languages["ar"].get("name", "العربية")

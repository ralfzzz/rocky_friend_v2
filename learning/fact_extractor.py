import re


def extract_fact(text):

    text = text.lower()

    patterns = {

        "job": r"(?:saya|i am) (?:seorang )?(.+?)(?:\.|$)",

        "city": r"(?:tinggal di|live in) (.+)",

        "favorite_language": r"suka (?:bahasa )?python",

        "favorite_food": r"suka makan (.+)"

    }

    result = {}

    if "python" in text:

        result["favorite_language"] = "Python"

    city = re.search(patterns["city"], text)

    if city:

        result["city"] = city.group(1).title()

    food = re.search(patterns["favorite_food"], text)

    if food:

        result["favorite_food"] = food.group(1).title()

    return result
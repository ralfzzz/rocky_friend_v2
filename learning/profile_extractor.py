import re


def extract_name(text):

    patterns = [

        r"nama saya (.+)",

        r"saya (.+)",

        r"my name is (.+)"

    ]

    for pattern in patterns:

        match = re.search(pattern, text.lower())

        if match:

            return match.group(1).strip().title()

    return None
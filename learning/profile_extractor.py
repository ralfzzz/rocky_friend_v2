import re


def extract_name(text):

    patterns = [

        r"nama saya (.+)",

        r"saya (.+)",

        r"my name is (.+)"

    ]

    for pattern in patterns:

        NAME_PATTERN = re.compile(

        r"nama saya (.+)",

        re.IGNORECASE

    )

        match = NAME_PATTERN.search(text)

        if match:

            return match.group(1).strip().title()

    return None
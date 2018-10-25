from copy import deepcopy


import pytest
from marshmallow import ValidationError


from clean_code.compile_reading_list import ReadingListSchema, format_review


valid_dict = {
    'title': 'title',
    'author': 'author',
    'availability': ['list', 'of', 'strings'],
    'recommendation': {
        'level': 'moderate',
        'parts': 'parts',
    },
    'price': 'price as string',
    'length': {
        'time': "> 10 hrs",
        'pages': 300,
    },
    'ease_of_use': 'moderate',
}


def test_validation_and_renaming():
    validated_schema = ReadingListSchema(strict=True).load(valid_dict)

    assert validated_schema.data["ease of use"] == "moderate"

    for key in valid_dict:
        invalid_dict = deepcopy(valid_dict)
        invalid_dict.pop(key)
        with pytest.raises(ValidationError):
            ReadingListSchema(strict=True).load(invalid_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["recommendation"]["level"] = "junk"
    with pytest.raises(ValidationError):
        ReadingListSchema(strict=True).load(invalid_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["length"]["time"] = "junk"
    with pytest.raises(ValidationError):
        ReadingListSchema(strict=True).load(invalid_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["ease_of_use"] = "junk"
    with pytest.raises(ValidationError):
        ReadingListSchema(strict=True).load(invalid_dict)


def test_formatting():
    validated_schema = ReadingListSchema(strict=True).load(valid_dict)

    result = format_review(validated_schema)
    expected = (
        "title by author\n"
        "+++++++++++++++\n"
        "\n"
        "- availability\n"
        "    - list\n"
        "    - of\n"
        "    - strings\n"
        "- recommendation\n"
        "    - moderate (parts)\n"
        "- price\n"
        "    - price as string\n"
        "- length\n"
        "    - time: > 10 hrs\n"
        "    - pages: 300\n"
        "- ease of use\n"
        "    - moderate\n"
    )

    assert result == expected


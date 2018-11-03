from copy import deepcopy
import re


import pytest
from marshmallow import ValidationError


from clean_code.compile_reading_list import (
    ReadingListSchema,
    format_review,
    load_review_yml,
    main,
)


valid_dict = {
    "title": "title",
    "author": "author",
    "availability": ["list", "of", "strings"],
    "recommendation": {"level": "moderate", "parts": "parts"},
    "price": "price as string",
    "length": {"time": "> 10 hrs", "pages": 300},
    "ease_of_use": "moderate",
    "comment": "any old string",
}


def test_load_review_yml():
    validated_schema = load_review_yml(valid_dict)

    assert validated_schema.data["ease of use"] == "moderate"

    optional_keys = ["comment"]
    for key in valid_dict:
        altered_dict = deepcopy(valid_dict)
        altered_dict.pop(key)
        if key in optional_keys:
            valid_schema = load_review_yml(altered_dict)
            assert key not in valid_schema
        else:
            with pytest.raises(ValidationError):
                load_review_yml(altered_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["recommendation"]["level"] = "junk"
    with pytest.raises(ValidationError):
        load_review_yml(invalid_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["length"]["time"] = "junk"
    error_msg = re.escape(
        "Invalid value for 'time'. Available options are:\n"
        "- <1 min\n"
        "- 1 min\n"
        "- 10 mins\n"
        "- 30 mins\n"
        "- 1 hr\n"
        "- 2 hrs\n"
        "- 5 hrs\n"
        "- > 10 hrs\n"
    )
    with pytest.raises(ValidationError, match=error_msg):
        load_review_yml(invalid_dict)

    invalid_dict = deepcopy(valid_dict)
    invalid_dict["ease_of_use"] = "junk"
    with pytest.raises(ValidationError):
        load_review_yml(invalid_dict)


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
        "\n"
        "Other comments\n"
        "~~~~~~~~~~~~~~\n"
        "\n"
        "any old string\n"
    )

    assert result == expected


def test_main():
    main()

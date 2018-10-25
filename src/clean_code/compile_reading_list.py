"""Compile our reading list page from our reviews

This script reads in our reviews, validates them, formats them and then writes them to
our output file.
"""
from os import listdir
from os.path import join, realpath, isdir, mkdir
import pkg_resources
import yaml


from marshmallow import Schema, fields
from marshmallow.schema import UnmarshalResult


def validate_level(l):
    valid_levels = ["essential", "high", "moderate", "low", "zero"]

    return l in valid_levels


class RecommendationSchema(Schema):
    level = fields.String(required=True, validate=validate_level)
    parts = fields.String(required=True)


def validate_time(t):
    valid_times = [
        "<1 min", "1 min", "10 mins", "30 mins",
        "1 hr", "2 hrs", "5 hrs", "> 10 hrs",
    ]

    return t in valid_times


class LengthSchema(Schema):


    time = fields.String(required=True, validate=validate_time)
    pages = fields.Integer(required=True)


def validate_ease_of_use(u):
    valid_ease_of_uses = ["trivial", "easy", "moderate", "hard", "nuclear"]

    return u in valid_ease_of_uses


class ReadingListSchema(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)
    availability = fields.List(fields.String(), required=True)
    recommendation = fields.Nested(RecommendationSchema, required=True)
    price = fields.String(required=True)
    length = fields.Nested(LengthSchema, required=True)
    ease_of_use = fields.String(
        required=True,
        attribute="ease of use",
        validate=validate_ease_of_use
    )


def format_review(review_schema):
    review_schema = (
        review_schema.data
        if isinstance(review_schema, UnmarshalResult)
        else review_schema
    )

    indent = " " * 4

    title = review_schema["title"]
    author = review_schema["author"]
    availability_list = f"\n{indent}- ".join(review_schema["availability"])
    recommendation_level = review_schema["recommendation"]["level"]
    recommended_parts = review_schema["recommendation"]["parts"]
    price = review_schema["price"]
    length_time = review_schema["length"]["time"]
    length_pages = review_schema["length"]["pages"]
    ease_of_use = review_schema["ease of use"]

    header = f"{title} by {author}"
    header_underline = "+" * len(header)

    formatted_review = (
        "\n".join([header, header_underline]) +
         "\n\n"
         "- availability\n"
        f"    - {availability_list}\n"
         "- recommendation\n"
        f"    - {recommendation_level} ({recommended_parts})\n"
         "- price\n"
        f"    - {price}\n"
         "- length\n"
        f"    - time: {length_time}\n"
        f"    - pages: {length_pages}\n"
         "- ease of use\n"
        f"    - {ease_of_use}\n"
    )

    return formatted_review

def main():
    pkg_root = pkg_resources.resource_filename("clean_code", "__init__.py").replace(
        join("src", "clean_code", "__init__.py"),
        ""
    )
    docs_root = join(pkg_root, "docs")

    template_file = join(docs_root, "reading_list_template.rst")
    print("Using template:\n{}\n".format(template_file))

    with open(template_file, "r") as f:
        template = f.read()


    review_root = join(docs_root, "reading")
    review_sources = [
        join(review_root, f)
        for f in listdir(review_root)
        if f.endswith(".yml")
    ]
    print("Found review files:\n{}\n".format("\n".join(review_sources)))

    reviews = []
    for rs in review_sources:
        with open(rs, "r") as f:
            rs_dict = yaml.load(f)

        rs_validated = ReadingListSchema(strict=True).load(rs_dict)
        reviews.append(format_review(rs_validated))

    reviews = "\n\n".join(reviews)

    text_to_write = template.replace("<resources go here>", reviews)

    output_file = join(pkg_root, "docs", "reading_list.rst")
    print("Writing formatted reading guide to:\n{}".format(output_file))

    if not isdir(realpath(output_file)):
        mkdir(realpath(output_file))

    with open(output_file, "w") as of:
        of.write(text_to_write)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Workflow to validate Redump bot .json
# Written by Edness   v1.0.1   2025-10-24

import json

def validate_json(path):
    print("Validating", path)

    # validate json formatting
    with open(path, "r") as file:
        articles = json.load(file)

    # validate json data itself
    assert type(articles["articles"]) is dict
    for k in articles["articles"]:
        assert type(articles["articles"][k]) is list
        for v in articles["articles"][k]:
            assert type(v) is str and v.isascii()
    assert type(articles["strict"]) is dict
    for k in articles["strict"]:
        assert type(articles["strict"][k]) is list
        for v in articles["strict"][k]:
            assert type(v) is str and v.isascii()
    assert type(articles["exclude"]) is list
    for v in articles["exclude"]:
        assert type(v) is str and v.isascii()

    print("Articles list is valid!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to a file to read")
    args = parser.parse_args()

    validate_json(args.path)

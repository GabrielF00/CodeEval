__author__ = 'Gabriel Fishman'
"""
JSON MENU IDS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/102/

You have JSON string which describes a menu. Calculate the SUM of IDs of all "items" in the case a "label" exists for
an item.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

* {"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85},
{"id": 54}, null, {"id": 46, "label": "Label 46"}]}}

* {"menu": {"header": "menu", "items": [{"id": 81}]}}

* {"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, {"id": 85, "label": "Label 85"}, {"id": 93,
"label": "Label 93"}, {"id": 2}]}}

All IDs are integers between 0 and 100. It can be 10 items maximum for a menu.

OUTPUT SAMPLE:

Print results in the following way.

* 46
* 0
* 248
"""

import json
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        json_obj = json.loads(test_case)
        id_sum = 0
        items = json_obj["menu"]["items"]
        for item in items:
            if isinstance(item, dict):
                if item.has_key("id") and item.has_key("label"):
                    id_sum += int(item.get("id"))
        print id_sum

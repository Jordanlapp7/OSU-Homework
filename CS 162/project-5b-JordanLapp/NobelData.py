# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/21/2023
# Description: Reads a JSON file to a NobelDate class and contains a function to look up laureates.

import json


class NobelData:
    """Reads a JSON file to a NobelDate class and contains a function to look up laureates."""
    def __init__(self):
        with open('nobels.json', 'r') as infile:
            self._object = json.load(infile)

    def search_nobel(self, year, category):
        laureates = []
        prizes = self._object["prizes"]
        for prize in prizes:
            if prize["year"] == year and prize["category"] == category:
                for laureate in prize["laureates"]:
                    laureates.append(laureate["surname"])
        laureates.sort()
        return laureates

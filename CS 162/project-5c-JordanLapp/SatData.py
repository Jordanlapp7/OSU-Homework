# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/21/2023
# Description: Reads in SAT data and provides method for writing stats of specific schools to .csv file.

import json


class SatData:
    """Reads in SAT data and provides method for writing stats of specific schools to .csv file."""
    def __init__(self):
        with open('sat.json', 'r') as infile:
            self._obj = json.load(infile)

    def save_as_csv(self, dbn_list):
        """Takes a list of DBNs and writes the associated stats to a .csv file."""
        data = self._obj['data']
        with open('output.csv', 'w') as outfile:
            outfile.write("DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean\n")
            for dbn in dbn_list:
                for school in data:
                    if dbn == school[8]:
                        outfile.write(school[8])
                        outfile.write(",")
                        outfile.write(school[9])
                        outfile.write(",")
                        outfile.write(school[10])
                        outfile.write(",")
                        outfile.write(school[11])
                        outfile.write(",")
                        outfile.write(school[12])
                        outfile.write(",")
                        outfile.write(school[13])
                        outfile.write("\n")

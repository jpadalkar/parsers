"""Main script to run entire package"""

import sys
import os
from multiprocessing import Process
from parserSEC.crawl import *


def DERA():
    print("Downloading DERA data")
    try:
        os.makedirs("DERA/")
    except OSError:
        print("DERA directory already exists")
    urls = ["https://www.sec.gov/dera/data/financial-statement-data-sets.html",
            "https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets",
            "https://www.sec.gov/dera/data/mutual-fund-prospectus-risk-return-summary-data-sets"]
    outdirs = ["DERA/financial_statements/", "DERA/crowdfunding/", "DERA/mutual_fund_prospectus/"]
    for i in range(3):
        p = Process(target=find_and_download, args=(urls[i], outdirs[i]))
        p.start()


def main():
    """Top level command line interface."""
    print("SEC Parser")
    DERA()


if __name__ == "__main__":
    main()

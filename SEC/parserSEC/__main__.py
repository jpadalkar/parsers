"""Main script to run entire package"""

import sys
import os
from parserSEC.crawl import *


def DERA():
    crowdfunding_url = "https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets"
    mutual_fund_url = "https://www.sec.gov/dera/data/mutual-fund-prospectus-risk-return-summary-data-sets"
    try:
        os.makedirs("DERA/")
    except OSError:
        print("DERA directory already exists")
    fin_statements_url = "https://www.sec.gov/dera/data/financial-statement-data-sets.html"
    print("Downloading financial statements")
    fin_zips = get_file_links(fin_statements_url)
    download_zips(fin_zips, out_dir = "DERA/financial_statements/")
    print("Downloading crowdfunding offerings")
    crowd_zips = get_file_links(crowdfunding_url)
    download_zips(crowd_zips, out_dir = "DERA/crowdfunding/")
    print("Downloading mutual fund prospectus")
    mutual_zips = get_file_links(mutual_fund_url)
    download_zips(mutual_zips, out_dir = "DERA/mutual_fund_prospectus/")


def main():
    """Top level command line interface."""
    print("SEC Parser")
    DERA()


if __name__ == "__main__":
    main()

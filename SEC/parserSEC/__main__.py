"""Main script to run entire package"""

from parserSEC import crawl

def main():
    """Top level command line interface."""
    print("SEC Parser")
    fin_statements_url = "https://www.sec.gov/dera/data/financial-statement-data-sets.html"
    crowdfunding_url = "https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets"
    mutual_fund_url = "https://www.sec.gov/dera/data/mutual-fund-prospectus-risk-return-summary-data-sets"
    


if __name__ == "__main__":
    main()

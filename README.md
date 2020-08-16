# amazon_buddy
![python_version](https://img.shields.io/static/v1?label=Python&message=3.5%20|%203.6%20|%203.7&color=blue) [![PyPI downloads/month](https://img.shields.io/pypi/dm/amazon_buddy?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/amazon_buddy)

## Description
Python wrapper for the [amazon-buddy](https://www.npmjs.com/package/amazon-buddy) npm package

## Install
First you need to install kfork-amazon-buddy npm as cli

For instructions check [github](https://github.com/drawrowfly/amazon-scraper) or [npm](https://www.npmjs.com/package/amazon-buddy)
NOTE: Install my fork (kfork-amazon-buddy) instead of (amazon-buddy). Other than that it should be the same isntallation process.

~~~~bash
pip install amazon_buddy
# or
pip3 install amazon_buddy
~~~~

## Usage

~~~~python
from amazon_buddy import AmazonBuddy

print(AmazonBuddy.get_product_details('macbook'))
print(AmazonBuddy.get_reviews('B01GW3H3U8', min_rating=4))
~~~~
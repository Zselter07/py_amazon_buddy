from amazon_buddy import AmazonBuddy, Category, SortType

# products = AmazonBuddy.search_products(
#     'vacuums',
#     category=Category.AUTOMOTIVE_PARTS_AND_ACCESSORIES,
#     sort_type=SortType.REVIEW_RANK,
#     min_rating=3.0,
#     # min_price=24.99,
#     # min_reviews=3,
#     max_results=10,
#     debug=True
# )
# print(len(products))

# print(AmazonBuddy.get_related_searches('electric bike', category=Category.ALL_DEPARTMENTS, debug=True))

# AmazonBuddy.get_product_details(asin='B07XMMQ1VP', debug=True).jsonprint()
# AmazonBuddy.get_product_details(asin='B07XJB7CG3', user_agent=RandomUA.random(), debug=True).jsonprint()
# print(len(reviews))

# [r.jsonprint() for r in AmazonBuddy.get_product_reviews_with_images(asin='B07N6S4SY1', debug=True)]

# print(AmazonBuddy.get_trends(category=Category.PREMIUM_BEAUTY, max_results_per_letter=10, debug=True))
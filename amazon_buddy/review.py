# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Pip
from jsoncodable import JSONCodable

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: Review ------------------------------------------------------------- #

class Review(JSONCodable):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        dict_: dict
    ):
        self.id = dict_['id']
        self.review_data = dict_['review_data']
        self.name = dict_['name']
        self.rating = dict_['rating']
        self.title = dict_['title']
        self.review = dict_['review']


# ---------------------------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Pip
from jsoncodable import JSONCodable

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: Review ------------------------------------------------------------- #

class Review(JSONCodable):

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        id: str,
        name: str,
        rating: int,
        upvotes: int,
        title: str,
        text: str
    ):
        self.id = id
        self.name = name
        self.rating = rating
        self.upvotes = upvotes
        self.title = title
        self.text = text


# ---------------------------------------------------------------------------------------------------------------------------------------- #
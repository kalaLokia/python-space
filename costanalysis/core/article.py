"""
Article model structure.
"""

import math


class Article:
    def __init__(
        self,
        brand: str = "brand 1",
        artno: str = "1111",
        color: str = "bk",
        size: int = 8,
        case_type: str = "1",
    ):
        self.artno = artno.lower()
        self.color = color.lower()
        self._category = "g"
        self.size = size
        self.case_type = case_type.lower()
        self.brand = brand.lower()
        self.pairs_in_case = 0
        self.mrp = 0.0
        self.stitch_rate = 0.0
        self.print_rate = 0.0
        self.basic_rate = 0.0

    @property
    def article_name(self) -> str:
        return "{0} {1} {2}".format(
            self.artno.upper(), self.color_name, self.category_name
        )

    @property
    def get_mc_name(self) -> str:
        prefix = "2-fb"
        return "-".join(
            [prefix, self.artno, self.color, self.category + self.case_type]
        )

    @property
    def get_category_size(self) -> str:
        return "{}{:02d}".format(self.category, self.size)

    @property
    def get_filename(self) -> str:
        return f"{self.article_name}.xlsx"

    @property
    def category(self):
        return self._category

    @property
    def article_code(self) -> str:
        return f"{self.artno}-{self.color}-{self._category}"

    @category.setter
    def category(self, value):
        self._category = {
            "gents": "g",
            "ladies": "l",
        }.get(value.lower(), "g")

    @property
    def category_name(self):
        return (
            {
                "g": "gents",
                "l": "ladies",
            }
            .get(self._category, self._category)
            .title()
        )

    @property
    def color_name(self):
        return (
            {
                "bk": "black",
                "br": "brown",
                "bl": "blue",
                "rd": "red",
                "ta": "tan",
                "wt": "white",
                "nb": "navy blue",
            }
            .get(self.color, self.color)
            .title()
        )

    def __str__(self):
        return self.article_code

    @classmethod
    def from_bulk_list(cls, article, rates):
        try:
            artno, color, catg = article.lower().split("-")
            catg = catg[0]
        except:
            artno, color, catg = "1111", "bk", "g"

        size = {"g": 8, "l": 7}.get(catg, 8)
        obj = cls(brand="brand 1", artno=artno, color=color, size=size)
        obj._category = catg
        obj.print_rate = 0 if math.isnan(rates[0]) else rates[0]
        obj.stitch_rate = 0 if math.isnan(rates[1]) else rates[1]
        obj.basic_rate = 0 if math.isnan(rates[2]) else rates[2]
        return obj

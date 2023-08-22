from PIL import Image
from typing import List


class ProductResult:
    def __init__(self, link: str, brand: str, store: str, desc: str, imgs: List[Image.Image]):
        self.link = link
        self.brand = brand
        self.store = store
        self.desc = desc
        self.imgs = imgs


class ProductSearchInterface():
    def search_product_by_img(self, img: Image) -> List[ProductResult]:
        pass

from typing import List
from PIL import Image
from .product_search_interface import ProductResult, ProductSearchInterface
import requests, json
import os


BASE_URI = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
API_KEY = 'ENTER_API_KEY'
imagePath = './app/ai/shopping/tshirt2.png'


class ProductSearchBing(ProductSearchInterface):

	def print_json(self, obj):
		"""Print the object as json"""
		print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))

	def search_product_by_img(self, img: Image) -> List[ProductResult]:
		print(os.getcwd())
		HEADERS = {'Ocp-Apim-Subscription-Key': API_KEY}

		file = {'image' : ('myfile', open(imagePath, 'rb'))}

		try:
			response = requests.post(BASE_URI, headers=HEADERS, files=file)
			response.raise_for_status()
			self.print_json(response.json())

		except Exception as ex:
			raise ex

		return []


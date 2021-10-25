import requests
from PIL import Image
from io import BytesIO
from os import path

class Alter:
    
    def __init__(self, card_name) -> None:
        self.card_name = card_name
        self.card_image = None
        self.alter_image = None
        
    # Get original card image from scryfall and save in self.card_image
    def get_card_image(self):
        SCRYFALL_API = 'https://api.scryfall.com'
        endpoint = '/cards/named'
        
        url = SCRYFALL_API+endpoint
        
        parameters = {'exact': self.card_name, 'format': 'image'}
        
        result = requests.get(url, params=parameters)
        
        self.card_image = Image.open(BytesIO(result.content))
    
    # NOT YET DONE
    def get_card_info(self):
        SCRYFALL_API = 'https://api.scryfall.com'
        endpoint = '/cards/named'
        
        url = SCRYFALL_API+endpoint
        
        parameters = {'exact': self.card_name, 'format': 'json'}
        
        result = requests.get(url, params=parameters)
        
        return result

    # Get alter art from path and save in self.alter_image LOCALLY
    def load_image(self, file_name):
        # replace with relative path (use __file__)
        IMAGE_FOLDER = path.join(os.getcwd(), '..', 'data', 'images')
        file_path = path.join(IMAGE_FOLDER, file_name)
        
        image = None
        
        self.alter_imageimage = Image.open(file_path)
        #with Image.open(file_path) as im:
        #    image = im
            
    # replace original art with alter art in card_image
    def replace_image(self):
        self.card_image.paste(self.alter_image, box = (50,100))
        
        
    def alter_card(self, new_image_path, new_name = None, new_flavor = None):
        
        # Load new image from path and replace old art
        self.alter_image = self.load_image(new_image_path)
        self.replace_image()
        
    def get_card(self):
        return self.card_image
        
        
        
from rembg import remove
from PIL import Image
from ultralytics import YOLO
input_path = '/Users/paif_iris/Desktop/test/IMG_1307.png'
output_path = 'output_cropped.png'

#get dimension if needed
# def get_png_dimensions(image_path):
#     try:
#         with Image.open(image_path) as img:
#             width, height = img.size
#             return width, height
#     except FileNotFoundError:
#         print(f"Error: Image file not found at '{image_path}'")
#         return None
#     except Exception as e:
#         print(f"Error opening or processing image: {e}")
#         return None

# dimensions = get_png_dimensions(input_path)
# width, height = dimensions







#resize image first by user. tell user usually good for clear background.
from ultralytics import YOLO
from PIL import Image
from rembg import remove

class HelperFunction:
    def __init__(self, image):
        self.image = image

    def get_pet(self, input_path):
        model = YOLO("yolov8m.pt")
        results = model.predict(input_path, save=False, imgsz=320, conf=0.25, save_txt = False)

        pet_boxes = []

        cls = int(results[0].boxes.cls[0])
        if cls in [15, 16]:
            pet_boxes.append(results[0].boxes.xyxy[0].tolist())

        input = Image.open(input_path)
        if len(pet_boxes) == 0:
            raise ValueError("No pet detected.")

        x1, y1, x2, y2 = map(int, pet_boxes[0])
        pad = 20
        x1, y1 = max(0, x1-pad), max(0, y1-pad)
        x2, y2 = min(input.width, x2+pad), min(input.height, y2+pad)

        cropped = input.crop((x1, y1, x2, y2))
        cropped.save("pet_cropped.jpg")

        #self.image = self.remove_background("pet_cropped.jpg", "output_cropped.png")
    
    # def make_3D(self, input_path, output_path):
    #     from rembg import remove
    #     input_image = Image.open(input_path)
    #     output = remove(input_image)
    #     output.save(output_path)
    #     print(f"3D image saved to {output_path}")

    def remove_background(self, input_path, output_path):
        input_image = Image.open(input_path)
        output = remove(input_image)
        output.save(output_path)
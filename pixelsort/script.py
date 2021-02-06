from PIL import Image
import logging
from main import pixelsort
from util import id_generator

CUSTOM_PATH = "../custom/"
IMAGE_INPUT = f"{CUSTOM_PATH}test.jpg"
IMAGE_OUTPUT = None

if image_output_path is None:
    image_output_path = id_generator() + ".png"
    logging.warning("No output path provided, using " + image_output_path)


args = {}
logging.debug("Opening image...")
args["image"] = Image.open(image_input_path)
args["angle"] = 35

logging.debug("Sorting those pixels...")
logging.debug(f"Args supplied: {str(args)}")
output = pixelsort(**args)

logging.debug("Saving image...")
output.save(image_output_path)

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from PIL import Image
import logging
logging.basicConfig(level=logging.INFO)
from pixelsort.main import pixelsort
from pixelsort.util import id_generator
from pixelsort.util import calc_size_given_max_dim
from pixelsort.util import ArgLog

CUSTOM_PATH = "./custom/"

def custom_dir(path):
    return f"{CUSTOM_PATH}{path}"

IMAGE_INPUT = "test.jpg"
IMAGE_OUTPUT = None
MAX_DIM_SIZE = 1260

# if IMAGE_OUTPUT is None:
#     IMAGE_OUTPUT = id_generator()
#     logging.warning("No output path provided, using " + IMAGE_OUTPUT)


logging.info("Opening image...")

image = Image.open(custom_dir(IMAGE_INPUT))
h, w = image.size
if h > MAX_DIM_SIZE or w > MAX_DIM_SIZE:
    imsize = calc_size_given_max_dim(image.size, MAX_DIM_SIZE)
    logging.warning(f"Image of size {image.size} exceeds the maximum dimension size of {MAX_DIM_SIZE}. Resizing to {imsize}")
    image = image.resize(imsize)

thresholds = [
    'random',
    'edges',
    'threshold',
    'waves',
    # 'file',
    # 'file-edges',	
    'none'
]

for threshold in thresholds:
    # if IMAGE_OUTPUT is None:
    IMAGE_OUTPUT = id_generator() + threshold
        # logging.warning("No output path provided, using " + IMAGE_OUTPUT)

    argLogger = ArgLog()

    args = {}

    args["angle"] = 55
    args["image"] = image
    args["interval_function"] = threshold
    args["sorting_function"] = "luma"
    argLogger.add_args(args)
    logging.info("Sorting those pixels...")
    logging.info(f"Args supplied: {str(args)}")
    output = pixelsort(**args)

    logging.info("Saving image...")
    output.save(custom_dir(IMAGE_OUTPUT) + ".png")
    argLogger.save(IMAGE_OUTPUT)
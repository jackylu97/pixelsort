from PIL import Image
import logging
logging.basicConfig(level=logging.INFO)
from main import pixelsort
from util import id_generator
from util import calc_size_given_max_dim
from util import ArgLog

CUSTOM_PATH = "../custom/"

def custom_dir(path):
    return f"{CUSTOM_PATH}{path}"

IMAGE_INPUT = "test.jpg"
IMAGE_OUTPUT = None
MAX_DIM_SIZE = 1260

if IMAGE_OUTPUT is None:
    IMAGE_OUTPUT = id_generator()
    logging.warning("No output path provided, using " + IMAGE_OUTPUT)

argLogger = ArgLog()

args = {}
logging.info("Opening image...")

image = Image.open(custom_dir(IMAGE_INPUT))
h, w = image.size
if h > MAX_DIM_SIZE or w > MAX_DIM_SIZE:
    imsize = calc_size_given_max_dim(image.size, MAX_DIM_SIZE)
    logging.warning(f"Image of size {image.size} exceeds the maximum dimension size of {MAX_DIM_SIZE}. Resizing to {imsize}")
    image = image.resize(imsize)

# args["image"] = image
# args["angle"] = 90
# # args["interval_function"] = "edges"
# argLogger.add_args(args.copy())
# logging.info("Sorting those pixels...")
# logging.info(f"Args supplied: {str(args)}")
# output = pixelsort(**args)

args["angle"] = 0
args["image"] = image
# args["interval_function"] = "edges"
argLogger.add_args(args.copy())
logging.info("Sorting those pixels...")
logging.info(f"Args supplied: {str(args)}")
output = pixelsort(**args)

logging.info("Saving image...")
output.save(custom_dir(IMAGE_OUTPUT) + ".png")
argLogger.save(custom_dir(IMAGE_OUTPUT))
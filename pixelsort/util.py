from colorsys import rgb_to_hsv
import json
import time
import os.path
from pixelsort.constants import DEFAULTS


def id_generator():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return timestr


def lightness(pixel):
    # For backwards compatibility with python2
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[2] / 255.0


def hue(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[0] / 255.0


def saturation(pixel):
    return rgb_to_hsv(pixel[0], pixel[1], pixel[2])[1] / 255.0

def calc_size_given_max_dim(size, mx):
    # get height, width with same aspect ratio, setting the larger dimension to mx
    assert len(size) == 2, f"image should have dim=2 !! got {size}"
    h, w = size

    if h > w:
        w = (float(mx) / float(h)) * w
        return (mx, int(w))
    else:
        h = (float(mx) / float(w)) * h
        return (int(h), mx)

class ArgLog:
    def __init__(self, base_dir="./custom/"):
        self.argdicts = []
        self.base_dir = base_dir
    
    def add_args(self, arg_dict):
        # save copy, in case dict object is modified later
        self.argdicts.append(arg_dict.copy())

    def save(self, path):
        save_text = ""
        for d in self.argdicts:
            d = dict(DEFAULTS, **d)
            d["image"] = f"image_{d['image'].size}"
            save_text = save_text + json.dumps(d) + '\n'
        if not os.path.isdir(self.base_dir + '/arg_logs'):
            os.mkdir(self.base_dir + '/arg_logs')
        with open(f"{self.base_dir}arg_logs/{path}.txt", 'w') as file:
            file.write(save_text)


def crop_to(image_to_crop, reference_image):
    """
    Crops image to the size of a reference image. This function assumes that the relevant image is located in the center
    and you want to crop away equal sizes on both the left and right as well on both the top and bottom.
    :param image_to_crop
    :param reference_image
    :return: image cropped to the size of the reference image
    """
    reference_size = reference_image.size
    current_size = image_to_crop.size
    dx = current_size[0] - reference_size[0]
    dy = current_size[1] - reference_size[1]
    left = dx / 2
    upper = dy / 2
    right = dx / 2 + reference_size[0]
    lower = dy / 2 + reference_size[1]
    return image_to_crop.crop(
        box=(
            int(left),
            int(upper),
            int(right),
            int(lower)))

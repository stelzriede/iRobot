#!/usr/bin/env python

# (This is an example similar to an example from the Adafruit fork
#  to show the similarities. Most important difference currently is, that
#  this library wants RGB mode.)
#
# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.led_rgb_sequence = 'RBG'

matrix = RGBMatrix(options = options)

# RGB example w/graphics prims.
# Note, only "RGB" mode is supported currently.
# image = Image.new("RGB", (64,  64))  # Can be larger than matrix if wanted!!
# draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
# # Draw some shapes into image (no immediate effect on matrix)...
# draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 255))
# draw.line((0, 0, 31, 31), fill=(255, 0, 0))
# draw.line((0, 31, 31, 0), fill=(0, 255, 0))

# # Then scroll image across matrix...
# for n in range(-32, 33):  # Start off top-left, move off bottom-right
#     matrix.Clear()
#     matrix.SetImage(image, n, n)
#     time.sleep(0.05)

# matrix.Clear()
eye_open = Image.open("eye_open.gif").convert('RGB')
matrix.SetImage(eye_open, 0, 0)
eye_half = Image.open("eye_open_half.gif").convert('RGB')
matrix.SetImage(eye_half, 0, 0)
eye_slit = Image.open("eye_open_slit.gif").convert('RGB')
matrix.SetImage(eye_slit, 0, 0)
eye_closed = Image.open("blank.gif").convert('RGB')
matrix.SetImage(eye_closed, 0, 0)
while True:
	matrix.SetImage(eye_open, 0, 0)
	time.sleep(2.5)
	matrix.SetImage(eye_half, 0, 0)
	time.sleep(0.1)
	matrix.SetImage(eye_slit, 0, 0)
	time.sleep(0.1)
	matrix.SetImage(eye_closed, 0, 0)
	time.sleep(0.1)

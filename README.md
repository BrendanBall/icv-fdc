Author: Brendan Ball
Date: 17 August 2015

Introduction to Computer Vision, feature detection for circles.
Simple circle detector. Detects circles in images and highlights them.

This program is entirely written in python 2 but has 2 dependencies:
python numpy version 1.9.2
python Pillow version 2.9.0 (a fork of python PIL)

This program has been tested using python 2.7
I have tested this program using gif image format

I have made sure that these dependencies are installed on the nightmare server
and I have tested that it works on nightmare (at least from my account).

It should all work but if you encounter an error or want to run it on a different machine
then you will have to make sure the dependencies are installed.

RUN:
python main.py <filename> 
other options exist, run the following for help:
python main.py -h
and you will get: 

usage: main.py [-h] [--slow] [-r RADIUS] [--save] filename

Simple circle detector. Detects circles in images and highlights them

positional arguments:
  filename              filename of the image you want to process

optional arguments:
  -h, --help            show this help message and exit
  --slow                If you want to use the naive gaussian blur which is
                        very slow then go ahead
  -r RADIUS, --radius RADIUS
                        Detect circles of specific radius. Uses naive hough
                        transform
  --save                Save the files to disk instead of just view them
                        temporarily



Description:
The program contains both slow versions of the gaussian blur and hough transforms and optimized versions.
The gaussian blur was optimized by vectorizing it using numpy.

The hough transform was optimized as follows:

This hough transform is optimized as it doesn't blindly bruteforce every possible radius 
throughout the image. Instead it finds shapes (a shape is a collection of connected points)
and creates a bounding box around this shape. the radius is calculated on the assumption that the
shape is a circle by getting the difference between the highest and lowest point in the shape.
If it is a circle then this radius is correct, otherwise it will simply fail in accumulation and thresholding.
regional accumulation is then performed on the bounding box with the specific radius and if a local maxima is above the
threshold then it's assumed to be a circle.

This means that instead of having to create a 3D array for the circle hough transform, I only use a 2D array.
Different parts of the array uses a hough transform with a different radius. 

Connected points are found using a simple depth first search algorithm.


To install dependencies without a python virtualenv:
sudo -H pip install numpy
sudo -H pip install pillow

To install dependencies inside a python virtualenv run the following:
# inside working directory, assumes python 2 is default python
virtualenv icv
source icv/bin/activate
# the virtualenv has now been started, to deactivate it simply run "deactivate"
pip install numpy
pip install pillow
#this takes a while as numpy has to compile lots of things




"""
.. module:: color
    :synopsis: main module for color processing in images

.. moduleauthor:: Raymel Francisco <franciscoraymel@gmail.com>
.. created:: Nov 15, 2017
"""
from PIL import Image
from eliana.lib.eliana_image import ElianaImage


class Color:

    @staticmethod
    def to_hsv(img: ElianaImage):
        return ElianaImage(pil=img.as_pil.convert('HSV'))

    @staticmethod
    def to_rgb(img: ElianaImage):
        return ElianaImage(pil=img.as_pil.convert('RGB'))

"""
.. module:: eliana_image
    :platform: Linux
    :synopsis: eliana image container

.. moduleauthor:: Raymel Francisco <franciscoraymel@gmail.com>
"""

import numpy as np
from PIL import Image

from matplotlib import pyplot as plt


class ElianaImage():
    """.. class:: ElianaImage

    Class for Eliana image container.
    """

    # TODO:
    # Add support to Tensor image.
    # Add sync update between image types

    def __init__(self, path=None, np=None, pil=None):

        """.. method:: ElianaImage(path: str)

        ElianaImage class constructor.

        Args:
            path (str): Image path.
        """

        if path is not None:
            self.__init_from_path(path)

        elif np is not None:
            self.__img_numpy = np
            self.__init_from_np()

        elif pil is not None:
            self.__img_pil = pil
            self.__init_from_pil()
        else:
            raise ValueError('No argument supplied.')

    def __init_from_path(self, path):

        self.__img_pil = Image.open(path)
        self.__init_from_pil()

    def __init_from_np(self):
        # TODO:
        # Convert np to pil
        pass

    def __init_from_pil(self):
        (self.__w, self.__h) = self.__img_pil.size

        self.__img_numpy = self.__load_image_into_numpy_array(self.__img_pil)

    @property
    def width(self):
        return self.__w

    @property
    def height(self):
        return self.__h

    @property
    def as_list(self):
        return self.__img_list

    @property
    def as_numpy(self):
        return self.__img_numpy

    @property
    def as_pil(self):
        return self.__img_pil

    def __load_image_into_numpy_array(self, img):

        img = np.array(
            img.getdata()
        ).reshape(
            (self.__h, self.__w, 3)
        ).astype(
            np.uint8
        )

        return img

    def show(self, use='pil'):
        """ Shows image.

            Args:
                use (str):

                Use 'pil' to use Pillow Image's show().

                Use 'plt' for matplotlib pyplot's imshow() and show().
        """

        def __show_using_plt():

            plt.figure(figsize=(12, 9))
            plt.imshow(self.__img_numpy)
            plt.show()

        def __show_using_pil():
            self.__img_pil.show()

        #
        #
        if use == 'pil':
            __show_using_pil()

        elif use == 'plt':
            __show_using_plt()

        else:
            raise ValueError(
                '"{}" is invalid argument. Use "pil" or "plt" only.'
                .format(use)
            )

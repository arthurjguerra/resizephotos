from unittest import TestCase, main

from PIL import Image

from core import SMALL_IMG_SIZE, MEDIUM_IMG_SIZE, LARGE_IMG_SIZE
from core.images import ResizedPhoto
from tests import clean_up_images


class TestExternalResources(TestCase):
    """
    Test for all functions that deal with external resources (images)
    """
    def setUp(self):
        clean_up_images()
        self.image_name = 'b737_5.jpg'
        self.rp = ResizedPhoto()

    def tearDown(self):
        clean_up_images()

    def test_resize_photo_small(self):
        image = Image.open(self.rp.get_small_image(self.image_name))
        self.assertEqual(SMALL_IMG_SIZE, image.size)

    def test_resize_photo_medium(self):
        image = Image.open(self.rp.get_medium_image(self.image_name))
        self.assertEqual(MEDIUM_IMG_SIZE, image.size)

    def test_resize_photo_large(self):
        image = Image.open(self.rp.get_large_image(self.image_name))
        self.assertEqual(LARGE_IMG_SIZE, image.size)

    def test_get_resized_image_small(self):
        image_resized_path = self.rp._get_resized_image(self.image_name)
        image = Image.open(image_resized_path)
        self.assertEqual(SMALL_IMG_SIZE, image.size)

    def test_get_resized_image_medium(self):
        image_resized_path = self.rp._get_resized_image(self.image_name, MEDIUM_IMG_SIZE)
        image = Image.open(image_resized_path)
        self.assertEqual(MEDIUM_IMG_SIZE, image.size)

    def test_get_resized_image_large(self):
        image_resized_path = self.rp._get_resized_image(self.image_name, LARGE_IMG_SIZE)
        image = Image.open(image_resized_path)
        self.assertEqual(LARGE_IMG_SIZE, image.size)

if __name__ == '__main__':
    main()

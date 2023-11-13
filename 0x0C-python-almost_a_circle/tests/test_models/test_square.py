#!/usr/bin/python3
"""Unit tests for the Square class"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_square_with_default_id(self):
        """Test to create a square with default id."""
        square1 = Square(1)
        self.assertEqual(square1.id, 1)

        square2 = Square(5, 3, 4)
        self.assertEqual(square2.size, 5)
        self.assertEqual(square2.width, 5)
        self.assertEqual(square2.height, 5)
        self.assertEqual(square2.x, 3)
        self.assertEqual(square2.y, 4)
        self.assertEqual(square2.id, 2)

    def test_square_str_representation(self):
        """Test __str__ representation."""
        square = Square(9, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (6) 4/5 - 9")

    def test_square_inheritance(self):
        """Test to check for inheritance."""
        square = Square(6)
        self.assertTrue(isinstance(square, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(square, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_create_square_missing_args(self):
        """Test to check for missing args."""
        with self.assertRaises(TypeError) as error:
            Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                error.exception))

    def test_inherited_methods_from_rectangle(self):
        """Test inherited methods from Rectangle."""
        square1 = Square(9)
        self.assertEqual(square1.area(), 81)

        square2 = Square(4, 1, 2, 5)
        square2.update(7)
        self.assertEqual(square2.id, 7)

        output = io.StringIO()
        square3 = Square(4)
        with contextlib.redirect_stdout(output):
            square3.display()
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")

    def test_square_size_attribute(self):
        """Test to check for size attribute."""
        square1 = Square(8)
        self.assertEqual(square1.size, 8)

        square2 = Square(9, 8, 7, 2)
        self.assertEqual(square2.size, 9)

    def test_create_square_with_incorrect_attributes(self):
        """Test to check for incorrect attributes."""
        with self.assertRaises(TypeError) as error:
            square = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            square = Square(2, "World")
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            square = Square(1, 2, "Foo", 3)
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(ValueError) as error:
            square = Square(0, 2)
        self.assertEqual("width must be > 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            square = Square(-1)
        self.assertEqual("width must be > 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            square = Square(2, -3)
        self.assertEqual("x must be >= 0", str(error.exception))

        with self.assertRaises(ValueError) as error:
            square = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(error.exception))

    def test_update_square_method(self):
        """Test to check update method"""
        square1 = Square(5)
        square1.update(10)
        self.assertEqual(square1.id, 10)

        square1.update(x=12)
        self.assertEqual(square1.x, 12)

        square1.update(size=7, id=89, y=1)
        self.assertEqual(square1.size, 7)
        self.assertEqual(square1.id, 89)
        self.assertEqual(square1.y, 1)

        square1.update()
        self.assertEqual(square1.size, 7)
        self.assertEqual(square1.id, 89)
        self.assertEqual(square1.y, 1)

    def test_update_square_method_with_incorrect_types(self):
        """Test for update method with incorrect types."""
        square = Square(9)
        with self.assertRaises(TypeError) as error:
            square.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            square.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(error.exception))

    def test_to_dictionary_square_method(self):
        """Test for public method to_dictionary."""
        square1 = Square(10, 2, 1)
        square1_dictionary = square1.to_dictionary()
        expected_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(square1_dictionary), len(expected_dictionary))
        self.assertEqual(type(square1_dictionary), dict)

        square2 = Square(1, 1)
        square2.update(**square1_dictionary)
        square2_dictionary = square2.to_dictionary()
        self.assertEqual(len(square1_dictionary), len(square2_dictionary))
        self.assertEqual(type(square2_dictionary), dict)
        self.assertFalse(square1 == square2)

    def test_to_dictionary_square_method_with_incorrect_args(self):
        """Test to_dictionary method with incorrect args."""
        error_message = (
            "to_dictionary() takes 1 positional argument "
            "but 2 were given"
        )
        with self.assertRaises(TypeError) as error:
            square1 = Square(10, 2, 1, 9)
            square1.to_dictionary("Hi")
        self.assertEqual(error_message, str(error.exception))


if __name__ == "__main__":
    unittest.main()

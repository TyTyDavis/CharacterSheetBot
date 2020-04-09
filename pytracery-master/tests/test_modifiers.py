#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Unit tests for pytracery
"""
from __future__ import print_function
import unittest

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from tracery import modifiers


class TestModifiers(unittest.TestCase):

    def test_replace(self):
        # Arrange
        text = "a big ship"

        # Act
        output = modifiers.replace(text, "ship", "shop")

        # Assert
        self.assertEqual(output, "a big shop")

    def test_capitalize_all(self):
        # Arrange
        text = "abc def"

        # Act
        output = modifiers.capitalizeAll(text)

        # Assert
        self.assertEqual(output, "Abc Def")

    def test_capitalize_(self):
        # Arrange
        text = "abc def"

        # Act
        output = modifiers.capitalize_(text)

        # Assert
        self.assertEqual(output, "Abc def")

    def test_a_consonant(self):
        # Arrange
        text = "house"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a house")

    def test_a_consonant_uppercase(self):
        # Arrange
        text = "HOUSE"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a HOUSE")

    def test_a_u_something_i(self):
        # Arrange
        text = "unicorn"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a unicorn")

    def test_a_u_something_i_uppercase(self):
        # Arrange
        text = "UNICORN"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a UNICORN")

    def test_a_u_not_i(self):
        # Arrange
        text = "underdog"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an underdog")

    def test_a_u_not_i_uppercase(self):
        # Arrange
        text = "UNDERDOG"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an UNDERDOG")

    def test_a_vowel(self):
        # Arrange
        text = "elephant"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an elephant")

    def test_a_vowel_uppercase(self):
        # Arrange
        text = "ELEPHANT"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an ELEPHANT")

    def test_first_s(self):
        # Arrange
        text = "elephant in a phonebox"

        # Act
        output = modifiers.firstS(text)

        # Assert
        self.assertEqual(output, "elephants in a phonebox")

    def test_first_s_uppercase(self):
        # Arrange
        text = "ELEPHANT IN A PHONEBOX"

        # Act
        output = modifiers.firstS(text)

        # Assert
        self.assertEqual(output, "ELEPHANTs IN A PHONEBOX")

    def test_s_ends_in_x(self):
        # Arrange
        text = "box"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "boxes")

    def test_s_ends_in_x_uppercase(self):
        # Arrange
        text = "BOX"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "BOXes")

    def test_s_ends_in_non_s(self):
        # Arrange
        text = "goat"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "goats")

    def test_s_ends_in_non_s_uppercase(self):
        # Arrange
        text = "GOAT"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "GOATs")

    def test_s_ends_in_vowel_y(self):
        # Arrange
        text = "monkey"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "monkeys")

    def test_s_ends_in_vowel_y_uppercase(self):
        # Arrange
        text = "MONKEY"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "MONKEYs")

    def test_s_ends_in_y_but_not_vowel_y(self):
        # Arrange
        text = "telly"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "tellies")

    def test_s_ends_in_y_but_not_vowel_y_uppercase(self):
        # Arrange
        text = "TELLY"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "TELLies")

    def test_ed_ends_in_e(self):
        # Arrange
        text = "glide"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "glided")

    def test_ed_ends_in_e_uppercase(self):
        # Arrange
        text = "GLIDE"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "GLIDEd")

    def test_ed_ends_in_y_but_not_vowel_y(self):
        # Arrange
        text = "shimmy"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "shimmied")

    def test_ed_ends_in_y_but_not_vowel_y_uppercase(self):
        # Arrange
        text = "SHIMMY"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "SHIMMied")

    def test_ed_ends_in_non_e_and_non_y(self):
        # Arrange
        text = "jump"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "jumped")

    def test_ed_ends_in_non_e_and_non_y_uppercase(self):
        # Arrange
        text = "JUMP"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "JUMPed")

    def test_uppercase(self):
        # Arrange
        text = "jump up"

        # Act
        output = modifiers.uppercase(text)

        # Assert
        self.assertEqual(output, "JUMP UP")

    def test_uppercase_uppercase(self):
        # Arrange
        text = "JUMP UP"

        # Act
        output = modifiers.uppercase(text)

        # Assert
        self.assertEqual(output, "JUMP UP")

    def test_lowercase(self):
        # Arrange
        text = "GET DOWN"

        # Act
        output = modifiers.lowercase(text)

        # Assert
        self.assertEqual(output, "get down")

    def test_lowercase_lowercase(self):
        # Arrange
        text = "get down"

        # Act
        output = modifiers.lowercase(text)

        # Assert
        self.assertEqual(output, "get down")


if __name__ == "__main__":
    unittest.main()

# End of file

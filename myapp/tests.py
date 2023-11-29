import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, recipes, add_recipe, help_command


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 564671702
        start(message)

    def test_recipes(self):
        message = MagicMock()
        message.chat.id = 564671702
        recipes(message)

    def test_add_recipe(self):
        message = MagicMock()
        message.chat.id = 564671702
        add_recipe(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 564671702
        help_command(message)


if __name__ == '__main__':
    unittest.main()
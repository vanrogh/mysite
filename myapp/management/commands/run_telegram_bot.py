from django.core.management.base import BaseCommand
import telebot

from myapp.models import Recipes

bot = telebot.TeleBot("6422647966:AAGQEQNqPpF_4R_BHW7IwTuYp_owi38mg2k") # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['recipes'])
def recipes(message):
    recipes = Recipes.objects.all()
    for recipe in recipes:
        bot.send_message(message.chat.id, f"Название: {recipe.name}\nИнгредиенты: {recipe.ingredients}")

@bot.message_handler(commands=['add'])
def add_recipe(message):
    # Получаем текст сообщения после команды /add
    command_args = message.text.split(' ', 2)

    if len(command_args) == 3:
        recipe_name = command_args[1]
        recipe_ingredients = command_args[2]

        # Создаем новый рецепт и сохраняем его в базу данных
        new_recipe = Recipes(name=recipe_name, ingredients=recipe_ingredients)
        new_recipe.save()

        bot.send_message(message.chat.id, f"Рецепт '{recipe_name}' успешно добавлен!")
    else:
        bot.send_message(message.chat.id, "Используйте команду /add <recipe_name> <recipe_ingredients>")

@bot.message_handler(commands=['help'])
def help_command(message):
    # Вывод списка команд
    commands = [
        "/start - Начать бота",
        "/recipes - Показать список рецептов",
        "/add <recipe_name> <recipe_ingredients> - Добавить рецепт",
        "/help - Показать список всех команд"
    ]
    bot.send_message(message.chat.id, "\n".join(commands))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


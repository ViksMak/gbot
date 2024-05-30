import telebot


TOKEN = "6762846526:AAH3kYblBg6ZzBGtCv45i1RL-ljjzrUGw0Q"

bot = telebot.TeleBot(TOKEN)

students = {
    "Макшеева Виктория": [5, 5, 5, 5],
    "Санькова Анна": [2, 2, 2, 2],
    "Кукушкина Алина": [5, 4, 5, 4],
    "Романов Степан": [4, 5, 5, 3],
    "Ситник Роман": [4, 5, 2, 3]
}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в чат-бот родителей в классе! Чтобы посмотреть успеваемость своего "
                          "ребенка, введите его фамилию и имя.")


@bot.message_handler(func=lambda message: True)
def check_progress(message):
    child_name = message.text

    if child_name in students:
        grades = students[child_name]
        average_grade = sum(grades) / len(grades)
        bot.reply_to(message, f"Успеваемость ребенка {child_name} - средний балл {average_grade}")
    else:
        bot.reply_to(message, "Ребенок с таким именем не найден. Попробуйте еще раз.")


bot.polling()

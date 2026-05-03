from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Допомога')],
                                    [KeyboardButton(text='Контакти')],
                                    [KeyboardButton(text='Завершити'),
                                    KeyboardButton(text='Розпочати')]],
                                   resize_keyboard=True,
                                   input_field_placeholder='Виберіть пункт меню')
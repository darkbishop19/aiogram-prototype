from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app import text_samples


async def get_user_main_keyboard_markup():
    builder = ReplyKeyboardBuilder()
    button_about_us = KeyboardButton(text=text_samples.about_us)
    button_profile = KeyboardButton(text=text_samples.profile)
    button_vpn = KeyboardButton(text=text_samples.your_vpn)
    button_products = KeyboardButton(text=text_samples.products_about)
    button_referral = KeyboardButton(text=text_samples.referral_programm)
    button_support = KeyboardButton(text=text_samples.support)
    builder.row(button_products)
    builder.row(button_profile, button_vpn)
    builder.row(button_about_us, button_support, button_referral)
    return builder.as_markup(resize_keyboard=True,
                             input_field_placeholder='Выберите пункт главного меню')

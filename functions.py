from configparser import ConfigParser
import os, asyncio
from pyrogram.errors import PasswordHashInvalid
from pyrogram.errors.exceptions.unauthorized_401 import SessionPasswordNeeded
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors.exceptions.bad_request_400 import PhoneCodeInvalid
from pyrogram import Client, types


def gen_config():
    open('config.ini', 'w').write('')
    (config := ConfigParser()).read('config.ini', encoding='UTF-8')
    config.add_section('GENERAL')
    print('Приложению потребуются некоторые ваши данные. '
          'Введите их. Это потребуется сделать только один раз, '
          'после чего вы всегда сможете изменить значения в файле config.ini')
    config['GENERAL']['API_ID'] = input('API-ID: ')
    config['GENERAL']['API_HASH'] = input('API-HASH: ')
    config['GENERAL']['DELAY'] = input('Задержка в секундах (Будет разброс от DELAY/1.5 до DELAY*1.5): ')
    config['GENERAL']['MAX_TOKENS'] = input('Максимальное количество символов в комментарии: ')
    config.write(open('config.ini', 'w'))


def init():
    gen_config() if not os.path.exists('config.ini') else ''
    with open('channels.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    with open('channels.txt', 'w', encoding='UTF-8') as file:
        file.writelines(line for line in lines if line.rstrip())

    open('black_list.txt', 'w').write('') if not os.path.exists('black_list.txt') else ''
    os.mkdir('sessions') if not os.path.exists('sessions') else ''


def gen_sess(name_sess):
    (config := ConfigParser()).read('config.ini', encoding='UTF-8')

    app = Client(f'sessions/{name_sess}', api_id=config['GENERAL']['API_ID'], api_hash=config['GENERAL']['API_HASH'])

    app.connect()

    while True:
        phone_number = input("Введите ваш номер телефона: ")
        try:
            sent_code_info = app.send_code(phone_number)
            break
        except PhoneNumberInvalid:
            print('Номер телефона неверный! Попробуйте ещё раз!')

    phone_code = input("Код был выслан. Введите его, пожалуйста: ")
    while True:
        try:
            app.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)
            break

        except PhoneCodeInvalid:
            print('Код неправильный!')
            phone_code = input("Введите код: ")

        except SessionPasswordNeeded:
            password = input("У вас стоит пароль. Введите его: ")
            while True:
                try:
                    app.check_password(password)
                    break
                except PasswordHashInvalid:
                    print('Пароль неверный!')
                    password = input("Введите пароль: ")

    app.disconnect()
    if input('Хотели бы вы использовать эту сессию по умолчанию? (y/n): ').lower() == 'y':
        config['GENERAl']['DEFAULT'] = name_sess
        config.write(open('config.ini', 'w', encoding='UTF-8'))


async def check_flags(message: types.Message):
    conditions = {
        'imagehasnocaption': (not message.caption and bool(message.photo)),
        'videohasnocaption': (not message.caption and bool(message.video)),
        'posthasnocaption': (not message.caption),
        'isvideo': (bool(message.video)),
        'isphoto': (bool(message.photo)),
        'isvoice': (bool(message.voice)),
        'isdocument': (bool(message.document)),
        'isgif': (bool(message.animation)),
        'issticker': (bool(message.sticker))
    }

    (config := ConfigParser()).read('config.ini', encoding='UTF-8')

    if not config.has_section('FLAGS'):
        return True

    for i in config.options('FLAGS'):
        if conditions[i] and config['FLAGS'][i] == 'False':
            return False

    return True

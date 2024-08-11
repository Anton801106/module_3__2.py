#"Способы вызова функции"


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    if not ('@' in recipient and '@' in sender and sender.endswith(('.com', '.ru', '.net'))
            and recipient.endswith(('.com', '.ru', '.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru', sender = 'university.help@gmail.ru')

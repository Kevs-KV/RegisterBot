import re


async def validations_phone(phone, country):
    valid_phone = [int(nomber) for nomber in phone if nomber.isdigit()]
    try:
        if country in ['Belarus', 'Беларусь']:
            if valid_phone[:3:] == [3, 7, 5]:
                phone = '+{}{}{}({}{}){}{}{}-{}{}-{}{}'.format(*valid_phone)
                return phone
            return None
        elif country == ['Russia', 'Россия']:
            if valid_phone[0] == 7:
                phone = '+{}({}{}{}){}{}{}-{}{}-{}{}'.format(*valid_phone)
                return phone
            return None
        elif country == ['England', 'Великобритания']:
            if valid_phone[:2:] == [4, 4]:
                phone = '+{}{}({}{}{}){}{}{}-{}{}{}{}'.format(*valid_phone)
                return phone
            return None
        return None
    except:
        return None


async def validations_email(email):
    pattern_email = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    if re.match(pattern_email, email) is not None:
        return True
    return False


async def validations_fullname(name):
    pattern_name = r"^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$"
    if re.match(pattern_name, name.title()) is not None:
        return True
    return False

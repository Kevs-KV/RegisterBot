from middlewares.language_moddleware import get_lang


async def validations_phone(user_id, phone):
    print('старт')
    user_lang = await get_lang(user_id)
    valid_phone = [int(nomber) for nomber in phone if nomber.isdigit()]
    print(valid_phone[:2:])
    if len(valid_phone) == 0:
        return None
    if user_lang == 'ru':
        if valid_phone[0] == 7:
            phone = '+{}({}{}{}){}{}{}-{}{}-{}{}'.format(*valid_phone)
            return phone
        elif valid_phone[:3:] == [3, 7, 5]:
            phone = '+{}{}{}({}{}){}{}{}-{}{}-{}{}'.format(*valid_phone)
            return phone
        else:
            return None
    elif user_lang == 'en':
        if valid_phone[:2:] == [4, 4]:
            phone = '+{}{}({}{}{}){}{}{}-{}{}{}{}'.format(*valid_phone)
            return phone
        else:
            return None
    else:
        return None



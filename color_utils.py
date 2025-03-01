def hex_to_rgb(hex_color = "000000"):
    # Принимает строку в формате #FFAAFF или 55DD00
    # Возвращает RGB цвет в формате списка
    rgb = [0, 0, 0]
    rgb[0] = int(hex_color[-6:-4], 16)
    rgb[1] = int(hex_color[-4:-2], 16)
    rgb[2] = int(hex_color[-2:], 16)

    return rgb

def rgb_to_hex(rgb = [0, 0, 0], prefix=True):
    # Принимает список или кортеж чисел с цветами RGB, а также наличие префикса "#"
    # Возвращает HEX цвет в формате строки
    hex = "0123456789ABCDEF"
    ans = ""

    for i in range(len(rgb)):
        x = rgb[i]
        sub = ""
        while x != 0:
            sub += hex[x % 16]
            x //= 16
        if len(sub) == 1:
            sub *= 2
        elif len(sub) == 0:
            sub = "00"
        ans += sub

    return ("#" * prefix) + ans

def anaylyze_color(color = "000000"):
    # Принимает список или кортеж чисел с цветами RGB, или строку HEX
    # Возвращает *вероятное* название цвета
    if type(color) is str:
        color = hex_to_rgb(color)

    r, g, b = color
    # это шуточная функция которая работает не точно! все коэфф. подобраны на рандом
    if r > 94 and g < 95 and b < 95:
        return "Красный"
    elif r < 95 and g > 94 and b < 95:
        return "Зелёный"
    elif r < 95 and g < 95 and b > 94:
        return "Синий"
    elif r > 94 and g > 94 and b < 95:
        return "Жёлтый"
    elif r > 94 and g < 95 and b > 94:
        return "Фиолетовый"
    elif r < 95 and g > 94 and b > 94:
        return "Бирюзовый"
    elif r > 94 and g > 94 and b > 94:
        return "Белый"
    elif r < 20 and g < 20 and b < 20:
        return "Чёрный"
    else:
        return "Программа не распознала цвет"
from color_utils import *

# Пример перевода в RGB
color = "224ebd"
print(f"HEX цвет {color} в RGB формате:", hex_to_rgb(color))
print(f"Вероятное название цвета {color}: {anaylyze_color(color)}")

# Пример перевода в HEX
color = (90, 237, 210)
print(f"RGB цвет {color} в HEX формате:", rgb_to_hex(color))
print(f"Вероятное название цвета {color}: {anaylyze_color(color)}")
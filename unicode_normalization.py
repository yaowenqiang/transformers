import unicodedata
from icecream import ic
print("\u00C7", "\u0043"+"\u0327")
print("\u00C7", "\u0043", "\u0327")

# decomposition(分解)
s = "𠮷国"  # 这是一个复合字符，包含一个变音符号

decomposed = unicodedata.normalize('NFD', s)

print(decomposed)  # 输出会是 "ｷ国"

c_with_cedilla = "\u00C7"  # Latin capital C with cedilla (single character)
c_plus_cedilla = "\u0043\u0327"  # \u0043 = Latin capital C, \u0327 = 'combining cedilla' (two characters)
ic(c_with_cedilla == c_plus_cedilla)
ic(unicodedata.normalize('NFD', c_with_cedilla) == c_plus_cedilla)

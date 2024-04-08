import unicodedata
from icecream import ic
print("\u00C7", "\u0043"+"\u0327")
print("\u00C7", "\u0043", "\u0327")

# decomposition(分解)
s = "𠮷国"  # 这是一个复合字符，包含一个变音符号

decomposed = unicodedata.normalize('NFD', s)

print(decomposed)  # 输出会是 "ｷ国"

c_with_cedilla = "\u00C7"  # Latin capital C with cedilla (single character)
c_plus_cedilla = "\u0043\u0327"  # \u0043 = Latin capital C, \u0327 = 'combining cedilla' (two characters) ic(c_with_cedilla == c_plus_cedilla)

ic(c_with_cedilla)
ic(unicodedata.normalize('NFD', c_with_cedilla))
ic(unicodedata.normalize('NFC', c_with_cedilla))
ic(unicodedata.normalize('NFKD', c_with_cedilla))
ic(unicodedata.normalize('NFKC', c_with_cedilla))


ic(unicodedata.normalize('NFD', c_with_cedilla) == c_plus_cedilla)
ic(unicodedata.normalize('NFC', c_with_cedilla) == c_plus_cedilla)
ic(unicodedata.normalize('NFKD', c_with_cedilla) == c_plus_cedilla)
ic(unicodedata.normalize('NFKC', c_with_cedilla) == c_plus_cedilla)

ic(unicodedata.normalize('NFC', 'ℌ'))
ic(unicodedata.normalize('NFD', 'ℌ'))
ic(unicodedata.normalize('NFKD', 'ℌ'))
ic(unicodedata.normalize('NFKC', 'ℌ'))

circle_chars = "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ'"
ic(unicodedata.normalize('NFC', circle_chars))
ic(unicodedata.normalize('NFD', circle_chars))
ic(unicodedata.normalize('NFKC', circle_chars))
ic(unicodedata.normalize('NFKD', circle_chars))


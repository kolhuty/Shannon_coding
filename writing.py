def write_compressed(codes, text, filename):
    """
    Преобразует исходный текст в сжатый.
    Используется для encode
    """
    bit_string = ''.join(codes[char] for char in text)

    #Дополняем нулями до целого числа байт
    padding = 8 - len(bit_string) % 8
    bit_string += '0' * padding

    #Конвертируем битовую строку в байты
    bytes_data = bytes(
        int(bit_string[i:i + 8], 2)
        for i in range(0, len(bit_string), 8)
    )

    with open(filename, 'wb') as f:
        f.write(bytes_data)

def write_decode_data(bytes_data, filename):
    """Записывает байт-код в файл"""
    with open(filename, 'wb') as f:
        f.write(bytes_data)
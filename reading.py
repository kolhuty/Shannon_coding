from collections import defaultdict

def find_frequencies(file_path: str) -> dict:
    """
    Считывает файл побайтово и строит по нему словарь частот встречающихся символов.
    Используется для encode
    """
    frequency = defaultdict(int)
    total_count = 0

    with open(file_path, 'rb') as file:
        while True:
            byte = file.read(1)
            if byte == b'':
                break

            sym = byte[0]
            frequency[sym] += 1
            total_count += 1

    freq = {sym: count/total_count for sym, count in frequency.items()}

    return freq

def json_codes(file_path: str) -> dict:
    """Считывает json-файл сo словарем для декодирования"""
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return {int(k): v for k, v in data.items()}

def byte_text(file_path: str) -> bytes:
    """Считывает файл полностью"""
    with open(file_path, 'rb') as f:
        text = f.read()
    return text

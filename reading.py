from collections import defaultdict

def find_frequencies(file_path: str) -> dict:
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
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_freq

def byte_text(file_path: str) -> bytes:
    with open(file_path, 'rb') as f:
        text = f.read()
    return text

import sys
import reading
import writing
from encoding import Encode
from decoding import Decode


def handle_encoding(file_path, filename_output="output.bin"):
    try:
        text = reading.byte_text(file_path)
        freq = reading.find_frequencies(file_path)
        encoder = Encode(freq)
        codes = encoder.get_codes()
        writing.write_compressed(codes, text, filename_output)
        writing.dict_to_json(codes)
    except FileNotFoundError:
        sys.stderr.write("\nFile not found\n")
        sys.exit(3)

def handle_decoding(codes_file, file_path, file_output="output_dec.bin"):
    try:
        codes = reading.json_codes(codes_file)
        text = reading.byte_text(file_path)
        bytes_data = Decode.decoding(Decode(codes), text)
        writing.write_decode_data(bytes_data, file_output)
    except FileNotFoundError:
        sys.stderr.write("\nFile not found\n")
        sys.exit(3)

def parse_arguments(args: list[str]):
    """Парсит аргументы командной строки."""
    result = {
        'decode': False,
        'dict': None,
        'input': False,
        'output': False,
        'help': False,
        'error': None
    }

    valid_args = {"-d", "-o", "--help"}
    unknown = [a for a in args if a not in valid_args]

    if len(unknown) > 3:
        result['error'] = "Unknown options or arguments"
        return result

    if "--help" in args:
        result['help'] = True
        return result

    if "-d" in args:
        result['decode'] = True
        if len(unknown) >= 2:
            result['dict'] = unknown[1]
            result['input'] = unknown[0]
            if "-o" in args and len(unknown) == 3:
                result['output'] = unknown[2]
        else:
            result['error'] = "Dictionary file or input file missing"

    else:
        result['encode'] = True
        if len(unknown) >= 1:
            result['input'] = unknown[0]
            if "-o" in args and len(unknown) == 2:
                result['output'] = unknown[1]
        else:
            result['error'] = "Input file missing"

    return result

def show_help():
    """Показывает справку."""
    with open("help.txt", "rb") as f:
        sys.stdout.buffer.write(f.read())

def main():
    """Основная логика программы."""
    args = parse_arguments(sys.argv[1:])

    if args['error']:
        sys.stderr.write(f"Error: {args['error']}\n")
        sys.exit(1)

    if args['help']:
        show_help()
        sys.exit(0)

    try:
        if args['decode']:
            if args['output']:
                handle_decoding(args['dict'], args['input'], args['output'])
            else:
                handle_decoding(args['dict'], args['input'])
        else:
            if args['output']:
                handle_encoding(args['input'], args['output'])
            else:
                handle_encoding(args['input'])

    except Exception:
        sys.stderr.write("\nException\n")
        sys.exit(2)

if __name__ == '__main__':
    main()
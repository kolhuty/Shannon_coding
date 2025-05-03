import sys
import reading
import tree_code
import writing


def handle_encoding(file_path, filename_output="output.bin"):
    text = reading.byte_text(file_path)
    freq = reading.find_frequencies(file_path)
    tree = tree_code.build_shanon_tree(freq)
    codes = tree_code.coding(tree)
    writing.write_compressed(codes, text, filename_output)
    return codes

def handle_decoding():
    pass

def shanon_main():
    """Основная логика программы."""
    arg = sys.argv[1]

    try:
        if arg == '-d':
            handle_decoding()
        else:
            handle_encoding(sys.argv[2])

    except Exception:
        sys.stderr.write("\nOperation cancelled\n")
        sys.exit(1)

if __name__ == '__main__':
    shanon_main()
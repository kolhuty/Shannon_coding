# Shannon Encoder/Decoder Tool  

Usage:  
  Encode: ./program INPUT_FILE [OPTIONS]  
  Decode: ./program -d INPUT_FILE DICT_FILE [OPTIONS]  

Options:  
  -d          Decode mode (requires dictionary)  
  -o FILE     Output file [default: output.bin for encode, output_dec.bin for decode]  
  --help      Show help  
  
### Encode mode  
На вход поступает двоичный файл, на выходе получаем двоичный файл с сжатым текстом и json-файл со словарем для декодировки.  
### Decode mode  
На вход поступает сжатый двоичный файл и словарь для декодирования, на выходе получаем рассшифрованный двоичный файл.  
  
## Пример использования:  
Кодировка: ./main.py Example/test_data  
Декодировка: ./main.py -d Example/output.bin Example/codes.json  
  
В папке Example представлены файлы для примера.  

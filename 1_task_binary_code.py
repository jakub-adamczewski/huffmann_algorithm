import math
import filecmp
import util


def get_possible_chars_count():
    alphabet_size = 26  # only small letters
    numbers_count = 10
    spaces = 1
    return alphabet_size + numbers_count + spaces


def get_code_word_size(possible_chars_count: int):
    code_word_capacity = 2
    while possible_chars_count > code_word_capacity:
        code_word_capacity *= 2
    return code_word_capacity, int(math.log(code_word_capacity, 2))


def get_binary(num: int, size: int):
    return format(num, f'0{size}b')


def chunked(data, chunk_size: int):
    return [data[i: i + chunk_size] for i in range(0, len(data), chunk_size)]


def encode(input_path, output_path, code_word_size: int):
    letter_to_code_dict = {}
    current_num = 0
    with open(file=input_path, mode="r") as file_in:
        with open(file=output_path, mode="w") as file_out:
            for char in file_in.read():
                try:
                    encoded_char = letter_to_code_dict[char]
                except KeyError:
                    encoded_char = get_binary(num=current_num, size=code_word_size)
                    letter_to_code_dict[char] = encoded_char
                    current_num += 1
                file_out.write(encoded_char)

    return util.reverse_keys_with_values(letter_to_code_dict)


def decode(input_path, output_path, translations: dict, code_word_size: int):
    with open(file=input_path, mode="r") as file_in:
        with open(file=output_path, mode="w") as file_out:
            for encoded_char in chunked(data=file_in.read(), chunk_size=code_word_size):
                decoded_char = translations[encoded_char]
                file_out.write(decoded_char)


if __name__ == '__main__':
    input_file = 'files/norm_wiki_sample.txt'
    encoded_file = 'files/1_task/encoded.txt'
    decoded_file = 'files/1_task/decoded.txt'

    possible_chars_count = get_possible_chars_count()
    print(f'possible_chars_count: {possible_chars_count}')

    code_word_capacity, code_word_size = get_code_word_size(possible_chars_count=possible_chars_count)
    print(f'code_word_capacity: {code_word_capacity}')
    print(f'code_word_size: {code_word_size}')

    print('Encoding...')
    translations = encode(input_path=input_file, output_path=encoded_file, code_word_size=code_word_size)
    print('Decoding...')
    decode(input_path=encoded_file, output_path=decoded_file, translations=translations, code_word_size=code_word_size)

    files_same = filecmp.cmp(input_file, decoded_file)
    print(f'Is decoded identical to input?: {files_same}')

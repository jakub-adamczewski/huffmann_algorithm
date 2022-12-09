import huffmann
import util
import filecmp


def huffmann_encode(input_path, output_path, letter_to_code_dict):
    with open(file=input_path, mode="r") as file_in:
        with open(file=output_path, mode="w") as file_out:
            for char in file_in.read():
                encoded_char = letter_to_code_dict[char]
                file_out.write(encoded_char)


def huffmann_decode(input_path, output_path, code_to_letter_dict):
    with open(file=input_path, mode="r") as file_in:
        with open(file=output_path, mode="w") as file_out:
            current_code = ''
            for char in file_in.read():
                current_code += char
                if current_code in code_to_letter_dict:
                    file_out.write(code_to_letter_dict[current_code])
                    current_code = ''


if __name__ == '__main__':
    input_file = 'files/norm_wiki_sample.txt'
    encoded_file = 'files/2_task/encoded.txt'
    decoded_file = 'files/2_task/decoded.txt'

    with open(file=input_file, mode="r") as file_in:
        text = file_in.read()

    huffmann_codes = huffmann.get_huffman_coding(text, True)

    print('Encoding...')
    huffmann_encode(
        input_path=input_file,
        output_path=encoded_file,
        letter_to_code_dict=huffmann_codes
    )

    print('Decoding...')
    huffmann_decode(
        input_path=encoded_file,
        output_path=decoded_file,
        code_to_letter_dict=util.reverse_keys_with_values(huffmann_codes)
    )

    files_same = filecmp.cmp(input_file, decoded_file)
    print(f'Is decoded identical to input?: {files_same}')

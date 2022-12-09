import entropies
import quantities


def get_compression_ratio(file_before_compression: str, file_after_compression: str):
    with open(file=file_before_compression, mode="r") as file_b:
        with open(file=file_after_compression, mode="r") as file_a:
            return len(file_b.read()) / len(file_a.read())


def get_coding_efficiency(
        file_before_compression: str,
        file_after_compression: str,
):
    with open(file=file_before_compression, mode="r") as file_b:
        with open(file=file_after_compression, mode="r") as file_a:
            (letters_quantities, all_letters_count) = quantities.get_x_chars_quantities(
                file=file_before_compression,
                x=1
            )
            prob_list = list(map(lambda x: x / all_letters_count, letters_quantities.values()))
            H = entropies.get_entropy(prob_list)
            L = len(file_a.read()) / len(file_b.read())
            return H / L


# Stopień kompresji jest na korzyść algorytmu Huffmanna, udowadnia, że zużywa on średnio mniej bitów na zakodowanie znaku pliku wejściowego.
# Efektywność kodowania również jest na korzyść algorytmu Huffmanna, jest bliska maksymalnej możliwej efektywności.
if __name__ == '__main__':
    input_file = 'files/norm_wiki_sample.txt'

    encoded_file_binary = 'files/1_task/encoded.txt'
    cr_binary = get_compression_ratio(
        file_before_compression=input_file,
        file_after_compression=encoded_file_binary
    )
    print(f'Binary compression ratio: {cr_binary}')
    eff_binary = get_coding_efficiency(
        file_before_compression=input_file,
        file_after_compression=encoded_file_binary
    )
    print(f'Binary coding efficiency: {eff_binary}')

    encoded_file_huffmann = 'files/2_task/encoded.txt'
    cr_huffmann = get_compression_ratio(
        file_before_compression=input_file,
        file_after_compression=encoded_file_huffmann
    )
    print(f'Huffmann compression ratio: {cr_huffmann}')
    eff_huffmann = get_coding_efficiency(
        file_before_compression=input_file,
        file_after_compression=encoded_file_huffmann
    )
    print(f'Huffmann coding efficiency: {eff_huffmann}')

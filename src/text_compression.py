def count_compressed_bits(text, default_size, encoding_map) -> int:
    total_bits_compressed = 0
    for c in text:
        if c in encoding_map:
            total_bits_compressed += encoding_map[c]
        else:
            total_bits_compressed += default_size
    return total_bits_compressed


def compress_text(text, encoding_map, default_bits = 8) -> tuple:
    text_len = len(text)
    char_counts = {k: text.count(k) for k in set(text)}

    most_common_chars = sorted(char_counts, key= lambda x: char_counts[x], reverse=True)  
    lowest_bits = sorted(encoding_map.values())
    optimised_encoding_map = dict(zip(most_common_chars, lowest_bits))

    no_compression = count_compressed_bits(text, default_bits, {})
    actual_compression = count_compressed_bits(text, default_bits, encoding_map)
    optimised_compression = count_compressed_bits(text, default_bits, optimised_encoding_map)

    for k, v in vars().items():
        print(f"{k} = {v}")

    return (
        text, 
        encoding_map,
        default_bits,
        text_len, 
        char_counts,
        most_common_chars,
        lowest_bits,
        optimised_encoding_map,
        no_compression,
        actual_compression,
        optimised_compression,
    )
def count_compressed_bits(text, default_size, encoding_map) -> int:
    total_bits_compressed = 0
    for c in text:
        if c in encoding_map:
            total_bits_compressed += encoding_map[c]
        else:
            total_bits_compressed += default_size
    return total_bits_compressed


def compress_text(text, encoding_map, default_bits=8) -> tuple:
    text_len = len(text)
    char_counts = {k: text.count(k) for k in set(text)}

    all_chars_by_freq = sorted(char_counts, key=lambda x: char_counts[x], reverse=True)
    encoded_chars_by_freq = [c for c in all_chars_by_freq if c in encoding_map] + [
        c for c in encoding_map if c not in all_chars_by_freq
    ]

    lowest_bits = sorted(encoding_map.values())
    optimised_encoding_map = dict(zip(encoded_chars_by_freq, lowest_bits))
    true_optimised_encoding_map = dict(zip(all_chars_by_freq, lowest_bits))

    no_compression = count_compressed_bits(text, default_bits, {})
    actual_compression = count_compressed_bits(text, default_bits, encoding_map)
    optimised_compression = count_compressed_bits(
        text, default_bits, optimised_encoding_map
    )
    true_optimised_compression = count_compressed_bits(
        text, default_bits, true_optimised_encoding_map
    )

    actual_compression_ratio = no_compression / actual_compression
    optimised_compression_ratio = no_compression / optimised_compression
    true_optimised_compression_ratio = no_compression / true_optimised_compression

    for k, v in vars().items():
        print(f"{k} = {v}")

    return (
        text,
        encoding_map,
        default_bits,
        text_len,
        char_counts,
        all_chars_by_freq,
        lowest_bits,
        optimised_encoding_map,
        no_compression,
        actual_compression,
        optimised_compression,
        actual_compression_ratio,
        optimised_compression_ratio,
        true_optimised_compression_ratio,
    )

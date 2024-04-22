EQUATIONS = [
    {
        "name": "compute_density",
        "syms": ["compute_density", "max_mips", "volume"],
        "equation": "max_mips / volume",
    },
    {
        "name": "power_density",
        "syms": ["power_density", "power", "volume"],
        "equation": "power / volume",
    },
    {
        "name": "cost_efficiency",
        "syms": ["cost_efficiency", "price", "max_mips"],
        "equation": "price / max_mips",
    },
    {
        "name": "cost_of_running_computer_for_n_secs",
        "syms": [
            "cost_of_running_computer_for_n_secs",
            "n_secs",
            "power_consumption_per_sec",
            "cost_per_sec",
            "base_cost",
        ],
        "equation": "n_secs * power_consumption_per_sec * cost_per_sec + base_cost",
    },
    {"name": "max_speedup", "syms": ["max_speedup", "P"], "equation": "1 / (1 - P)"},
    {
        "name": "true_speedup",
        "syms": ["true_speedup", "P", "n"],
        "equation": "1 / ((1 - P) + (P / n))",
    },
    {
        "name": "gustafsons_law",
        "syms": ["gustafsons_law", "P", "n"],
        "equation": "(1 - P) + (P * n)",
    },
    {
        "name": "branch_prediction_saving_time",
        "syms": [
            "branch_prediction_saving_time",
            "hit_rate",
            "hit_time_avg",
            "miss_rate",
            "miss_time_avg",
        ],
        "equation": "hit_rate * hit_time_avg - miss_rate * miss_time_avg",
    },
    {
        "name": "n_addressable_locations",
        "syms": ["n_addressable_locations", "total_address_lines"],
        "equation": "2 ** total_address_lines",
    },
    {
        "name": "storage_capacity",
        "syms": ["storage_capacity", "n_addressable_locations", "n_data_lines"],
        "equation": "n_addressable_locations * n_data_lines",
    },
    {
        "name": "cycle_time_normal_mode",
        "syms": [
            "cycle_time_normal_mode",
            "ras",
            "cas",
            "access_time",
            "recovery_cycles",
        ],
        "equation": "ras + cas + access_time + recovery_cycles",
    },
    {
        "name": "cycle_time_n_reads_burst_mode",
        "syms": [
            "cycle_time_n_reads_burst_mode",
            "ras",
            "cas",
            "wait_time",
            "n",
            "read_time",
            "recovery_cycles",
        ],
        "equation": "ras + cas + wait_time + (n * read_time) + recovery_cycles",
    },
    {
        "name": "cycle_time_fast_page_mode",
        "syms": [
            "cycle_time_fast_page_mode",
            "ras",
            "cas",
            "wait_time",
            "n",
            "read_time",
            "recovery_cycles",
        ],
        "equation": "ras + (n * cas) + wait_time + (n * read_time) + recovery_cycles",
    },
    {
        "name": "cycle_time_mode_mixtures",
        "syms": [
            "cycle_time_mode_mixtures",
            "cycle_time_mode1",
            "ratio_mode1",
            "cycle_time_mode2",
            "ratio_mode2",
        ],
        "equation": "cycle_time_mode1 * ratio_mode1 + cycle_time_mode2 * ratio_mode2",
    },
    {
        "name": "data_transfer_rate",
        "syms": ["data_transfer_rate", "bus_width", "cycle_time_total"],
        "equation": "bus_width / cycle_time_total",
    },
    {
        "name": "cache_read_time_avg",
        "syms": [
            "cache_read_time_avg",
            "cache_hit_rate",
            "cache_hit_time_avg",
            "cache_miss_rate",
            "cache_miss_time_avg",
        ],
        "equation": "cache_hit_rate * cache_hit_time_avg + cache_miss_rate * cache_miss_time_avg",
    },
    {
        "name": "cache_miss_time_avg",
        "syms": ["cache_miss_time_avg", "cache_hit_time_avg", "main_memory_read_time"],
        "equation": "cache_hit_time_avg + main_memory_read_time",
    },
    {
        "name": "cycle_time_sec",
        "syms": ["cycle_time_sec", "n_clock_cycles", "clock_freq"],
        "equation": "n_clock_cycles / clock_freq",
    },
    {
        "name": "time_speedup",
        "syms": ["time_speedup", "time_original", "time_new"],
        "equation": "time_original / time_new",
    },
    {
        "name": "cycles_total",
        "syms": ["cycles_total", "cycles_payload", "cycles_overhead"],
        "equation": "cycles_payload + cycles_overhead",
    },
    {
        "name": "bus_data_transfer_rate",
        "syms": [
            "bus_data_transfer_rate",
            "bus_freq",
            "amount_of_data",
            "cycles_total",
        ],
        "equation": "(bus_freq * amount_of_data) / cycles_total",
    },
    {
        "name": "cycles_block",
        "syms": ["cycles_block", "size_block", "size_bus_width"],
        "equation": "size_block / size_bus_width",
    },
    {
        "name": "bus_data_transfer_efficiency",
        "syms": ["bus_data_transfer_efficiency", "cycles_block", "cycles_overhead"],
        "equation": "(cycles_block / (cycles_block + cycles_overhead)) * 100",
    },
    {
        "name": "read_time_synchronous",
        "syms": [
            "read_time_synchronous",
            "time_send_address",
            "time_memory_access",
            "time_send_data",
        ],
        "equation": "time_send_address + time_memory_access + time_send_data",
    },
    {
        "name": "read_time_asynchronous",
        "syms": ["read_time_asynchronous", "time_handshake", "time_memory_access"],
        "equation": "((1 + 3)* time_handshake) + max(time_memory_access, (3 * time_handshake))",
    },
    {
        "name": "bandwidth_max_for_bus",
        "syms": [
            "bandwidth_max_for_bus",
            "n_bytes_to_transfer",
            "read_time_per_block",
            "n_blocks_total",
        ],
        "equation": "n_bytes_to_transfer / (read_time_per_block * n_blocks_total)",
    },
    {
        "name": "disk_revolution_time_sec",
        "syms": ["disk_revolution_time_sec", "rotations_per_min"],
        "equation": " 60 / rotations_per_min",
    },
    {
        "name": "disk_access_time_worst",
        "syms": ["disk_access_time_worst", "time_rotational_latency", "time_head_seek"],
        "equation": "time_rotational_latency + time_head_seek",
    },
    {
        "name": "disk_access_time_avg",
        "syms": ["disk_access_time_avg", "disk_access_time_worst"],
        "equation": "disk_access_time_worst / 2",
    },
    {
        "name": "track_size",
        "syms": ["track_size", "sector_size", "sectors_per_track"],
        "equation": "sector_size * sectors_per_track",
    },
    {
        "name": "data_transfer_rate_disk",
        "syms": ["data_transfer_rate_disk", "track_size", "rotations_per_sec"],
        "equation": "track_size * rotations_per_sec",
    },
    {
        "name": "performance_gain_from_hyperthreading",
        "syms": [
            "performance_gain_from_hyperthreading",
            "n_cores",
            "k_ways_of_hyperthreading",
        ],
        "equation": "n_cores * k_ways_of_hyperthreading",
    },
    {
        "name": "cpu_time_pct_thread",
        "syms": [
            "cpu_time_pct_thread",
            "total_time_slice_thread",
            "switch_time_thread",
        ],
        "equation": "(total_time_slice_thread / (total_time_slice_thread + switch_time_thread)) * 100",
    },
    {
        "name": "time_interval_between_repetitions",
        "syms": [
            "time_interval_between_repetitions",
            "total_time_slice_thread",
            "switch_time_thread",
            "n_tasks",
        ],
        "equation": "(total_time_slice_thread + switch_time_thread) * n_tasks",
    },
    {
        "name": "repetition_freq",
        "syms": ["repetition_freq", "time_interval_between_repetitions"],
        "equation": "1 / time_interval_between_repetitions",
    },
    {
        "name": "compression_ratio",
        "syms": ["compression_ratio", "original_size", "compressed_size"],
        "equation": "original_size / compressed_size",
    },
    {
        "name": "total_network_bandwidth",
        "syms": ["total_network_bandwidth", "raw_bandwidth", "bridge_bandwidth"],
        "equation": "(2 * raw_bandwidth) - bridge_bandwidth",
    },
    {
        "name": "packet_bytes_total",
        "syms": ["packet_bytes_total", "packet_bytes_payload", "packet_bytes_overhead"],
        "equation": "packet_bytes_payload + packet_bytes_overhead",
    },
    {
        "name": "true_data_rate",
        "syms": ["true_data_rate", "raw_data_rate", "efficiency"],
        "equation": "raw_data_rate * efficiency",
    },
    {
        "name": "packet_latency",
        "syms": ["packet_latency", "packet_size", "raw_data_rate"],
        "equation": "packet_size / raw_data_rate",
    },
    {
        "name": "p_no_failures_in_n_periods",
        "syms": ["p_no_failures_in_n_periods", "p_works", "n"],
        "equation": "p_works ** n",
    },
    {
        "name": "p_exactly_1_failure_among_n_drives_in_1_period",
        "syms": [
            "p_exactly_1_failure_among_n_drives_in_1_period",
            "n",
            "p_1_drive_fails_in_1_period",
            "p_1_drive_works_in_1_period",
        ],
        "equation": "n * p_1_drive_fails_in_1_period * (p_1_drive_works_in_1_period**(n-1))",
    },
    {
        "name": "p_exactly_2_failure_among_n_drives_in_1_period",
        "syms": [
            "p_exactly_2_failure_among_n_drives_in_1_period",
            "n",
            "p_1_drive_fails_in_1_period",
            "p_1_drive_works_in_1_period",
        ],
        "equation": "((n**2 -n) / 2) * (p_1_drive_fails_in_1_period ** 2) * (p_1_drive_works_in_1_period**(n-2))",
    },
]

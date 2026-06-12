CODE FOR GOLDEN RECORD / TEXT FILE
import csv
import itertools
import random
from collections import defaultdict

# Supported characters (excluding digits)
supported_chars = (
    list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") +
    list("abcdefghijklmnopqrstuvwxyz") +
    list(".,!?\"':;-() /")
)

def generate_valid_dna_codes():
    bases = ['A', 'C', 'G', 'T']
    all_combinations = [''.join(p) for p in itertools.product(bases, repeat=4)]
    valid = [seq for seq in all_combinations if not any(seq[i] == seq[i+1] == seq[i+2] == seq[i+3] for i in range(len(seq) - 3))]
    return valid

def build_char_to_dna_map():
    valid_codes = generate_valid_dna_codes()
    if len(valid_codes) < len(supported_chars):
        raise ValueError("Not enough unique DNA codes for characters!")
    random.seed(42)
    random.shuffle(valid_codes)
    char_to_dna = dict(zip(supported_chars, valid_codes[:len(supported_chars)]))

    dna_to_chars = defaultdict(list)
    for ch, dna in char_to_dna.items():
        dna_to_chars[dna].append(ch)
    duplicates = {dna: chars for dna, chars in dna_to_chars.items() if len(chars) > 1}
    if duplicates:
        duplicate_info = "\n".join(f"DNA code '{dna}' maps to characters {chars}" for dna, chars in duplicates.items())
        raise ValueError(f"Duplicate DNA codes detected in mapping:\n{duplicate_info}")
    return char_to_dna

def encode_message_to_dna(message, char_to_dna):
    dna_seq = ''
    for char in message:
        if char not in char_to_dna:
            raise ValueError(f"Unsupported character: '{char}'")
        dna_seq += char_to_dna[char]
    return dna_seq

def encode_csv_to_dna(input_csv_path, char_to_dna):
    full_dna = ''
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        headers = [h.strip() for h in headers]

        try:
            lang_idx = headers.index("Language")
            msg_idx = headers.index("Message")
        except ValueError:
            raise ValueError("CSV must contain 'Language' and 'Message' columns (case-sensitive).")

        for row in reader:
            if len(row) <= max(lang_idx, msg_idx):
                continue
            language = row[lang_idx].strip()
            message = row[msg_idx].strip()
            combined = f"{language}: {message}"
            dna = encode_message_to_dna(combined, char_to_dna)
            full_dna += dna
    return full_dna

def introduce_errors(dna_seq, error_rate_per_kbp):
    bases = ['A', 'C', 'G', 'T']
    seq_list = list(dna_seq)
    length = len(seq_list)
    total_errors = int(length * error_rate_per_kbp / 1000)
    if total_errors == 0:
        return dna_seq, 0

    error_positions = random.sample(range(length), total_errors)
    error_positions.sort()
    errors_applied = 0
    i = 0

    while i < len(error_positions):
        pos = error_positions[i]
        error_type = random.choice(['substitution', 'insertion', 'deletion'])

        if error_type == 'substitution':
            original_base = seq_list[pos]
            substitutes = [b for b in bases if b != original_base]
            seq_list[pos] = random.choice(substitutes)
            errors_applied += 1
            i += 1

        elif error_type == 'insertion':
            insert_base = random.choice(bases)
            seq_list.insert(pos, insert_base)
            errors_applied += 1
            for j in range(i + 1, len(error_positions)):
                if error_positions[j] >= pos:
                    error_positions[j] += 1
            i += 1

        elif error_type == 'deletion':
            seq_list.pop(pos)
            errors_applied += 1
            for j in range(i + 1, len(error_positions)):
                if error_positions[j] > pos:
                    error_positions[j] -= 1
            i += 1

    corrupted_seq = ''.join(seq_list)
    return corrupted_seq, errors_applied

def decode_dna_to_message(dna_seq, char_to_dna):
    dna_to_char = {v: k for k, v in char_to_dna.items()}
    message = ''
    for i in range(0, len(dna_seq) - 3, 4):
        codon = dna_seq[i:i+4]
        message += dna_to_char.get(codon, '?')
    return message

# === MAIN ===
if __name__ == "__main__":
    input_file = 'golden_record.csv'         
    ERROR_RATE_PER_KBP = 5.0                 

    try:
        char_to_dna = build_char_to_dna_map()
        original_dna = encode_csv_to_dna(input_file, char_to_dna)

        print(f"Original DNA length: {len(original_dna)} bases")

        # Output original DNA to file
        with open('original_dna.txt', 'w') as f:
            f.write(original_dna)

        corrupted_dna, total_errors = introduce_errors(original_dna, ERROR_RATE_PER_KBP)
        print(f"Total errors introduced: {total_errors}")
        print(f"Corrupted DNA length: {len(corrupted_dna)} bases")

        # Output corrupted DNA
        with open('corrupted_dna.txt', 'w') as f:
            f.write(corrupted_dna)

        # Print previews
        preview_len = 200
        print("\n--- Original DNA sequence preview ---")
        print(original_dna[:preview_len] + ('...' if len(original_dna) > preview_len else ''))

        print("\n--- Corrupted DNA sequence preview ---")
        print(corrupted_dna[:preview_len] + ('...' if len(corrupted_dna) > preview_len else ''))

        decoded_message = decode_dna_to_message(corrupted_dna, char_to_dna)
        print("\n--- Decoded message from corrupted DNA (with '?' for errors) ---")
        print(decoded_message[:500] + ('...' if len(decoded_message) > 500 else ''))

    except Exception as e:
        print(f"Error: {e}")


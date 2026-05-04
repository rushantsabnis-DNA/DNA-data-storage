CODE FOR MAKING OLIGOPOOL 
import pandas as pd

def reverse_complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict[base] for base in reversed(sequence))

def generate_primers(dna_sequence, forward_primer_length, reverse_primer_length, overlap_length):
    primers = []
    i = 0
    primer_count = 1
    
    while i < len(dna_sequence):
        # Forward primer
        primer_forward = dna_sequence[i:i + forward_primer_length]
        primers.append((f"Forward_{primer_count}", primer_forward))
        
        i += forward_primer_length - overlap_length
        
        if i >= len(dna_sequence):
            break
        
        # Reverse primer
        primer_reverse_seq = dna_sequence[i:i + reverse_primer_length]
        primer_reverse = reverse_complement(primer_reverse_seq)
        primers.append((f"Reverse_{primer_count}", primer_reverse))
        
        i += reverse_primer_length - overlap_length
        primer_count += 1
        
    return primers

def split_and_process_dna(full_sequence, forward_universal, reverse_universal, chunk_size=720):
    part_number = 1
    all_data = []

    for i in range(0, len(full_sequence), chunk_size):
        chunk = full_sequence[i:i+chunk_size]

        # Add universal primers
        chunk_with_primers = forward_universal + chunk + reverse_universal

        # Generate primers
        primers = generate_primers(chunk_with_primers, 60, 60, 30)

        # Store data
        for primer_name, primer_seq in primers:
            all_data.append({
                "Part_Number": f"Part_{part_number}",
                "Primer_Name": primer_name,
                "Primer_Sequence": primer_seq
            })
        
        part_number += 1

    # Convert to dataframe
    df = pd.DataFrame(all_data)
    return df

# === Example Usage ===

# Full DNA sequence 
input_dna_sequence = ""

# Universal primers 
universal_forward = "TTTGTTTAACTTTAAGAAGGAGATATACAT"
universal_reverse = "TTCCTTTCGGGCTTTGTTAGCAGCCGGATC"

# Process
primers_df = split_and_process_dna(input_dna_sequence, universal_forward, universal_reverse)

# Save to Excel
primers_df.to_excel("split_primers_output.xlsx", index=False)

# Output to see in console
print(primers_df)

Forward primer used =TTTGTTTAACTTTAAGAAGGAGATATACAT
Reverse primer used =TTCCTTTCGGGCTTTGTTAGCAGCCGGATC

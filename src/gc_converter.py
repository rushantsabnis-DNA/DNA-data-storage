GC CONVERTER/ ENHANCER
def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq)

def evenly_spaced_indices(seq, target_count):
    """
    Return `target_count` evenly spaced indices from `seq`
    """
    if target_count >= len(seq):
        return seq
    step = len(seq) / target_count
    return [seq[int(i * step)] for i in range(target_count)]

def increase_gc_uniformly(dna_seq, target_gc):
    dna_list = list(dna_seq)
    tag = ['0'] * len(dna_list)
    current_gc = gc_content(dna_seq)

    at_positions = [i for i, base in enumerate(dna_list) if base in ('A', 'T')]
    gc_positions = [i for i, base in enumerate(dna_list) if base in ('G', 'C')]

    # Calculate how many bases need to be flipped
    diff = abs(target_gc - current_gc)
    total_change_needed = int(diff * len(dna_seq))

    if total_change_needed == 0:
        return ''.join(dna_list), ''.join(tag)

    # Select positions uniformly across the sequence
    if current_gc < target_gc:
        # Need to flip A → G and T → C
        target_positions = evenly_spaced_indices(at_positions, total_change_needed)
        for pos in target_positions:
            if dna_list[pos] == 'A':
                dna_list[pos] = 'G'
            elif dna_list[pos] == 'T':
                dna_list[pos] = 'C'
            tag[pos] = '1'

    else:
        # Need to flip G → A and C → T
        target_positions = evenly_spaced_indices(gc_positions, total_change_needed)
        for pos in target_positions:
            if dna_list[pos] == 'G':
                dna_list[pos] = 'A'
            elif dna_list[pos] == 'C':
                dna_list[pos] = 'T'
            tag[pos] = '1'

    return ''.join(dna_list), ''.join(tag)

def recover_original_dna(modified_dna, tag):
    """
    Reverses the GC modification using the tag
    """
    recovered = []
    for base, t in zip(modified_dna, tag):
        if t == '1':
            if base == 'G':
                recovered.append('A')
            elif base == 'C':
                recovered.append('T')
            elif base == 'A':
                recovered.append('G')
            elif base == 'T':
                recovered.append('C')
        else:
            recovered.append(base)
    return ''.join(recovered)

# === Example Usage ===
if __name__ == "__main__":
    input_dna = "ATGTAGACATGCCAGTATGCATACAGATATACATGCCAGTCAGCCCGCCGCACCGCCAGTATGTAGACATGCCAGTATGCATACAGATATACATGCCAGTCAGCCCGCCGCACCGCCAGTCGACCCGCCAGTATGTATACATGCCAGTATGCATACAGATACATAGACATACATTAATGCCAGCCCGCCGCACCGCCATCAGATATACATGCCAGTCAGCCCGCCGATCCGCCAGCATGTATACAGACACATAGACAGACAGGCATGCATGCAGGCAGACACACAAACAAACACACAGACAGAGACAAACATAGACAGACAGGCATGCATGCAGGCAGACACACAAACAAACACACAGACACAGAAAAAAATACACACACAGACAAACACACAGAAAGGAAGACAAACACACAGATAGACAGACAGGCATGCATGCAGGCAGACACACAAACAAACACACAGACACAGAAAAAAATAAACAAACATGCATGCCAGCCAGCATGTAGGCAGGCAGACAGACACACACACAAATAAACAAAAACAGAAAGAGGGAGATAAACAAAAACAGAAAGATGGAGGTAGACAGACAGATAGACAGACAGATAGACATGCAAACACACAGCCAGGCAGGCAGGCAGGCAGGCAGACAGACAGAGAGAAAGACACACACACAGACACATATGT"
    target_gc = 0.63 

    print(f"Original DNA:  {input_dna}")
    print(f"Original GC%:  {gc_content(input_dna):.4f}")

    modified_dna, tag = increase_gc_uniformly(input_dna, target_gc)

    print(f"\nModified DNA:  {modified_dna}")
    print(f"Modified GC%:  {gc_content(modified_dna):.4f}")
    print(f"Binary Tag:    (39)")
    recovered = recover_original_dna(modified_dna, tag)
    print(f"\nRecovered DNA: {recovered}")
    print(f"Recovered OK:  {'✅' if recovered == input_dna else '❌'}")

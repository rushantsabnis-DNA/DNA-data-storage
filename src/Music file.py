CODE TO WRITE MUSIC IN DNA 
import random
from pydub import AudioSegment
from pydub.generators import Sine

# --- Note and duration mappings ---
note_freqs = {
      'C4': 206.92, 'C#4': 218.78, 'D4': 231.23, 'D#4': 245.36, 'E4': 260.95,
    'F4': 275.90, 'F#4': 291.90, 'G4': 309.68, 'G#4': 327.75, 'A4': 347.60,
    'A#4': 367.96, 'B4': 389.65, 'C5': 413.29, 'C#5': 437.23, 'D5': 462.31,
    'D#5': 489.57, 'E5': 518.77, 'F5': 549.08, 'F#5': 581.29, 'G5': 616.56,
    'G#5': 653.48, 'A5': 694.51, 'A#5': 735.78, 'B5': 778.94,
    
    # Optional rest note
    'REST': 0.0
}

note_dict = {note: format(i, '05b') for i, note in enumerate(note_freqs)}
note_dict_inv = {v: k for k, v in note_dict.items()}

durations = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0]
duration_dict = {d: format(i, '03b') for i, d in enumerate(durations)}
duration_dict_inv = {v: k for k, v in duration_dict.items()}

bin_to_dna = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
dna_to_bin = {v: k for k, v in bin_to_dna.items()}

# --- Sample melody ---
happy_birthday = [
    ('C4', 0.5), ('C4', 0.25), ('D4', 0.75), ('C4', 0.75),
    ('F4', 0.75), ('E4', 1.0),
    ('C4', 0.5), ('C4', 0.25), ('D4', 0.75), ('C4', 0.75),
    ('G4', 0.75), ('F4', 1.0)
]

ode_to_joy = [
        ('E4', 0.5), ('E4', 0.5), ('F4', 0.5), ('G4', 0.5),
    ('G4', 0.5), ('F4', 0.5), ('E4', 0.5), ('D4', 0.5),
    ('C4', 0.5), ('C4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('E4', 0.75), ('D4', 0.25), ('D4', 1.0),

    ('E4', 0.5), ('E4', 0.5), ('F4', 0.5), ('G4', 0.5),
    ('G4', 0.5), ('F4', 0.5), ('E4', 0.5), ('D4', 0.5),
    ('C4', 0.5), ('C4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('D4', 0.75), ('C4', 0.25), ('C4', 1.0),

    ('D4', 0.5), ('D4', 0.5), ('E4', 0.5), ('C4', 0.5),
    ('D4', 0.5), ('E4', 0.25), ('F4', 0.25), ('E4', 0.5),
    ('C4', 0.5), ('D4', 0.5), ('E4', 1.0),

    ('E4', 0.5), ('E4', 0.5), ('F4', 0.5), ('G4', 0.5),
    ('G4', 0.5), ('F4', 0.5), ('E4', 0.5), ('D4', 0.5),
    ('C4', 0.5), ('C4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('D4', 0.75), ('C4', 0.25), ('C4', 1.0)
]
twinkle = [
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('A4', 0.5), ('A4', 0.5), ('G4', 1.0),
    ('F4', 0.5), ('F4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('C4', 1.0)
]


jingle_bells = [
    ('E4', 0.5), ('E4', 0.5), ('E4', 1.0),
    ('E4', 0.5), ('E4', 0.5), ('E4', 1.0),
    ('E4', 0.5), ('G4', 0.5), ('C4', 0.5), ('D4', 0.5), ('E4', 2.0),
    
    ('F4', 0.5), ('F4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('F4', 0.5), ('E4', 0.5), ('E4', 0.5), ('E4', 0.75), ('E4', 0.25),
    
    ('E4', 0.5), ('D4', 0.5), ('D4', 0.5), ('E4', 0.5), ('D4', 1.0), ('G4', 1.0),
]
spirit_of_aggieland = [
    # Verse: "Some may boast of prowess bold..."
    ("G4", 1), ("E4", 0.5), ("G4", 0.5), ("A4", 1),
    ("G4", 0.5), ("F#4", 0.5), ("E4", 1),
    ("F#4", 0.5), ("G4", 0.5), ("A4", 1), ("A4", 0.5), ("B4", 0.5),
    ("C5", 1.5), ("B4", 0.5), ("A4", 1), 

    # "Of the school they think so grand..."
    ("G4", 1), ("E4", 0.5), ("G4", 0.5), ("A4", 1),
    ("G4", 0.5), ("F#4", 0.5), ("E4", 1),
    ("F#4", 0.5), ("G4", 0.5), ("A4", 1), ("A4", 0.5), ("B4", 0.5),
    ("C5", 1.5), ("B4", 0.5), ("A4", 1),

    # "But there’s a spirit can ne’er be told..."
    ("C5", 0.5), ("B4", 0.5), ("A4", 1), ("G4", 1),
    ("F#4", 0.5), ("G4", 0.5), ("A4", 1),
    ("G4", 0.5), ("F#4", 0.5), ("E4", 1), ("D4", 1),

    # "It’s the Spirit of Aggieland"
    ("E4", 0.5), ("F#4", 0.5), ("G4", 1.5), ("G4", 0.5),
    ("A4", 0.5), ("B4", 0.5), ("C5", 1.5), ("B4", 0.5),
    ("A4", 2),

    # Chorus: "We are the Aggies, the Aggies are we..."
    ("E4", 1), ("F#4", 0.5), ("G4", 0.5), ("A4", 1),
    ("A4", 0.5), ("B4", 0.5), ("C5", 1),
    ("B4", 0.5), ("A4", 0.5), ("G4", 1),
    ("F#4", 0.5), ("E4", 0.5), ("D4", 1),

    # "True to each other as Aggies can be..."
    ("E4", 1), ("F#4", 0.5), ("G4", 0.5), ("A4", 1),
    ("A4", 0.5), ("B4", 0.5), ("C5", 1),
    ("B4", 0.5), ("A4", 0.5), ("G4", 1),
    ("F#4", 0.5), ("E4", 0.5), ("D4", 1),

    # "We’ve got to fight, boys, we’ve got to fight!"
    ("F#4", 0.5), ("G4", 0.5), ("A4", 1), ("G4", 0.5), ("F#4", 0.5),
    ("E4", 1), ("F#4", 0.5), ("G4", 0.5), ("A4", 1),
    ("B4", 0.5), ("C5", 0.5), ("D5", 1),

    # "We’ve got to fight for Maroon and White..."
    ("C5", 0.5), ("B4", 0.5), ("A4", 1), ("G4", 0.5), ("F#4", 0.5),
    ("E4", 1), ("F#4", 0.5), ("G4", 0.5), ("A4", 1), ("G4", 1),

    # "After they’ve boosted all the rest..."
    ("G4", 1), ("E4", 0.5), ("G4", 0.5), ("A4", 1),
    ("G4", 0.5), ("F#4", 0.5), ("E4", 1),
    ("F#4", 0.5), ("G4", 0.5), ("A4", 1), ("A4", 0.5), ("B4", 0.5),

    # "Then they will come and join the best..."
    ("C5", 1.5), ("B4", 0.5), ("A4", 1),
    ("G4", 0.5), ("F#4", 0.5), ("G4", 1),
    ("A4", 0.5), ("B4", 0.5), ("C5", 1),

    # "For we are the Aggies, the Aggies are we..."
    ("E4", 1), ("F#4", 0.5), ("G4", 0.5), ("A4", 1),
    ("A4", 0.5), ("B4", 0.5), ("C5", 1),
    ("B4", 0.5), ("A4", 0.5), ("G4", 1),
    ("F#4", 0.5), ("E4", 0.5), ("D4", 2)
]

songs = spirit_of_aggieland + ode_to_joy + happy_birthday 
# --- Encoding ---
def encode_to_dna(melody):
    binary = ''.join(note_dict[n] + duration_dict[d] for n, d in melody)
    if len(binary) % 2 != 0:
        binary += '0'  # pad
    dna = ''.join(bin_to_dna[binary[i:i+2]] for i in range(0, len(binary), 2))
    return dna

# --- Mutate DNA ---
def mutate_dna(dna, error_rate):
    if error_rate == 0:
        return dna

    dna = list(dna)
    bases = ['A', 'T', 'C', 'G']
    num_mutations = round(len(dna) * error_rate/1000)

    for _ in range(num_mutations):
        mutation_type = random.choice(['substitution', 'insertion', 'deletion'])
        idx = random.randint(0, len(dna) - 1)

        if mutation_type == 'substitution':
            dna[idx] = random.choice([b for b in bases if b != dna[idx]])

        elif mutation_type == 'insertion':
            dna.insert(idx, random.choice(bases))

        elif mutation_type == 'deletion' and len(dna) > 1:
            dna.pop(idx)

    return ''.join(dna)

# --- Decoding ---
def decode_from_dna(dna):
    bits = ''.join(dna_to_bin.get(base, '00') for base in dna)
    melody = []
    for i in range(0, len(bits) - 7, 8):
        note_bin = bits[i:i+5]
        dur_bin = bits[i+5:i+8]
        note = note_dict_inv.get(note_bin, 'C4')
        dur = duration_dict_inv.get(dur_bin, 0.5)
        melody.append((note, dur))
    return melody

# --- GC Content ---
def gc_content(dna):
    return round(100 * (dna.count('G') + dna.count('C')) / len(dna), 2)

# --- Synthesize audio from melody ---
def melody_to_audio(melody):
    song = AudioSegment.silent(duration=0)
    for note, dur in melody:
        freq = note_freqs.get(note, 440.0)
        dur_ms = int(dur * 1000)

        # Fundamental + overtones for richer sound
        base = Sine(freq).to_audio_segment(duration=dur_ms).apply_gain(-6)
        overtone1 = Sine(freq * 2).to_audio_segment(duration=dur_ms).apply_gain(-10)
        overtone2 = Sine(freq * 3).to_audio_segment(duration=dur_ms).apply_gain(-15)
        overtone3 = Sine(freq * 4).to_audio_segment(duration=dur_ms).apply_gain(-20)

        tone = base.overlay(overtone1).overlay(overtone2).overlay(overtone3)
        fade_out_ms = min(int(dur_ms * 0.25), 50)
        tone = tone.fade_in(5).fade_out(fade_out_ms)[:dur_ms]

        silence_gap = AudioSegment.silent(duration=20)
        song += tone + silence_gap
    return song
def write_notation_with_errors(original_melody, corrupted_melody, filename="notation_with_errors.txt"):
    with open(filename, "w") as f:
        f.write("Index\tOriginal Note\tOriginal Dur\tDecoded Note\tDecoded Dur\tError?\n")
        length = max(len(original_melody), len(corrupted_melody))
        for i in range(length):
            orig_note, orig_dur = original_melody[i] if i < len(original_melody) else ('', '')
            corr_note, corr_dur = corrupted_melody[i] if i < len(corrupted_melody) else ('', '')
            error_flag = "NO"
            if (orig_note != corr_note) or (orig_dur != corr_dur):
                error_flag = "<< ERROR >>"
            f.write(f"{i+1}\t{orig_note}\t{orig_dur}\t{corr_note}\t{corr_dur}\t{error_flag}\n")

# --- Example usage ---
if __name__ == "__main__":
    original_dna = encode_to_dna(songs)
    corrupted_dna = mutate_dna(original_dna, error_rate=1)

    original_melody = decode_from_dna(original_dna)
    corrupted_melody = decode_from_dna(corrupted_dna)
    write_notation_with_errors(original_melody, corrupted_melody)
    print("Original DNA:", original_dna)
    print("Corrupted DNA:", corrupted_dna)
    print("GC Content:", gc_content(original_dna), "%")

    melody_to_audio(original_melody).export("original.wav", format="wav")
    melody_to_audio(corrupted_melody).export("corrupted.wav", format="wav")
    with open("compiled_original_dna.txt", "w") as f:
        f.write(original_dna)

    with open("compiled_corrupted_dna.txt", "w") as f:
        f.write(corrupted_dna)

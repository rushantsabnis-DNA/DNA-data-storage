IMAGE CODE
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio, structural_similarity, mean_squared_error

# === Step 1: Load, Resize, and Crop Image ===
image = Image.open("Eye.jpg").convert("RGB")
RESIZE_WIDTH, RESIZE_HEIGHT = 120, 160
image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
left, top = 16, 16
crop_width, crop_height = 88, 96
cropped_image = image.crop((left, top, left + crop_width, top + crop_height))
rgb_array = np.array(cropped_image)

# === Step 2: Delta Encode, Binary and DNA Convert ===
def delta_encode(channel):
    flat = channel.flatten()
    deltas = [flat[0]] + [int(flat[i]) - int(flat[i - 1]) for i in range(1, len(flat))]
    deltas = [(x + 256) % 256 for x in deltas]
    return deltas

def to_binary(data):
    return ''.join(f"{val:08b}" for val in data)

def binary_to_dna(binary_str):
    bin_to_base = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    if len(binary_str) % 2: binary_str += '0'
    return ''.join(bin_to_base[binary_str[i:i+2]] for i in range(0, len(binary_str), 2))

def encode_channel(channel):
    delta = delta_encode(channel)
    binary = to_binary(delta)
    return binary_to_dna(binary)

# Encode RGB channels
dna_r = encode_channel(rgb_array[:, :, 0])
dna_g = encode_channel(rgb_array[:, :, 1])
dna_b = encode_channel(rgb_array[:, :, 2])

# Concatenate all DNA sequences
full_dna_sequence = dna_r + dna_g + dna_b
print(f"🧬 Full DNA sequence (concatenated RGB): {full_dna_sequence}")
print(f"🧬 DNA lengths - R: {len(dna_r)}, G: {len(dna_g)}, B: {len(dna_b)}")

# === Step 3: Decode DNA Back ===
def dna_to_binary(dna_seq):
    base_to_bin = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    return ''.join(base_to_bin[base] for base in dna_seq)

def binary_to_delta(binary_str):
    return [int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)]

def delta_decode(deltas):
    decoded = [deltas[0]]
    for i in range(1, len(deltas)):
        decoded.append((decoded[i-1] + deltas[i]) % 256)
    return decoded

def decode_channel(dna_seq):
    binary = dna_to_binary(dna_seq)
    delta = binary_to_delta(binary)
    decoded = delta_decode(delta)
    return np.array(decoded, dtype=np.uint8).reshape((crop_height, crop_width))

# Decode all channels
r_rec = decode_channel(dna_r)
g_rec = decode_channel(dna_g)
b_rec = decode_channel(dna_b)
reconstructed_rgb = np.stack([r_rec, g_rec, b_rec], axis=-1)

# === Step 4: Introduce DNA Errors ===
def introduce_dna_error(dna_seq, errors_per_1000bp=1):
    dna = list(dna_seq)
    bases = ['A', 'C', 'G', 'T']
    total_errors = int((len(dna) / 1000) * errors_per_1000bp)
    error_indices = np.random.choice(len(dna), total_errors, replace=False)
    for idx in error_indices:
        original = dna[idx]
        dna[idx] = np.random.choice([b for b in bases if b != original])
    return ''.join(dna)

# Corrupt DNA sequences
r_err = introduce_dna_error(dna_r, 0.03)
g_err = introduce_dna_error(dna_g, 0.03)
b_err = introduce_dna_error(dna_b, 0.03)

r_dec_err = decode_channel(r_err)
g_dec_err = decode_channel(g_err)
b_dec_err = decode_channel(b_err)
reconstructed_rgb_err = np.stack([r_dec_err, g_dec_err, b_dec_err], axis=-1)

# === Step 5: Error Metrics ===
mse = mean_squared_error(reconstructed_rgb, reconstructed_rgb_err)
psnr = peak_signal_noise_ratio(reconstructed_rgb, reconstructed_rgb_err)
ssim = structural_similarity(reconstructed_rgb, reconstructed_rgb_err, win_size=7, channel_axis=-1)

print(f"🧪 Error Metrics:")
print(f"- MSE: {mse:.2f}")
print(f"- PSNR: {psnr:.2f} dB")
print(f"- SSIM: {ssim:.4f}")

# === Step 6: Visual Output ===
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(reconstructed_rgb)
plt.title("Original from DNA")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_rgb_err)
plt.title("Corrupted DNA")
plt.axis('off')
plt.show()

# === GC Content ===
def calculate_gc_content(dna_seq):
    g = dna_seq.count('G')
    c = dna_seq.count('C')
    return 100 * (g + c) / len(dna_seq)

print(f"🧬 GC Contents: R={calculate_gc_content(dna_r):.2f}%, G={calculate_gc_content(dna_g):.2f}%, B={calculate_gc_content(dna_b):.2f}%")


    recovered = recover_original_dna(modified_dna, tag)
    print(f"\nRecovered DNA: {recovered}")
    print(f"Recovered OK:  {'✅' if recovered == input_dna else '❌'}")


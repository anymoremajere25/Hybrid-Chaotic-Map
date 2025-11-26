from skimage.metrics import mean_squared_error, peak_signal_noise_ratio
from PIL import Image
import numpy as np

# ✅ Image filenames
rgb_filenames = ["Baboon.jpg"]#, "Cameraman.png", "Lena.jpeg", "Pepper.tiff"]

# ✅ Table header
print(" MSE and PSNR Results")
print(f"{'Image':<15} {'MSE':>10} {'PSNR (dB)':>12}")
print("-" * 40)

# 🔁 Compute metrics
offset = 0
for fname in rgb_filenames:
    # Load image
    orig_img = Image.open(fname).convert("RGB")
    orig_arr = np.array(orig_img).astype(np.float64)

    # Encrypt and decrypt (since keystream XOR is reversible)
    flat = orig_arr.flatten()
    ks_segment = keystream[offset:offset + flat.size]
    encrypted_flat = np.bitwise_xor(flat.astype(np.uint8), ks_segment)
    decrypted_flat = np.bitwise_xor(encrypted_flat, ks_segment)
    decrypted_arr = decrypted_flat.reshape(orig_arr.shape).astype(np.float64)

    offset += flat.size

    # Compute MSE and PSNR on decrypted image
    mse = mean_squared_error(orig_arr, decrypted_arr)
    psnr = peak_signal_noise_ratio(orig_arr, decrypted_arr, data_range=255)

    # Handle infinite PSNR nicely
    psnr_display = "∞" if np.isinf(psnr) else f"{psnr:.4f}"

    # Print row
    print(f"{fname:<15} {mse:10.4f} {psnr_display:>12}")


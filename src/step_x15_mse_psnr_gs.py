from skimage.metrics import mean_squared_error, peak_signal_noise_ratio
from PIL import Image
import numpy as np

# ✅ Grayscale image filenames
gray_filenames = ["Cameraman.png"]   # add more if needed

# ✅ Table header
print(" MSE and PSNR Results (Grayscale Images)")
print(f"{'Image':<15} {'MSE':>12} {'PSNR (dB)':>14}")
print("-" * 45)

# 🔁 Compute metrics
offset = 0
for fname in gray_filenames:
    # Load original grayscale image
    orig_img = Image.open(fname).convert("L")
    orig_arr = np.array(orig_img).astype(np.float64)

    # Encrypt + decrypt (XOR reversible)
    flat = orig_arr.flatten()
    ks_segment = keystream[offset:offset + flat.size]

    if ks_segment.size < flat.size:
        raise ValueError(f"Keystream too short at offset {offset} for image {fname}")

    encrypted_flat  = np.bitwise_xor(flat.astype(np.uint8), ks_segment)
    decrypted_flat  = np.bitwise_xor(encrypted_flat, ks_segment)

    decrypted_arr = decrypted_flat.reshape(orig_arr.shape).astype(np.float64)

    offset += flat.size

    # Calculate MSE + PSNR
    mse  = mean_squared_error(orig_arr, decrypted_arr)
    psnr = peak_signal_noise_ratio(orig_arr, decrypted_arr, data_range=255)

    # Format PSNR for display
    psnr_display = "∞" if np.isinf(psnr) else f"{psnr:.4f}"

    # Print result row
    print(f"{fname:<15} {mse:12.6f} {psnr_display:>14}")


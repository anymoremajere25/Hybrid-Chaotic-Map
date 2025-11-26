import numpy as np
from PIL import Image
from scipy.stats import pearsonr

# 🔐 Encrypt grayscale image with XOR keystream
def encrypt_grayscale_image(img: Image.Image, keystream: np.ndarray, offset: int):
    arr = np.array(img)
    flat = arr.flatten()
    ks_segment = keystream[offset:offset + flat.size]
    encrypted = np.bitwise_xor(flat, ks_segment)
    encrypted_arr = encrypted.reshape(arr.shape).astype(np.uint8)
    encrypted_img = Image.fromarray(encrypted_arr, mode='L')
    return encrypted_img

# 📊 Extract pixel pairs in specific direction
def get_pixel_pairs_gray(arr: np.ndarray, mode: str):
    if mode == 'horizontal':
        x = arr[:, :-1]
        y = arr[:, 1:]
    elif mode == 'vertical':
        x = arr[:-1, :]
        y = arr[1:, :]
    elif mode == 'diagonal':
        x = arr[:-1, :-1]
        y = arr[1:, 1:]
    else:
        raise ValueError("Mode must be 'horizontal', 'vertical', or 'diagonal'")

    return x.flatten(), y.flatten()

# 📂 Grayscale image filenames
gray_filenames = ["Cameraman.png"]
directions = ['horizontal', 'vertical', 'diagonal']

offset = 0
print("📌 Pearson Correlation Coefficients and p-values – Grayscale Images\n")

for fname in gray_filenames:
    print(f"📁 {fname}")
    orig_img = Image.open(fname).convert("L")
    enc_img = encrypt_grayscale_image(orig_img, keystream, offset)
    offset += np.array(orig_img).size

    orig_arr = np.array(orig_img)
    enc_arr  = np.array(enc_img)

    for direction in directions:
        x_o, y_o = get_pixel_pairs_gray(orig_arr, direction)
        x_e, y_e = get_pixel_pairs_gray(enc_arr, direction)

        r_orig, p_orig = pearsonr(x_o, y_o)
        r_enc,  p_enc  = pearsonr(x_e, y_e)

        print(f"  ➤ {direction.capitalize()}:")
        print(f"      Original : r = {r_orig:.4f}, p = {p_orig:.2e}")
        print(f"      Encrypted: r = {r_enc:.4f}, p = {p_enc:.2e}")
    print("─" * 60)


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 📥 Load keystream from file (change filename if needed)
keystream_filename = "keystream_composite_dyadic_tent_4MB_whitened.bin"
with open(keystream_filename, "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

print(f"Loaded keystream: {keystream_filename}")
print(f"Keystream size = {len(keystream):,} bytes")

# 🔐 Encrypt RGB image using XOR keystream
def encrypt_rgb_image(img: Image.Image, keystream: np.ndarray, offset: int):
    arr = np.array(img)
    flat = arr.flatten()
    ks_segment = keystream[offset:offset + flat.size]
    if ks_segment.size < flat.size:
        raise ValueError("Keystream too short for this image + offset!")
    encrypted = np.bitwise_xor(flat, ks_segment)
    encrypted_arr = encrypted.reshape(arr.shape).astype(np.uint8)
    encrypted_img = Image.fromarray(encrypted_arr, mode='RGB')
    return encrypted_img

# 📊 Extract horizontal pixel pairs per RGB channel
def get_horizontal_pixel_pairs_rgb(arr: np.ndarray):
    pairs = {}
    for i, color in enumerate(['R', 'G', 'B']):
        channel = arr[:, :, i]
        x = channel[:, :-1].flatten()
        y = channel[:, 1:].flatten()
        pairs[color] = (x, y)
    return pairs

# 📊 Extract vertical pixel pairs per RGB channel
def get_vertical_pixel_pairs_rgb(arr: np.ndarray):
    pairs = {}
    for i, color in enumerate(['R', 'G', 'B']):
        channel = arr[:, :, i]
        x = channel[:-1, :].flatten()
        y = channel[1:, :].flatten()
        pairs[color] = (x, y)
    return pairs

# 📊 Extract diagonal pixel pairs per RGB channel (top-left → bottom-right)
def get_diagonal_pixel_pairs_rgb(arr: np.ndarray):
    pairs = {}
    for i, color in enumerate(['R', 'G', 'B']):
        channel = arr[:, :, i]
        x = channel[:-1, :-1].flatten()
        y = channel[1:, 1:].flatten()
        pairs[color] = (x, y)
    return pairs

# 📂 RGB test images
rgb_filenames = ["Baboon.jpg", "Lena.jpeg", "Pepper.tiff"]

offset = 0
for fname in rgb_filenames:
    print(f"\n📊 Pixel Correlation Scatterplots – {fname}")

    # Load original image and encrypt once
    orig_img = Image.open(fname).convert("RGB")
    orig_arr = np.array(orig_img)

    enc_img = encrypt_rgb_image(orig_img, keystream, offset)
    enc_arr = np.array(enc_img)
    offset += orig_arr.size  # advance keystream offset

    # =========================================================
    # 1) HORIZONTAL CORRELATION
    # =========================================================
    orig_pairs_h = get_horizontal_pixel_pairs_rgb(orig_arr)
    enc_pairs_h  = get_horizontal_pixel_pairs_rgb(enc_arr)

    fig, axs = plt.subplots(3, 2, figsize=(12, 9))
    fig.suptitle(f"Horizontal Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    for row, color in enumerate(['R', 'G', 'B']):
        x_o, y_o = orig_pairs_h[color]
        x_e, y_e = enc_pairs_h[color]

        # Original
        axs[row, 0].scatter(x_o, y_o, s=1, alpha=0.5, color=color.lower())
        axs[row, 0].set_title(f"Original – Channel {color}")
        axs[row, 0].set_xlabel("Pixel(i)")
        axs[row, 0].set_ylabel("Pixel(i+1)")
        axs[row, 0].grid(True)

        # Encrypted
        axs[row, 1].scatter(x_e, y_e, s=1, alpha=0.5, color=color.lower())
        axs[row, 1].set_title(f"Encrypted – Channel {color}")
        axs[row, 1].set_xlabel("Pixel(i)")
        axs[row, 1].set_ylabel("Pixel(i+1)")
        axs[row, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # =========================================================
    # 2) VERTICAL CORRELATION
    # =========================================================
    orig_pairs_v = get_vertical_pixel_pairs_rgb(orig_arr)
    enc_pairs_v  = get_vertical_pixel_pairs_rgb(enc_arr)

    fig, axs = plt.subplots(3, 2, figsize=(12, 9))
    fig.suptitle(f"Vertical Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    for row, color in enumerate(['R', 'G', 'B']):
        x_o, y_o = orig_pairs_v[color]
        x_e, y_e = enc_pairs_v[color]

        axs[row, 0].scatter(x_o, y_o, s=1, alpha=0.5, color=color.lower())
        axs[row, 0].set_title(f"Original – Channel {color}")
        axs[row, 0].set_xlabel("Pixel(i)")
        axs[row, 0].set_ylabel("Pixel(i+1)")
        axs[row, 0].grid(True)

        axs[row, 1].scatter(x_e, y_e, s=1, alpha=0.5, color=color.lower())
        axs[row, 1].set_title(f"Encrypted – Channel {color}")
        axs[row, 1].set_xlabel("Pixel(i)")
        axs[row, 1].set_ylabel("Pixel(i+1)")
        axs[row, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # =========================================================
    # 3) DIAGONAL CORRELATION
    # =========================================================
    orig_pairs_d = get_diagonal_pixel_pairs_rgb(orig_arr)
    enc_pairs_d  = get_diagonal_pixel_pairs_rgb(enc_arr)

    fig, axs = plt.subplots(3, 2, figsize=(12, 9))
    fig.suptitle(f"Diagonal Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    for row, color in enumerate(['R', 'G', 'B']):
        x_o, y_o = orig_pairs_d[color]
        x_e, y_e = enc_pairs_d[color]

        axs[row, 0].scatter(x_o, y_o, s=1, alpha=0.5, color=color.lower())
        axs[row, 0].set_title(f"Original – Channel {color}")
        axs[row, 0].set_xlabel("Pixel(i,j)")
        axs[row, 0].set_ylabel("Pixel(i+1,j+1)")
        axs[row, 0].grid(True)

        axs[row, 1].scatter(x_e, y_e, s=1, alpha=0.5, color=color.lower())
        axs[row, 1].set_title(f"Encrypted – Channel {color}")
        axs[row, 1].set_xlabel("Pixel(i,j)")
        axs[row, 1].set_ylabel("Pixel(i+1,j+1)")
        axs[row, 1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


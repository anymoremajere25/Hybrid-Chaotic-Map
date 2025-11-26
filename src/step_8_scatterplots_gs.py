import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 📥 Load keystream from file (set your filename here)
keystream_filename = "keystream_composite_dyadic_tent_4MB_whitened.bin"
with open(keystream_filename, "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

print(f"Loaded keystream: {keystream_filename}")
print(f"Keystream size = {len(keystream):,} bytes")

# 🔐 Encrypt grayscale image using XOR keystream
def encrypt_grayscale_image(img: Image.Image, keystream: np.ndarray, offset: int):
    arr = np.array(img)
    flat = arr.flatten()
    ks_segment = keystream[offset:offset + flat.size]
    if ks_segment.size < flat.size:
        raise ValueError("Keystream too short for this image + offset!")
    encrypted = np.bitwise_xor(flat, ks_segment)
    encrypted_arr = encrypted.reshape(arr.shape).astype(np.uint8)
    encrypted_img = Image.fromarray(encrypted_arr, mode='L')
    return encrypted_img

# 📊 Extract vertical pixel pairs for grayscale image
def get_vertical_pixel_pairs_gray(arr: np.ndarray):
    x = arr[:-1, :].flatten()
    y = arr[1:, :].flatten()
    return x, y

# 📊 Extract diagonal pixel pairs (top-left → bottom-right)
def get_diagonal_pixel_pairs_gray(arr: np.ndarray):
    x = arr[:-1, :-1].flatten()
    y = arr[1:, 1:].flatten()
    return x, y

# 📊 Extract horizontal pixel pairs for grayscale image
def get_horizontal_pixel_pairs_gray(arr: np.ndarray):
    x = arr[:, :-1].flatten()
    y = arr[:, 1:].flatten()
    return x, y

# 📂 Grayscale image filenames
gray_filenames = ["Cameraman.png"]   # change or add more if needed

offset = 0
for fname in gray_filenames:
    print(f"\n📊 Pixel Correlation Scatterplots – {fname}")

    # Load original image (grayscale)
    orig_img = Image.open(fname).convert("L")
    orig_arr = np.array(orig_img)

    # Encrypt once for this image
    enc_img = encrypt_grayscale_image(orig_img, keystream, offset)
    enc_arr = np.array(enc_img)
    offset += orig_arr.size

    # ========= VERTICAL =========
    x_o_v, y_o_v = get_vertical_pixel_pairs_gray(orig_arr)
    x_e_v, y_e_v = get_vertical_pixel_pairs_gray(enc_arr)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Vertical Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    axs[0].scatter(x_o_v, y_o_v, s=1, alpha=0.5, color='gray')
    axs[0].set_title("Original Grayscale")
    axs[0].set_xlabel("Pixel(i)")
    axs[0].set_ylabel("Pixel(i+1)")
    axs[0].grid(True)

    axs[1].scatter(x_e_v, y_e_v, s=1, alpha=0.5, color='gray')
    axs[1].set_title("Encrypted Grayscale")
    axs[1].set_xlabel("Pixel(i)")
    axs[1].set_ylabel("Pixel(i+1)")
    axs[1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # ========= DIAGONAL =========
    x_o_d, y_o_d = get_diagonal_pixel_pairs_gray(orig_arr)
    x_e_d, y_e_d = get_diagonal_pixel_pairs_gray(enc_arr)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Diagonal Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    axs[0].scatter(x_o_d, y_o_d, s=1, alpha=0.5, color='gray')
    axs[0].set_title("Original Grayscale")
    axs[0].set_xlabel("Pixel(i,j)")
    axs[0].set_ylabel("Pixel(i+1,j+1)")
    axs[0].grid(True)

    axs[1].scatter(x_e_d, y_e_d, s=1, alpha=0.5, color='gray')
    axs[1].set_title("Encrypted Grayscale")
    axs[1].set_xlabel("Pixel(i,j)")
    axs[1].set_ylabel("Pixel(i+1,j+1)")
    axs[1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # ========= HORIZONTAL =========
    x_o_h, y_o_h = get_horizontal_pixel_pairs_gray(orig_arr)
    x_e_h, y_e_h = get_horizontal_pixel_pairs_gray(enc_arr)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Horizontal Pixel Pairs – Original vs Encrypted\n{fname}", fontsize=14)

    axs[0].scatter(x_o_h, y_o_h, s=1, alpha=0.5, color='gray')
    axs[0].set_title("Original Grayscale")
    axs[0].set_xlabel("Pixel(i)")
    axs[0].set_ylabel("Pixel(i+1)")
    axs[0].grid(True)

    axs[1].scatter(x_e_h, y_e_h, s=1, alpha=0.5, color='gray')
    axs[1].set_title("Encrypted Grayscale")
    axs[1].set_xlabel("Pixel(i)")
    axs[1].set_ylabel("Pixel(i+1)")
    axs[1].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


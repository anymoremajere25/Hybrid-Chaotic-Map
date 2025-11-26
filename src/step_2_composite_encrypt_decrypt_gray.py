# 📦 Step 1: Import required libraries
from google.colab import files
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io

# 📤 Step 2: Upload grayscale image(s)
print("Upload grayscale image(s) (e.g., cameraman.png)...")
uploaded = files.upload()

# 📥 Step 3: Load images and convert to grayscale ("L" mode)
images = {}
for fname in uploaded.keys():
    img = Image.open(io.BytesIO(uploaded[fname])).convert("L")  # "L" = grayscale
    images[fname] = img

# 🔐 Step 4: Upload and load composite SHA-whitened keystream
print("Upload keystream file (e.g., keystream_composite_hybrid_4MB_whitened.bin)...")
ks_file = files.upload()

ks_fname = list(ks_file.keys())[0]
with open(ks_fname, "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

print(f"Loaded keystream from {ks_fname} with length {len(keystream)} bytes.")

# 🔁 Step 5: Encrypt & Decrypt function for grayscale images
def encrypt_decrypt_image_gray(img: Image.Image, keystream: np.ndarray, offset: int):
    img_array = np.array(img)
    flat = img_array.flatten()

    # take a segment of keystream of same length
    ks_segment = keystream[offset:offset + flat.size]
    if ks_segment.size < flat.size:
        raise ValueError("Keystream too short for this image + offset!")

    encrypted_flat = np.bitwise_xor(flat, ks_segment)
    decrypted_flat = np.bitwise_xor(encrypted_flat, ks_segment)

    encrypted_img = Image.fromarray(
        encrypted_flat.reshape(img_array.shape).astype(np.uint8),
        mode='L'
    )
    decrypted_img = Image.fromarray(
        decrypted_flat.reshape(img_array.shape).astype(np.uint8),
        mode='L'
    )

    return encrypted_img, decrypted_img

# 📊 Step 6: Process and display results
offset = 0
for fname, img in images.items():
    enc_img, dec_img = encrypt_decrypt_image_gray(img, keystream, offset)
    offset += np.array(img).size  # move offset for next image

    # Plot original, encrypted, and decrypted grayscale images
    fig, axs = plt.subplots(1, 3, figsize=(14, 4))
    titles = [
        f"Original ({fname})",
        f"Encrypted ({fname})",
        f"Decrypted ({fname})"
    ]
    for ax, im, title in zip(axs, [img, enc_img, dec_img], titles):
        ax.imshow(im, cmap='gray')
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
    plt.show()



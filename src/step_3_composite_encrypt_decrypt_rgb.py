# 📦 Step 1: Import required libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import io

# 📤 Step 2: Upload RGB images
print("Upload RGB image(s)...")
uploaded = files.upload()

# 📥 Step 3: Load images exactly as they are (no .convert())
images = {}
for fname in uploaded.keys():
    img = Image.open(io.BytesIO(uploaded[fname]))
    images[fname] = img

# 🔐 Step 4: Upload & load composite whitened keystream
print("Upload keystream file (e.g., keystream_composite_hybrid_4MB_whitened.bin)...")
ks_file = files.upload()

ks_name = list(ks_file.keys())[0]
with open(ks_name, "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

print(f"Loaded keystream: {ks_name}")
print(f"Keystream size = {len(keystream):,} bytes")

# 🔁 Step 5: Encryption & Decryption using XOR
def encrypt_decrypt_image(img: Image.Image, keystream: np.ndarray, offset: int):
    img_array = np.array(img)  # RGB image array
    flat = img_array.flatten()

    # Extract keystream segment
    ks_segment = keystream[offset:offset + flat.size]
    if ks_segment.size < flat.size:
        raise ValueError("❌ Keystream too short for this image + offset.")

    encrypted_flat = np.bitwise_xor(flat, ks_segment)
    decrypted_flat = np.bitwise_xor(encrypted_flat, ks_segment)

    encrypted_img = Image.fromarray(
        encrypted_flat.reshape(img_array.shape).astype(np.uint8)
    )
    decrypted_img = Image.fromarray(
        decrypted_flat.reshape(img_array.shape).astype(np.uint8)
    )

    return encrypted_img, decrypted_img

# 📊 Step 6: Process each image (supports multiple images)
offset = 0
for fname, img in images.items():
    enc_img, dec_img = encrypt_decrypt_image(img, keystream, offset)

    # Update offset for next image
    offset += np.array(img).size

    # Show original, encrypted, and decrypted
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    titles = ["Original Image", "Encrypted Image", "Decrypted Image"]

    for ax, im, title in zip(axs, [img, enc_img, dec_img], titles):
        ax.imshow(im)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import io

# 📥 Step 1: Load the composite whitened keystream
keystream_filename = "keystream_composite_dyadic_tent_4MB_whitened.bin"
with open(keystream_filename, "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

print(f"Loaded keystream: {keystream_filename}")
print(f"Keystream size = {len(keystream):,} bytes")

# 📤 Step 2: Upload RGB images
print("📤 Upload one or more RGB images")
uploaded = files.upload()

# 📦 Step 3: Encrypt and Plot Histograms side-by-side
offset = 0
for fname in uploaded:
    # Load image (already RGB; no need to convert if you're sure, but safe to enforce RGB)
    img = Image.open(io.BytesIO(uploaded[fname])).convert("RGB")
    img_np = np.array(img)
    flat = img_np.flatten()

    # 🔐 Encrypt using XOR with keystream segment
    ks_segment = keystream[offset:offset + flat.size]
    if ks_segment.size < flat.size:
        raise ValueError(f"❌ Keystream too short for image {fname} at offset {offset}")

    encrypted_flat = np.bitwise_xor(flat, ks_segment)
    encrypted_np = encrypted_flat.reshape(img_np.shape).astype(np.uint8)
    offset += flat.size

    # Split channels: R, G, B
    channels_orig = [img_np[..., i].flatten() for i in range(3)]
    channels_enc = [encrypted_np[..., i].flatten() for i in range(3)]
    colors = ['red', 'green', 'blue']

    # 🖼️ Plot side-by-side comparison for R, G, B
    fig, axs = plt.subplots(3, 2, figsize=(12, 8))
    for i, color in enumerate(colors):
        # Original channel histogram
        axs[i, 0].hist(channels_orig[i], bins=256, color=color, alpha=0.7)
        axs[i, 0].set_title(f"Original {color.upper()} Histogram")

        # Encrypted channel histogram
        axs[i, 1].hist(channels_enc[i], bins=256, color=color, alpha=0.7)
        axs[i, 1].set_title(f"Encrypted {color.upper()} Histogram")

        for ax in axs[i]:
            ax.set_xlim([0, 256])

    fig.suptitle(f"RGB Histogram Comparison: {fname}", fontsize=14)
    plt.tight_layout()
    plt.show()


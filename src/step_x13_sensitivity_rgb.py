from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from sklearn.metrics import mean_squared_error
import io

# Step 1: Upload RGB images
uploaded = files.upload()
images = {}
for fname in uploaded.keys():
    img = Image.open(io.BytesIO(uploaded[fname])).convert("RGB")
    images[fname] = img

# Step 2: Load keystream
with open("keystream_composite_dyadic_tent_4MB_whitened.bin", "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

# Step 3: Define offsets simulating key drift
offset_scenarios = {
    "x₀ = 0.7": 0,
    "x₀ + 1e−6": 1,
    "x₀ + 1e−15": 10,
    "x₀ + 1e−17": 0
}

# Step 4: Encrypt and decrypt with perturbed keystreams
for fname, img in images.items():
    print(f"\n🔐 Sensitivity Analysis for: Lena")
    img_arr = np.array(img)
    flat = img_arr.flatten()

    # Encrypt with base keystream
    ks_enc = keystream[:len(flat)]
    encrypted = np.bitwise_xor(flat, ks_enc)

    # Prepare figure
    fig, axs = plt.subplots(1, len(offset_scenarios), figsize=(16, 5))

    for ax, (label, offset) in zip(axs, offset_scenarios.items()):
        ks_dec = keystream[offset:offset + len(flat)]
        decrypted = np.bitwise_xor(encrypted, ks_dec)
        dec_img = decrypted.reshape(img_arr.shape).astype(np.uint8)

        # MSE
        mse = mean_squared_error(flat, decrypted)
        ax.imshow(dec_img)
        ax.set_title(f"{label}\nMSE={mse:.2f}")
        ax.axis("off")

    plt.suptitle(f"Sensitivity Analysis", fontsize=14)
    plt.tight_layout()
    plt.show()


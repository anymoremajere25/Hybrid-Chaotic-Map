from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from sklearn.metrics import mean_squared_error
import io

# Step 1: Upload grayscale image (e.g., cake.png)
uploaded = files.upload()
img_gray = Image.open(io.BytesIO(next(iter(uploaded.values())))).convert("L")
img_array = np.array(img_gray)
flat = img_array.flatten()

# Step 2: Load the base keystream
with open("keystream_composite_dyadic_tent_4MB_whitened.bin", "rb") as f:
    keystream = np.frombuffer(f.read(), dtype=np.uint8)

# Step 3: Encrypt using correct keystream
ks_correct = keystream[:len(flat)]
encrypted = np.bitwise_xor(flat, ks_correct)

# Step 4: Define decryption scenarios
offsets = {
    "x₀ = 0.7": 0,
    "x₀ + 1e−6": 1,
    "x₀ + 1e−15": 10,
    "x₀ + 1e−17": 0  # Use same keystream as encryption
}

results = {}

for label, offset in offsets.items():
    ks_decrypt = keystream[offset:offset + len(flat)]
    decrypted = np.bitwise_xor(encrypted, ks_decrypt)
    dec_img = decrypted.reshape(img_array.shape).astype(np.uint8)

    mse = mean_squared_error(flat, decrypted)
    results[label] = (dec_img, mse)

# Step 5: Plot the results
fig, axs = plt.subplots(1, len(results), figsize=(16, 5))
for ax, (label, (img, mse)) in zip(axs, results.items()):
    ax.imshow(img, cmap="gray")
    ax.set_title(f"{label}\nMSE={mse:.2f}")
    ax.axis("off")

plt.suptitle("Sensitivity Analysis – Decrypted Results with Perturbed Keystreams", fontsize=14)
plt.tight_layout()
plt.show()


from PIL import Image
import numpy as np
from scipy.stats import chisquare

# 📊 Chi-Square Test Function for Grayscale
def chisquare_test_grayscale(img: Image.Image):
    arr = np.array(img).flatten()
    obs, _ = np.histogram(arr, bins=256, range=(0, 255))
    expected = np.ones_like(obs) * (obs.sum() / 256)
    chi2_stat, p_val = chisquare(obs, f_exp=expected)
    return chi2_stat, p_val

# 🧪 Apply test to encrypted grayscale images
offset = 0
print("📊 Chi-Square Test Results – Grayscale Encrypted Images:\n")

for fname, img in images.items():
    enc_img, _ = encrypt_decrypt_image_gray(img, keystream, offset)
    offset += np.array(img).size

    chi2, p = chisquare_test_grayscale(enc_img)
    print(f"{fname}: Chi² = {chi2:.2f}, p = {p:.6f} "
          + ("✅ Uniform" if p > 0.05 else "❗ Not Uniform"))


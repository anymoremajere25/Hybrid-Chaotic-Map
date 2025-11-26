# 📊 Chi-Square Test Function for RGB
def chisquare_test_rgb(img: Image.Image):
    arr = np.array(img)
    results = {}
    for i, color in enumerate(['R', 'G', 'B']):
        channel = arr[:, :, i].flatten()
        obs, _ = np.histogram(channel, bins=256, range=(0, 255))
        expected = np.ones_like(obs) * (obs.sum() / 256)
        chi2_stat, p_val = chisquare(obs, f_exp=expected)
        results[color] = (chi2_stat, p_val)
    return results

# 🧪 Apply test to encrypted RGB images
offset = 0
print("\n📊 Chi-Square Test Results – RGB Encrypted Images:\n")

for fname, img in images.items():
    enc_img, _ = encrypt_decrypt_image(img, keystream, offset)
    offset += np.array(img).size

    print(f"🔐 {fname}")
    results = chisquare_test_rgb(enc_img)
    for ch, (chi2, p) in results.items():
        print(f"  Channel {ch}: Chi² = {chi2:.2f}, p = {p:.6f} "
              + ("✅ Uniform" if p > 0.05 else "❗ Not Uniform"))
    print()


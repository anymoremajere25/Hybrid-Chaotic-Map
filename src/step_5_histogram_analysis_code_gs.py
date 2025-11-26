# 📈 Step 7: Plot grayscale histogram
def plot_grayscale_histogram(image: Image.Image, title: str):
    arr = np.array(image).flatten()
    
    plt.figure(figsize=(6, 3))
    plt.hist(arr, bins=256, range=(0, 255), color='gray', alpha=0.75)
    plt.title(title)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

# 🔍 Step 8: Generate histograms for Original, Encrypted, and Decrypted
offset = 0
for fname, img in images.items():
    # Encrypt & decrypt using the same grayscale encryption function
    enc_img, dec_img = encrypt_decrypt_image_gray(img, keystream, offset)
    offset += np.array(img).size

    # Plot histograms
    plot_grayscale_histogram(img, f"Histogram – Original [{fname}]")
    plot_grayscale_histogram(enc_img, f"Histogram – Encrypted [{fname}]")
    plot_grayscale_histogram(dec_img, f"Histogram – Decrypted [{fname}]")


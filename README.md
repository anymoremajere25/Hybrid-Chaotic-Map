# 🌀 Hybrid Chaotic Map Image Encryption (Google Colab)

This project implements a **Hybrid Chaotic Map** (composite Dyadic–Tent function) with **SHA-256 whitening** to generate a strong keystream for **image encryption**.

All experiments (keystream generation, encryption/decryption, histograms, correlation, MSE/PSNR, runtime, etc.), excluding NIST Tests are designed to be run **in Google Colab using Python**.

---

## 📂 Project Structure

```text
Chaos-Hybrid-Encryption/
├── Hybrid Function/
│   ├── composite_function_definition.ipynb
│   ├── hybrid_map_plot.ipynb
│   ├── hybrid_bifurcation.ipynb
│   ├── Hybrid_lyapunov.ipynb
├── Hybrid_keystream/
│   ├── Keystream_generation.ipynb
│   ├── Hybrid_keystream_bytevalue_distribution.ipynb
│   │   └── README.md
│
├── Resources/
│   ├── Images
│   │   
│   └── README.md
│
├── src/
│   ├── step_1_createCompositeKeystream.py
│   ├── step_2_composite_encrypt_decrypt_gray.py
│   ├── step_3_composite_encrypt_decrypt_rgb.py
│   ├── step_4_histogram_analysis_code_rgb.py
│   ├── step_5_histogram_analysis_code_gs.py
│   ├── step_6_chisquare_test_gs.py
│   ├── step_7_chisquare_test_rgb.py
│   ├── step_8_scatterplots_gs.py
│   ├── step_9_scatterplots_rgb.py
│   ├── step_x10_pearson_correlation_rgb.py
│   ├── step_x11_pearson_correlation_gs.py
│   ├── step_x12_sensitivity_gs.py
│   ├── step_x13_sensitivity_rgb.py
│   ├── step_x14_mse_psnr_rgb.py
│   ├── step_x15_mse_psnr_gs.py
│   └── step_x16_runtime_annalysis.py
│
└── README.md   ← main project README

```

Most scripts are **step-by-step** and include comments explaining what each part does.

---

## ✅ How to Use This Project in Google Colab

### 1️⃣ Open Colab and Clone the Repository

In a new Colab notebook cell, run:

```python
!git clone https://github.com/<your-username>/<your-repo-name>.git
%cd <your-repo-name>
```

(Replace `<your-username>` and `<your-repo-name>` with your actual GitHub details.)

---

### 2️⃣ Generate the Composite Keystream

Run:

```python
!python src/step_1_createCompositeKeystream.py
```

This will create a keystream file such as:

```text
keystream_composite_hybrid_4MB_whitened.bin
```

Some scripts expect this keystream filename—adjust inside the script if you renamed it.

---

### 3️⃣ Encrypt & Decrypt Images (in Colab)

Many scripts already use:

```python
from google.colab import files
uploaded = files.upload()
```

So you will:

1. Run the script:

   ```python
   !python src/step_2_composite_encrypt_decrypt_gray.py
   ```

   or

   ```python
   !python src/step_3_composite_encrypt_decrypt_rgb.py
   ```

2. When prompted in Colab, **upload the test image(s)** (e.g. Cameraman, Lena, Baboon, Pepper) and ensure the keystream file is in the working directory (or adjust the path in the script).

---

### 4️⃣ Run Security Analysis Scripts

All analysis scripts can be run the same way from Colab:

#### Histograms

```python
!python src/step_4_histogram_analysis_code_rgb.py
!python src/step_5_histogram_analysis_code_gs.py
```

#### Chi-square tests

```python
!python src/step_6_chisquare_test_gs.py
!python src/step_7_chisquare_test_rgb.py
```

#### Scatterplots (H/V/D correlation)

```python
!python src/step_8_scatterplots_gs.py
!python src/step_9_scatterplots_rgb.py
```

#### Pearson Correlation

```python
!python src/step_x10_pearson_correlation_rgb.py
!python src/step_x11_pearson_correlation_gs.py
```

#### Sensitivity (key sensitivity test)

```python
!python src/step_x12_sensitivity_gs.py
!python src/step_x13_sensitivity_rgb.py
```

#### MSE & PSNR

```python
!python src/step_x14_mse_psnr_rgb.py
!python src/step_x15_mse_psnr_gs.py
```

#### Runtime Analysis

```python
!python src/step_x16_runtime_annalysis.py
```

Most of these scripts will either:

* read images by filename (if they are in the repo), or
* use `files.upload()` to let you upload images manually in Colab.

---

## 🖼️ Image Datasets

The standard test images used in this study (e.g. Cameraman, Lena, Baboon, Pepper, etc.) are **not stored directly** in this repo.

Instead, you can find links to download them in:

```text
resources/images_link.txt
```

You can download those images and then upload them in Colab when scripts ask for `files.upload()`.

---

## 🧪 NIST Test Suite

Instructions and link for the **NIST SP 800-22 statistical test suite** are provided in:

```text
resources/nist_test_kit.txt
```

Use this file as a guide to:

* Download the official NIST test suite
* Prepare the keystream file as input
* Run NIST tests outside Colab (usually locally or on Linux)

---

## 📘 Citation

If you use this work in academic writing:

please cite/ acknowledge
```

---

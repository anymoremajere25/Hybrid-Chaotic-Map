# **Hybrid Chaotic Map**

A novel hybrid chaotic system that combines the **Dyadic Transformation Map** and the **Tent Map** to generate highly unpredictable keystreams for **image encryption** and **cryptographic applications**. The hybrid design enhances sensitivity to initial conditions, randomness, and resistance to classical attacks often seen in chaos-based cryptosystems.

---

## 🔍 **Overview**

This repository contains the implementation of a **Hybrid Chaotic Map**, designed to improve the security and robustness of chaos-based image encryption systems.
The model integrates:

* **Dyadic Map** – strong bit-level chaos and sensitivity
* **Tent Map** – continuous chaotic behavior and parameter flexibility
* **SHA-256 Hashing** – acts as a whitening layer to enhance unpredictability

Together, these components form a stronger keystream generator suitable for modern cryptographic use.

---

## 🧠 **Key Features**

* ✔️ Hybrid chaotic map combining Dyadic + Tent transformations
* ✔️ SHA-256-based key whitening
* ✔️ Keystream generation for image encryption
* ✔️ Histogram and correlation analysis
* ✔️ NIST SP 800-22 randomness testing
* ✔️ Easy-to-follow and modular code structure
* ✔️ Suitable for academic research and publication

---

## 🧬 **Mathematical Model**

The hybrid chaotic map ( H(x) ) is defined as a composition of the Dyadic Map and Tent Map:

1. **Dyadic Transform:**
   [
   x_{n+1} = 2x_n \mod 1
   ]

2. **Tent Transform:**
   [
   T(x)=
   \begin{cases}
   \mu x, & x < 0.5 \
   \mu (1 - x), & x \ge 0.5
   \end{cases}
   ]

3. **Hybrid Formulation:**
   [
   H(x_{n+1}) = T(D(x_n))
   ]

This hybridization increases entropy and improves chaotic complexity.

---

## 🔐 **Application: Image Encryption**

The keystream produced by the Hybrid Chaotic Map is used for:

* Bitwise XOR encryption
* Pixel scrambling
* Diffusion and confusion layers
* Protection against brute-force and statistical attacks

---

## 📁 **Repository Structure**

```
Hybrid-Chaotic-Map/
│
├── src/
│   ├── dyadic_map.py
│   ├── tent_map.py
│   ├── hybrid_map.py
│   ├── keystream_generator.py
│   
│
├── encryption/
│   ├── encrypt_image.py
│   ├── decrypt_image.py
│
├── analysis/
│   ├── histogram_analysis.ipynb
│   ├── correlation_analysis.ipynb
│   ├── nist_test_results/
│
└── README.md
```

---

## 🧪 **Results**

* High key sensitivity
* Flat cipher image histograms
* Very low adjacent-pixel correlations
* Passed most NIST randomness tests
* Strong confusion–diffusion properties

(You may update these results after completing your analysis.)

---

## 🚀 **How to Run**

```bash
git clone https://github.com/anymoremajere25/Hybrid-Chaotic-Map.git
cd Hybrid-Chaotic-Map
python3 encrypt_image.py
```

---

## ✍️ **Citation**


```
Majere, A., (2025). Hybrid Chaotic Function Using Dyadic and Tent Maps for Image Encryption. 
```

---

## 👩‍💻 **Author**

**Anymore Majere**
Graduate Student – Mathematics
Faculty of Mathematics and Natural Sciences,
Universitas Indonesia, Indonesia

---

## 📬 **Contact**

For questions or collaboration:
📧 **mailto:anymoremajere2@gmail.com)**
💼 GitHub: anymoremajere25


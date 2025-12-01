## Hybrid Dyadic–Tent Keystream Generator and Statistical Distribution Testing

This folder contains the implementation and evaluation tools for generating and analyzing keystreams produced by the **Hybrid Dyadic–Tent composite chaotic map**. The system is designed for cryptographic research, randomness testing, and chaos-based encryption experiments.

---

## 📁 Contents

### **1. `hybrid_keystream_generation.py` / `.ipynb`**

Generates a cryptographic keystream using:

* The **Dyadic–Tent composite chaotic map**
* Warm-up iterations to eliminate transient behavior
* Conversion of chaotic states into 8-bit bytes
* **SHA-256 whitening** to enhance randomness

The script outputs a **4 MB keystream file** named:

```
keystream_composite_dyadic_tent_4MB_whitened.bin
```

---

### **2. `keystream_distribution_test.py` / `.ipynb`**

Loads the generated keystream and performs statistical inspection, including:

* **Byte value distribution (0–255)**
* Histogram visualization in **lime color**
* Basic randomness statistics:

  * Mean and variance
  * Shannon entropy
  * Chi-square uniformity test
* Optional bit-level balance test (0/1 distribution)

The resulting histogram demonstrates whether the keystream approximates a **uniform random distribution**, which is required for secure cryptographic keystreams.

---

### **3. Output Figures**

Common outputs stored in this folder:

* `byte_distribution.png`

  * Histogram of byte frequencies, plotted in lime
  * Shows uniformity of the keystream after whitening

* (Optional) additional images: Lyapunov plots, bifurcation diagrams, composite map curves, etc.

---

## 🚀 How to Use

### **Generate a Keystream**

Run:

```
hybrid_keystream_generation.ipynb
```

or:

```bash
python hybrid_keystream_generation.py
```

A 4 MB keystream binary file will be created.

---

### **Analyze Keystream Distribution**

Run:

```
keystream_distribution_test.ipynb
```

or:

```bash
python keystream_distribution_test.py
```

Upload the generated `.bin` file when prompted.
A histogram like the one below will be produced:

```
Byte Value Distribution of composite map Keystream
```

---

## 📚 Purpose

This folder supports experimental evaluation of the **Hybrid Dyadic–Tent chaotic system** for:

* Pseudo-random keystream generation
* Chaos-based cryptography
* Randomness distribution analysis
* Comparing against pure Tent or Dyadic maps

The provided tools help verify whether the composite chaotic system produces high-entropy, statistically uniform outputs suitable for secure encryption applications.

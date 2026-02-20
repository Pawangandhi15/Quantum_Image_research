# Quantum_Image_research
A minimal implementation of single-qubit quantum circuits using Qiskit — exploring superposition, measurement statistics, and hardware noise across local simulation and IBM Quantum backends.

# ⚛️ Quantum Hello World — 1-Qubit Quantum Computing with Qiskit

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-6929C4?style=for-the-badge&logo=ibm)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Local%20%7C%20IBM%20Quantum-orange?style=for-the-badge)

> The simplest possible quantum program — demonstrating **superposition** with a 1-qubit circuit using IBM's Qiskit framework. Runs on both a local simulator and real IBM Quantum hardware.

---

## 📋 Table of Contents

- [What is This?](#-what-is-this)
- [Quantum Concepts](#-quantum-concepts)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Hello World](#1-hello-world)
  - [Local Simulator](#2-local-simulator)
  - [IBM Quantum (Real Hardware)](#3-ibm-quantum-real-hardware)
- [Understanding the Output](#-understanding-the-output)
- [Quantum Gates Reference](#-quantum-gates-reference)
- [Examples](#-examples)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔭 What is This?

This repository is a beginner-friendly introduction to quantum computing using **Qiskit** — IBM's open-source quantum computing framework.

Just like every programmer starts with `print("Hello, World!")`, every quantum programmer starts with a **1-qubit Hadamard circuit** — the quantum Hello World.

```
Classical Hello World:   print("Hello, World!")   → Always outputs: Hello, World!
Quantum Hello World:     H gate + measure          → Randomly outputs: 0 or 1 (50/50)
```

The key difference? The quantum version demonstrates **true randomness** — a fundamental property of nature itself.

---

## ⚡ Quantum Concepts

| Concept | Explanation |
|---|---|
| **Qubit** | Quantum bit — can be 0, 1, or both at the same time (superposition) |
| **Superposition** | A qubit existing in multiple states until it is measured |
| **Hadamard Gate (H)** | Puts a qubit into equal superposition — 50% chance of 0 or 1 |
| **Measurement** | Observing a qubit collapses it from superposition to 0 or 1 |
| **Shot** | One single execution of the quantum circuit |
| **Backend** | The quantum computer or simulator that runs your circuit |

---

## 📁 Project Structure

```
quantum-hello-world/
│
├── 📄 README.md                  ← You are here
├── 📄 requirements.txt           ← Python dependencies
├── 📄 .gitignore                 ← Files to ignore in git
├── 📄 LICENSE                    ← MIT License
│
├── 🐍 hello_world.py             ← Quantum Hello World (start here!)
├── 🐍 local_simulator.py         ← Full local simulator example
├── 🐍 ibm_quantum.py             ← Real IBM Quantum hardware example
│
├── 📁 examples/
│   ├── 🐍 multiple_gates.py      ← X, Y, Z, S, T gate demos
│   ├── 🐍 bloch_sphere.py        ← Visualize qubit on Bloch sphere
│   └── 🐍 compare_results.py     ← Simulator vs real hardware comparison
│
└── 📁 docs/
    └── 📄 quantum_documentation.docx  ← Full line-by-line documentation
```

---

## 📦 Requirements

- Python 3.8 or higher
- pip (Python package manager)

```txt
qiskit>=1.0.0
qiskit-aer>=0.14.0
qiskit-ibm-runtime>=0.20.0
matplotlib>=3.7.0
pylatexenc>=2.10
```

---

## 🚀 Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/quantum-hello-world.git
cd quantum-hello-world
```

### Step 2 — Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### 1. Hello World

The simplest quantum program. Start here.

```bash
python hello_world.py
```

**Expected output:**
```
=== Quantum Circuit ===
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└─┘
c: 1/══════╩═
           0

=== Hello from the Quantum World! ===
Measurement Results: {'0': 498, '1': 526}
  |0⟩ (zero): 498 times
  |1⟩ (one):  526 times

Superposition confirmed! The qubit was both 0 and 1 at the same time.
```

---

### 2. Local Simulator

Runs the circuit on a local quantum simulator — fast, free, and unlimited.

```bash
python local_simulator.py
```

No internet or IBM account needed. Perfect for development and learning.

---

### 3. IBM Quantum (Real Hardware)

Runs the circuit on a **real quantum computer** hosted by IBM.

#### Step 1 — Get a free IBM Quantum account
1. Visit [https://quantum.ibm.com](https://quantum.ibm.com)
2. Sign up for a free account
3. Copy your **API Token** from your profile

#### Step 2 — Add your token
Open `ibm_quantum.py` and replace `YOUR_IBM_TOKEN`:

```python
QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_IBM_TOKEN")
```

#### Step 3 — Run
```bash
python ibm_quantum.py
```

> ⚠️ **Note:** Free IBM accounts get ~10 minutes of quantum compute time per month. Real hardware queues can take minutes to hours depending on demand.

---

## 📊 Understanding the Output

When you run the Hello World, you'll see results like:

```python
{'0': 498, '1': 526}
```

| Key | Value | Meaning |
|---|---|---|
| `'0'` | `498` | The qubit measured as **0** a total of 498 times |
| `'1'` | `526` | The qubit measured as **1** a total of 526 times |

### Why ~50/50?

The **Hadamard gate** creates an exact equal superposition. Over 1024 shots, we expect roughly 512 zeros and 512 ones. The slight variation (like 498 vs 526) is **genuine quantum randomness** — not a bug!

```
No Hadamard:   |0⟩ ──── measure ──→  Always: {'0': 1024}
With Hadamard: |0⟩ ──H── measure ──→  Random: {'0': ~512, '1': ~512}
```

### Simulator vs Real Hardware

| Feature | Local Simulator | IBM Quantum |
|---|---|---|
| Speed | Instant | Minutes to hours (queue) |
| Accuracy | Perfect (no noise) | Noisy (real quantum errors) |
| Cost | Free, unlimited | Free tier: 10 min/month |
| Setup | Just pip install | IBM account + token |
| Best for | Learning & testing | Research & real quantum |

---

## 🔬 Quantum Gates Reference

| Gate | Code | Symbol | Effect |
|---|---|---|---|
| Hadamard | `qc.h(0)` | H | Superposition — equal 0/1 probability |
| Pauli-X | `qc.x(0)` | X | NOT gate — flips 0→1 and 1→0 |
| Pauli-Y | `qc.y(0)` | Y | Y-axis rotation with phase shift |
| Pauli-Z | `qc.z(0)` | Z | Phase flip — leaves 0 unchanged, flips phase of 1 |
| S Gate | `qc.s(0)` | S | 90° phase rotation (√Z) |
| T Gate | `qc.t(0)` | T | 45° phase rotation (√S) |
| Rx | `qc.rx(θ, 0)` | Rx(θ) | Rotation around X-axis by angle θ |
| Ry | `qc.ry(θ, 0)` | Ry(θ) | Rotation around Y-axis by angle θ |
| Rz | `qc.rz(θ, 0)` | Rz(θ) | Rotation around Z-axis by angle θ |

---

## 💡 Examples

### Try different gates

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

# Try swapping qc.h(0) with any of these:
qc.x(0)   # Always gives {'1': 1024} — deterministic flip
qc.h(0)   # Always gives ~{'0': 512, '1': 512} — superposition
# qc.x(0) then qc.h(0) — try combining gates!

qc.measure(0, 0)
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
print(result.get_counts())
```

### Visualize the circuit

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Text diagram
print(qc.draw())

# Matplotlib diagram (saves as image)
qc.draw(output='mpl', filename='circuit.png')
```

---

## 📚 Documentation

A full **line-by-line documentation** Word document is included in the `docs/` folder:

📄 `docs/quantum_documentation.docx`

It covers:
1. Introduction to Quantum Computing
2. Installation & Setup
3. Local Simulator — every line explained
4. IBM Quantum — every line explained
5. Quantum Gates Reference
6. Simulator vs Real Hardware comparison
7. Common Errors & Solutions
8. Complete Glossary (20+ terms)
9. Quantum Hello World — deep dive

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. **Create** a new branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add your feature"`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Open a Pull Request**

### Ideas for contributions
- Add 2-qubit entanglement example
- Add Grover's algorithm example
- Add Deutsch-Jozsa algorithm
- Improve visualizations
- Add unit tests

---

## 🐛 Common Issues

**`ImportError: No module named 'qiskit'`**
```bash
pip install qiskit qiskit-aer
```

**`IBMAccountError: No account found`**
```bash
# Run this once with your token:
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_TOKEN")
```

**`Circuit has no measurements`**
```python
qc.measure(0, 0)  # Don't forget this line before running!
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Useful Links

- [Qiskit Documentation](https://docs.quantum.ibm.com)
- [IBM Quantum Platform](https://quantum.ibm.com)
- [Qiskit GitHub](https://github.com/Qiskit/qiskit)
- [Quantum Computing Textbook](https://learning.quantum.ibm.com)

---

<p align="center">Made with ❤️ for quantum beginners everywhere</p>
<p align="center">⭐ Star this repo if it helped you understand quantum computing!</p>

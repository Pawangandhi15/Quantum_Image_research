"""
=============================================================
  Option 1: Local Simulator
  -------------------------
  Runs a 1-qubit quantum circuit on your local machine
  using Qiskit's AerSimulator. No internet or IBM account
  required. Perfect for development and learning.

  Run:   python local_simulator.py
  Needs: pip install qiskit qiskit-aer
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# ── Build the quantum circuit ──────────────────────────────
qc = QuantumCircuit(1, 1)   # 1 qubit, 1 classical bit

qc.h(0)                     # Hadamard gate → superposition
qc.measure(0, 0)            # Measure qubit 0 → store in bit 0

# ── Display circuit ────────────────────────────────────────
print("=" * 50)
print("  1-Qubit Circuit (Local Simulator)")
print("=" * 50)
print(qc.draw())

# ── Run on AerSimulator ────────────────────────────────────
simulator = AerSimulator()
job       = simulator.run(qc, shots=1000)
result    = job.result()
counts    = result.get_counts()

# ── Results ────────────────────────────────────────────────
print("\n" + "=" * 50)
print("  Results")
print("=" * 50)
print(f"  Raw counts    : {counts}")
print(f"  |0⟩  (zero)   : {counts.get('0', 0)} / 1000")
print(f"  |1⟩  (one)    : {counts.get('1', 0)} / 1000")
print()
print("  Expected ~500 zeros and ~500 ones (50/50 split)")
print("  Variation is normal — quantum results are random!\n")
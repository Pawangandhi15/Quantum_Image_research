"""
=============================================================
  Quantum Hello World
  -------------------
  The simplest quantum program — demonstrates superposition
  using a 1-qubit circuit with a Hadamard gate.

  Run:   python hello_world.py
  Needs: pip install qiskit qiskit-aer
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# ── Step 1: Build the circuit ──────────────────────────────
# QuantumCircuit(1, 1) → 1 qubit, 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate → puts qubit into superposition (50/50)
qc.h(0)

# Measure qubit 0, store result in classical bit 0
qc.measure(0, 0)

# ── Step 2: Print the circuit diagram ─────────────────────
print("=" * 45)
print("  Quantum Circuit Diagram")
print("=" * 45)
print(qc.draw())

# ── Step 3: Run on local simulator ────────────────────────
simulator = AerSimulator()

# shots=1024 means run the circuit 1024 times
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

# ── Step 4: Print results ──────────────────────────────────
print("\n" + "=" * 45)
print("  Hello from the Quantum World! 🌌")
print("=" * 45)
print(f"\n  Measurement Results : {counts}")
print(f"  |0⟩  (zero)         : {counts.get('0', 0)} times")
print(f"  |1⟩  (one)          : {counts.get('1', 0)} times")
print(f"  Total shots         : {sum(counts.values())}")

zero_pct = counts.get('0', 0) / 10.24
one_pct  = counts.get('1', 0) / 10.24
print(f"\n  Distribution → 0: {zero_pct:.1f}%  |  1: {one_pct:.1f}%")
print("\n  Superposition confirmed!")
print("  The qubit existed as BOTH 0 and 1 simultaneously")
print("  until the moment it was measured.\n")
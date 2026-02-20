"""
=============================================================
  Example: Multiple Quantum Gates
  --------------------------------
  Demonstrates different single-qubit gates and their
  effects on measurement outcomes.

  Run:   python examples/multiple_gates.py
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()

def run_circuit(gate_name, qc):
    """Run a circuit and print results."""
    job    = simulator.run(qc, shots=1024)
    counts = job.result().get_counts()
    print(f"  {gate_name:<25} → {counts}")

print("=" * 60)
print("  Quantum Gate Demonstrations (1024 shots each)")
print("=" * 60)
print()

# ── No gate (default |0> state) ───────────────────────────
qc = QuantumCircuit(1, 1)
qc.measure(0, 0)
run_circuit("No gate (|0> state)", qc)

# ── X Gate (NOT / Flip) ───────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)
run_circuit("X gate (NOT / flip)", qc)

# ── H Gate (Superposition) ────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
run_circuit("H gate (superposition)", qc)

# ── X then H ──────────────────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.h(0)
qc.measure(0, 0)
run_circuit("X → H", qc)

# ── H then H (cancels out) ────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.h(0)
qc.measure(0, 0)
run_circuit("H → H (cancels out!)", qc)

# ── Z Gate ────────────────────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.z(0)
qc.measure(0, 0)
run_circuit("Z gate (phase flip)", qc)

# ── S Gate ────────────────────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.s(0)
qc.measure(0, 0)
run_circuit("H → S gate", qc)

# ── T Gate ────────────────────────────────────────────────
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.t(0)
qc.measure(0, 0)
run_circuit("H → T gate", qc)

print()
print("Key observations:")
print("  • No gate      → always 0 (qubit starts at |0>)")
print("  • X gate       → always 1 (flipped to |1>)")
print("  • H gate       → ~50/50  (superposition!)")
print("  • H → H        → always 0 (H is its own inverse)")
print()

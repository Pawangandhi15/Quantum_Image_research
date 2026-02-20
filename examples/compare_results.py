"""
=============================================================
  Example: Compare Results Across Shot Counts
  ---------------------------------------------
  Shows how increasing the number of shots makes the
  results converge closer to the theoretical 50/50 split.

  This demonstrates the Law of Large Numbers applied
  to quantum measurement.

  Run:   python examples/compare_results.py
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()

# Build standard H-gate circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

shot_counts = [10, 50, 100, 500, 1000, 5000, 10000]

print("=" * 65)
print("  Law of Large Numbers in Quantum Measurement")
print("  More shots → closer to theoretical 50/50")
print("=" * 65)
print(f"  {'Shots':<10} {'|0⟩':>8} {'|1⟩':>8} {'0%':>8} {'1%':>8} {'Deviation':>12}")
print("-" * 65)

for shots in shot_counts:
    job    = simulator.run(qc, shots=shots)
    counts = job.result().get_counts()

    zeros = counts.get('0', 0)
    ones  = counts.get('1', 0)
    pct0  = zeros / shots * 100
    pct1  = ones  / shots * 100
    dev   = abs(50.0 - pct0)

    bar = "✓" if dev < 5 else ("~" if dev < 10 else "✗")
    print(f"  {shots:<10} {zeros:>8} {ones:>8} {pct0:>7.1f}% {pct1:>7.1f}% {dev:>10.1f}% {bar}")

print("-" * 65)
print()
print("  ✓ = within 5% of ideal   ~ = within 10%   ✗ = off by 10%+")
print()
print("  Takeaway: With more shots, results converge to 50/50.")
print("  Quantum results are probabilistic — statistics reveal the truth.\n")

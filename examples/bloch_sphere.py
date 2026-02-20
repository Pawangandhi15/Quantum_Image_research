"""
=============================================================
  Example: Bloch Sphere Visualization
  -------------------------------------
  Visualizes the qubit state on a Bloch sphere — a 3D
  representation of all possible qubit states.

  The north pole  = |0⟩
  The south pole  = |1⟩
  The equator     = superposition states

  Run:   python examples/bloch_sphere.py
  Extra: pip install matplotlib pylatexenc
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

def show_bloch(title, qc):
    """Plot qubit state on Bloch sphere."""
    state = Statevector(qc)
    fig   = plot_bloch_multivector(state)
    fig.suptitle(title, fontsize=14, fontweight='bold')
    return fig

# ── State |0⟩ — north pole ────────────────────────────────
qc0 = QuantumCircuit(1)
fig1 = show_bloch("|0⟩ State — North Pole (no gate)", qc0)

# ── State |1⟩ — south pole (X gate) ──────────────────────
qc1 = QuantumCircuit(1)
qc1.x(0)
fig2 = show_bloch("|1⟩ State — South Pole (X gate)", qc1)

# ── Superposition — equator (H gate) ──────────────────────
qcH = QuantumCircuit(1)
qcH.h(0)
fig3 = show_bloch("|+⟩ Superposition — Equator (H gate)", qcH)

# ── Show all ───────────────────────────────────────────────
print("Bloch sphere plots generated!")
print("Close the window to exit.\n")
print("  North pole = |0⟩ (definite zero)")
print("  South pole = |1⟩ (definite one)")
print("  Equator    = superposition (50/50)")

plt.show()

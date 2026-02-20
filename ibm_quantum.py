"""
=============================================================
  Option 2: Real IBM Quantum Hardware
  ------------------------------------
  Runs a 1-qubit circuit on a REAL quantum computer
  hosted by IBM's cloud platform.

  Setup:
    1. Create a free account at https://quantum.ibm.com
    2. Copy your API Token from your profile
    3. Replace YOUR_IBM_TOKEN below with your actual token
    4. Run: python ibm_quantum.py

  Needs: pip install qiskit qiskit-ibm-runtime
=============================================================
"""

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# ── Step 1: Save IBM account (only needed ONCE) ────────────
# After running once, your credentials are stored locally.
# Comment out this line on future runs.
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="YOUR_IBM_TOKEN",   # ← Replace with your real token
    overwrite=True
)

# ── Step 2: Connect to IBM Quantum ─────────────────────────
service = QiskitRuntimeService()
print("Connected to IBM Quantum ✓")

# ── Step 3: Build the circuit ──────────────────────────────
qc = QuantumCircuit(1, 1)
qc.h(0)           # Hadamard → superposition
qc.measure(0, 0)  # Measure

print("\nCircuit:")
print(qc.draw())

# ── Step 4: Select least busy real quantum computer ────────
backend = service.least_busy(operational=True, simulator=False)
print(f"\nSelected backend : {backend.name}")
print(f"Queued jobs      : {backend.status().pending_jobs}")
print("Sending circuit to real quantum hardware...\n")

# ── Step 5: Run on real hardware ───────────────────────────
sampler = Sampler(backend)
job     = sampler.run([qc], shots=1000)

print(f"Job ID: {job.job_id()}")
print("Waiting for results (this may take a few minutes)...")

result = job.result()

# ── Step 6: Display results ─────────────────────────────────
counts = result[0].data.c.get_counts()

print("\n" + "=" * 50)
print("  Results from Real Quantum Hardware")
print("=" * 50)
print(f"  Backend       : {backend.name}")
print(f"  Raw counts    : {counts}")
print(f"  |0⟩  (zero)   : {counts.get('0', 0)} / 1000")
print(f"  |1⟩  (one)    : {counts.get('1', 0)} / 1000")
print()
print("  Note: Real hardware results include quantum noise.")
print("  You may see slightly less perfect 50/50 splits")
print("  compared to the simulator — that's real quantum!")
print()
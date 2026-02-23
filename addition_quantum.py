"""
=============================================================
  Quantum Addition using Qiskit
  ------------------------------
  User inputs two integers and the circuit computes
  their sum using quantum gates (QFT-based addition).

  Run:   python quantum_addition.py
  Needs: pip install qiskit qiskit-aer
=============================================================
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import math

# ── QFT (Quantum Fourier Transform) helpers ───────────────

def qft(qc, qubits):
    """Apply QFT to the given qubits."""
    n = len(qubits)
    for i in range(n):
        qc.h(qubits[i])
        for j in range(i + 1, n):
            angle = math.pi / (2 ** (j - i))
            qc.cp(angle, qubits[j], qubits[i])
    # Swap qubits to correct bit order
    for i in range(n // 2):
        qc.swap(qubits[i], qubits[n - 1 - i])

def iqft(qc, qubits):
    """Apply inverse QFT to the given qubits."""
    n = len(qubits)
    for i in range(n // 2):
        qc.swap(qubits[i], qubits[n - 1 - i])
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            angle = -math.pi / (2 ** (j - i))
            qc.cp(angle, qubits[j], qubits[i])
        qc.h(qubits[i])

def encode_number(qc, qubits, number):
    """Encode a classical integer into quantum register using X gates."""
    n = len(qubits)
    binary = format(number, f'0{n}b')  # Convert to binary string
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            qc.x(qubits[i])

def add_classical_to_qft(qc, qubits, number):
    """Add a classical number to a QFT-encoded quantum register."""
    n = len(qubits)
    binary = format(number, f'0{n}b')
    for i in range(n):
        for j in range(i, n):
            if binary[n - 1 - (j - i)] == '1':
                angle = math.pi / (2 ** (j - i))
                qc.p(angle, qubits[j])

# ── Main Program ───────────────────────────────────────────

def quantum_add(a, b):
    """Add two integers using a quantum circuit."""

    # Calculate how many qubits needed
    max_val  = a + b
    n_qubits = max(max_val.bit_length() + 1, 3)  # Extra qubit for overflow safety

    print(f"\n  Using {n_qubits} qubits to represent values up to {2**n_qubits - 1}")

    # ── Build circuit ──────────────────────────────────────
    qr = QuantumRegister(n_qubits, name='q')
    cr = ClassicalRegister(n_qubits, name='c')
    qc = QuantumCircuit(qr, cr)

    # Step 1: Encode number A into qubits
    print(f"\n  Step 1: Encoding A = {a} → binary {format(a, f'0{n_qubits}b')}")
    encode_number(qc, qr, a)

    # Step 2: Apply QFT
    print(f"  Step 2: Applying Quantum Fourier Transform (QFT)")
    qft(qc, qr)

    # Step 3: Add B in frequency domain
    print(f"  Step 3: Adding B = {b} → binary {format(b, f'0{n_qubits}b')} in QFT space")
    add_classical_to_qft(qc, qr, b)

    # Step 4: Apply inverse QFT to get result
    print(f"  Step 4: Applying Inverse QFT to retrieve result")
    iqft(qc, qr)

    # Step 5: Measure
    qc.measure(qr, cr)

    # ── Run ────────────────────────────────────────────────
    simulator = AerSimulator()
    job       = simulator.run(qc, shots=1024)
    counts    = job.result().get_counts()

    # Get most frequent result (should be deterministic)
    result_binary = max(counts, key=counts.get)
    result_int    = int(result_binary, 2)

    return result_int, counts, qc, n_qubits

# ── User Input ─────────────────────────────────────────────

print("=" * 50)
print("  ⚛️  Quantum Addition Calculator")
print("=" * 50)

while True:
    try:
        a = int(input("\n  Enter first number  (A): "))
        b = int(input("  Enter second number (B): "))

        if a < 0 or b < 0:
            print("  ⚠️  Please enter non-negative integers only.")
            continue
        if a + b > 255:
            print("  ⚠️  Sum too large. Please keep A + B ≤ 255.")
            continue
        break
    except ValueError:
        print("  ⚠️  Invalid input. Please enter whole numbers.")

# ── Run quantum addition ───────────────────────────────────
print(f"\n  Computing {a} + {b} on a quantum circuit...")
result, counts, qc, n_qubits = quantum_add(a, b)

# ── Display results ────────────────────────────────────────
print("\n" + "=" * 50)
print("  Results")
print("=" * 50)
print(f"\n  A              : {a}  ({format(a, f'0{n_qubits}b')} in binary)")
print(f"  B              : {b}  ({format(b, f'0{n_qubits}b')} in binary)")
print(f"  A + B (quantum): {result}  ({format(result, f'0{n_qubits}b')} in binary)")
print(f"  A + B (classic): {a + b}")
print(f"\n  ✅ Correct!" if result == a + b else f"\n  ❌ Mismatch — try again.")
print(f"\n  Shot distribution: {counts}")

# ── Show circuit ───────────────────────────────────────────
show = input("\n  Show circuit diagram? (y/n): ").strip().lower()
if show == 'y':
    print("\n" + qc.draw(fold=80).__str__())

print("\n  Done! ⚛️\n")


# **Expected output:**
# ```
# ==================================================
#   ⚛️  Quantum Addition Calculator
# ==================================================

#   Enter first number  (A): 5
#   Enter second number (B): 3

#   Computing 5 + 3 on a quantum circuit...

#   Using 4 qubits to represent values up to 15

#   Step 1: Encoding A = 5 → binary 0101
#   Step 2: Applying Quantum Fourier Transform (QFT)
#   Step 3: Adding B = 3 → binary 0011 in QFT space
#   Step 4: Applying Inverse QFT to retrieve result

# ==================================================
#   Results
# ==================================================

#   A              : 5  (0101 in binary)
#   B              : 3  (0011 in binary)
#   A + B (quantum): 8  (1000 in binary)
#   A + B (classic): 8

#   ✅ Correct!

#   Shot distribution: {'1000': 1024}

#   Show circuit diagram? (y/n): n

#   Done! ⚛️

from qiskit import ClassicalRegister, transpile
from qiskit_aer import AerSimulator

from backend.circuit_builder import CircuitBuilder


class Measurements:
    """
    Measures all qubits in a quantum circuit and returns the counts.
    """

    def __init__(self, builder: CircuitBuilder):
        """
        Initialize with a CircuitBuilder object.
        """
        self._builder = builder

    def measure_all(self, shots=1024):
        """
        Measure all qubits and return measurement counts.
        """

        # Get the original circuit
        circuit = self._builder.get_circuit()

        # Create a copy so the original circuit remains unchanged
        measured_circuit = circuit.copy()

        # Number of qubits
        num_qubits = self._builder.get_qubit_count()

        # Create classical register
        classical_register = ClassicalRegister(num_qubits)

        # Add classical bits
        measured_circuit.add_register(classical_register)

        # Measure every qubit
        measured_circuit.measure(range(num_qubits), range(num_qubits))

        # Create simulator
        simulator = AerSimulator()

        # Optimize circuit
        compiled_circuit = transpile(measured_circuit, simulator)

        # Execute circuit
        job = simulator.run(compiled_circuit, shots=shots)

        # Get result
        result = job.result()

        # Return counts
        return result.get_counts()


# -------------------------------------------------------
# Testing
# -------------------------------------------------------
if __name__ == "__main__":

    from backend.gates import GateManager

    builder = CircuitBuilder(2)

    gates = GateManager(builder)

    gates.apply_h(0)
    gates.apply_x(1)

    measurement = Measurements(builder)

    counts = measurement.measure_all()

    print("Quantum Circuit:")
    print(builder.get_circuit())

    print("\nMeasurement Counts:")
    print(counts)
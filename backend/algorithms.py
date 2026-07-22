from backend.circuit_builder import CircuitBuilder


class QuantumAlgorithms:
    """
    Collection of basic quantum algorithms and demonstrations.
    """

    def __init__(self, builder: CircuitBuilder):
        self._builder = builder

    def hadamard_demo(self):
        """
        Places qubit 0 into superposition.
        """
        circuit = self._builder.get_circuit()

        if self._builder.get_qubit_count() < 1:
            raise ValueError("At least one qubit is required.")

        circuit.h(0)

    def bell_state(self):
        """
        Creates a Bell State using two qubits.
        """
        circuit = self._builder.get_circuit()

        if self._builder.get_qubit_count() < 2:
            raise ValueError("Bell State requires at least 2 qubits.")

        circuit.h(0)
        circuit.cx(0, 1)

    def ghz_state(self):
        """
        Creates a GHZ State using three qubits.
        """
        circuit = self._builder.get_circuit()

        if self._builder.get_qubit_count() < 3:
            raise ValueError("GHZ State requires at least 3 qubits.")

        circuit.h(0)
        circuit.cx(0, 1)
        circuit.cx(1, 2)


# -------------------------------------------------------
# Testing
# -------------------------------------------------------
if __name__ == "__main__":

    builder = CircuitBuilder(3)

    algorithms = QuantumAlgorithms(builder)

    algorithms.ghz_state()

    print("Quantum Circuit:")
    print(builder.get_circuit())
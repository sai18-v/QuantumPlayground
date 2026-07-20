from qiskit import QuantumCircuit


class CircuitBuilder:
    """
    Responsible for creating and managing a QuantumCircuit.

    This class owns the lifecycle of the circuit and provides
    controlled access to it for other backend modules.
    """

    MIN_QUBITS = 1
    MAX_QUBITS = 32

    def __init__(self, qubit_count: int):
        self._validate_qubit_count(qubit_count)

        self._qubit_count = qubit_count
        self._circuit = QuantumCircuit(qubit_count)

    def _validate_qubit_count(self, qubit_count: int):
        """
        Validate the number of qubits requested by the user.
        """

        if not isinstance(qubit_count, int):
            raise TypeError("Qubit count must be an integer.")

        if qubit_count < self.MIN_QUBITS:
            raise ValueError(
                f"Qubit count must be at least {self.MIN_QUBITS}."
            )

        if qubit_count > self.MAX_QUBITS:
            raise ValueError(
                f"Qubit count cannot exceed {self.MAX_QUBITS}."
            )
        
    def get_circuit(self):
             '''
            return the quantum circuit managed by builder
             '''  
             return self._circuit   

    def get_qubit_count(self):
        """
        Return the number of qubits in the circuit.
        """

        return self._qubit_count
    
    def reset_circuit(self):
         self._circuit = QuantumCircuit(self._qubit_count)


if __name__ == "__main__":
    builder = CircuitBuilder(6)

    print("Circuit created successfully!")

    print("Number of qubits:", builder.get_qubit_count())

    print("\nInitial Circuit:")
    print(builder.get_circuit())

    builder.reset_circuit()

    print("\nAfter Reset:")
    print(builder.get_circuit())             
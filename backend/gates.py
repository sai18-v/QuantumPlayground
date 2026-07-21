from backend.circuit_builder import CircuitBuilder


class GateManager:
    """
    Responsible for applying quantum gates
    to the QuantumCircuit.
    """

    def __init__(self, builder: CircuitBuilder):
        """
        Initialize the GateManager with an existing CircuitBuilder.
        """

        self._builder = builder

    def apply_h(self, qubit: int):
        """
        Apply a Hadamard gate to the specified qubit.
        """

        circuit = self._builder.get_circuit()
        circuit.h(qubit)

    def apply_x(self, qubit: int):
        """
        Apply an X (NOT) gate to the specified qubit.
        """

        circuit = self._builder.get_circuit()
        circuit.x(qubit)
if __name__ == "__main__":

    builder = CircuitBuilder(2)

    gates = GateManager(builder)

    gates.apply_h(0)
    gates.apply_x(1)

    print(builder.get_circuit())        
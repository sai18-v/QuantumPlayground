from qiskit.quantum_info import Statevector
from backend.circuit_builder import CircuitBuilder


class Simulator:
    """
    Executes a quantum circuit and returns its statevector.
    """

    def __init__(self, builder: CircuitBuilder):
        """
        Initialize the simulator with a CircuitBuilder object.
        """
        self._builder = builder

    def run(self):
        """
        Simulate the quantum circuit and return the statevector.
        """
        circuit = self._builder.get_circuit()

        statevector = Statevector.from_instruction(circuit)

        return statevector


# -------------------------
# Testing
# -------------------------
if __name__ == "__main__":

    from backend.gates import GateManager

    builder = CircuitBuilder(2)

    gates = GateManager(builder)

    gates.apply_h(0)
    gates.apply_x(1)

    simulator = Simulator(builder)

    result = simulator.run()

    print("Quantum Circuit:")
    print(builder.get_circuit())

    print("\nStatevector:")
    print(result)
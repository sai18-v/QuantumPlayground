from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

from backend.circuit_builder import CircuitBuilder


class BlochVisualizer:
    

    def __init__(self, builder: CircuitBuilder):
        """
        Initialize with a CircuitBuilder object.
        """
        self._builder = builder

    def generate_bloch(self):
        """
        Generate and return the Bloch sphere figure.
        """

        # Get the circuit
        circuit = self._builder.get_circuit()

        # Get statevector
        statevector = Statevector.from_instruction(circuit)

        # Create Bloch sphere figure
        figure = plot_bloch_multivector(statevector)

        return figure



#Testing

if __name__ == "__main__":

    from backend.gates import GateManager

    builder = CircuitBuilder(1)

    gates = GateManager(builder)

    gates.apply_h(0)

    bloch = BlochVisualizer(builder)

    figure = bloch.generate_bloch()

    figure.show()
    input("Press Enter to exit...")
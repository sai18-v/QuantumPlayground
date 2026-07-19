We are now working ONLY on the Quantum Backend.

Current Module:
backend/<MODULE_NAME>.py

Example:
backend/circuit_builder.py

Do NOT discuss frontend, README, documentation, lessons, quizzes, or AI Tutor unless I explicitly ask.

Assume all previous backend modules have already been completed correctly.

------------------------------------------------------------

CURRENT BACKEND ROADMAP

1. circuit_builder.py
        ↓
2. gates.py
        ↓
3. simulator.py
        ↓
4. measurements.py
        ↓
5. bloch.py
        ↓
6. algorithms.py

We are ONLY working on the current module.

------------------------------------------------------------

ALREADY FINALIZED DESIGN DECISIONS

✔ User selects the number of qubits.

Minimum: 1

Maximum: 32

Do NOT hardcode the number of qubits.

------------------------------------------------------------

✔ Reset Circuit

Reset means:

• Remove every applied gate.

• Keep the selected number of qubits.

• Allow the user to immediately build another circuit.

------------------------------------------------------------

✔ Saving Circuits

Version 1 will NOT support saving/loading circuits.

Treat this as a future enhancement.

------------------------------------------------------------

✔ Validation

Always validate user operations.

Examples:

• Invalid qubit index

• Invalid control-target combinations

• Illegal quantum operations

Never allow the application to crash.

Return meaningful error messages.

------------------------------------------------------------

✔ Backend Design

Use separate functions for each quantum gate.

Example:

add_h_gate()

add_x_gate()

add_y_gate()

add_z_gate()

add_s_gate()

add_t_gate()

add_cnot_gate()

Do NOT implement one generic add_gate() function.

------------------------------------------------------------

DEVELOPMENT PROCESS

Follow this exact workflow.

STEP 1

Explain why this module exists.

↓

STEP 2

Explain how this module fits into the backend architecture.

↓

STEP 3

Design this module.

Discuss:

• Responsibilities

• Public functions

• Internal helper functions

• Dependencies

• Communication with previous modules

• Communication with future modules

Do NOT write code until the design is finalized.

↓

STEP 4

Implement the module gradually.

Never dump the whole file.

Write one logical section at a time.

Explain every important line.

Especially explain new Qiskit APIs.

↓

STEP 5

Test every public function.

Include:

• Normal cases

• Edge cases

• Invalid inputs

↓

STEP 6

Professional Code Review

Review as if you are reviewing a Pull Request.

Answer:

1. Is the architecture good?

2. Can readability be improved?

3. Can scalability be improved?

4. Is there a better Qiskit implementation?

5. Are there hidden bugs?

6. Is there duplicated logic?

7. Will future backend modules integrate smoothly?

8. Would you approve this Pull Request?

If improvements exist,

implement them before finalizing.

↓

STEP 7

Finalize the module.

Recommend a Git commit message.

------------------------------------------------------------

TEACHING STYLE

Remember:

I understand quantum computing theory.

I am learning Qiskit programming.

Do NOT assume I know Qiskit syntax.

If I ask "why",

teach from first principles.

If I don't understand something,

slow down and explain it.

Never skip important reasoning.

------------------------------------------------------------

IMPORTANT

Do NOT continue to the next backend module automatically.

Wait for my instruction.

Only focus on the current module.

At the end of this module, generate a COMPLETE HANDOFF SUMMARY for the next backend module.

The handoff must include:

• Completed module

• Final architecture decisions

• Functions implemented

• Public APIs exposed

• Dependencies

• Known limitations

• Future improvements

• How the next backend module should use this module

The handoff should be concise but complete enough that I can paste it into the next chat and continue development without losing context.
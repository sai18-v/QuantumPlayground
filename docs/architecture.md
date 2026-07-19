# Quantum Circuit Playground - Architecture

## 1. Project Overview

Quantum Circuit Playground is an interactive web application built using Streamlit and Qiskit. It helps beginners learn quantum computing through interactive lessons, circuit simulations, AI tutoring, quizzes, and progress tracking.

---

# 2. High-Level Architecture

User
 │
 ▼
Streamlit Application (app.py)
 │
 ___________________________________________________________________
 │               │               │               │               │
 ▼               ▼               ▼               ▼               ▼
Home         Learn         Playground      AI Tutor         Quiz
 │               │               │               │               │
 ▼               ▼               ▼               ▼               ▼
Markdown      Lessons     Backend Logic      AI Module      Quiz Engine
                              │
                              ▼
                       Qiskit Simulator
                              │
                              ▼
                    Measurement Results
                              │
                              ▼
                        Bloch Visualization

---

# 3. Application Flow

1. User opens the application.

2. Home page is displayed.

3. User selects one of the modules.

    • Learn
    • Playground
    • AI Tutor
    • Quiz
    • Progress

4. Each module performs its own task.

5. Results are displayed.

6. Progress is saved.

---

# 4. Data Flow

User Input

↓

Frontend (Streamlit)

↓

Backend Processing

↓

Qiskit Simulation

↓

Measurement Results

↓

Frontend Visualization

↓

Progress Storage

---

# 5. Module Communication

Pages

↓

Backend

↓

Qiskit

↓

Results

↓

Pages

---

# 6. Future Expansion

• IBM Quantum Hardware
• Drag-and-drop circuit builder
• AI-generated quizzes
• Adaptive learning
• Cloud database

# ElevatorProject

**A Python-based simulation of an intelligent elevator system in a multi-story building.**

---

##  Overview

ElevatorProject is a simulation that models the logic and movement of elevators within a building. The goal is to simulate how multiple elevators interact with user requests across several floors, making decisions about direction, stopping points, and request handling.

This project is written entirely in Python and uses object-oriented principles to represent building components such as elevators, floors, and manage systems.

---

##  Project Structure

```
ElevatorProject/
│
├── main.py              # Main simulation runner
├── building.py          # Represents the building structure (floors + elevators)
├── elevator.py          # Models the behavior of a single elevator
├── floor.py             # Represents a floor in the building
├── button.py            # Models elevator call buttons (inside & outside)
├── factory.py           # Responsible for creating and connecting building elements
├── management.py        # Contains elevator control and dispatch logic
├── neighborhood.py      # Groups floors into neighborhoods for optimized handling
├── globals.py           # Shared global constants and configurations
│
├── sound/               # Sound assets for simulation events (e.g., elevator dings)
│   └── *.wav
│
├── pic/                 # Image assets for visual representation
│   └── *.png / *.jpg
│
└── README.md            # Project documentation
```

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yehezkelmayer/ElevatorProject.git
cd ElevatorProject
```

Make sure you're using **Python 3.x**

### 3. Run the simulation

```bash
python main.py
```

---

##  Features

-  Simulates multiple elevators responding to user requests.
-  Manages direction logic, current floor tracking, and stop requests.
-  Includes management logic to assign requests to elevators intelligently.
-  Supports grouping of floors into “neighborhoods” to optimize dispatching.
-  Audio feedback using `.wav` files to mimic real elevator behavior.
-  Support for image assets (optional GUI/visualization expansion possible).

---

##  Assets

- **Images:** Located in the `pic/` folder. Used for possible GUI elements or debugging views.
- **Sounds:** Stored in the `sound/` folder, played during events like elevator arrival.

---


##  Author

Developed by [Yehezkel Mayer](https://github.com/yehezkelmayer)

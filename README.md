# Emission and Absorption Spectrum Visualization

This Python program is designed to help students at the University of Delaware, particularly those enrolled in **CHEM 106**, better understand emission and absorption spectra. The script calculates the energy change when an electron transitions between energy levels and visually represents the transition using **Turtle graphics**.

## Author

This project was developed by **Furdeen Hasan** [Spring 2021].

## Features
- **Calculates Energy Change**: Determines whether energy is emitted or absorbed based on user-inputted energy levels.
- **Visual Representation**: Uses **Turtle graphics** to depict electron transitions.
- **User Interaction**: Accepts user input for initial and final energy levels.

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed along with the required libraries:

```sh
pip install matplotlib numpy
```

## Usage

Run the script in a Python environment:

```sh
python emission_spectra.py
```

### How it Works

1. The user inputs the **initial (i)** and **final (f)** energy levels.
2. The program calculates the energy difference using:
   
   \[ \Delta E = \frac{-2.178 \times 10^{-18}}{1} \left( \frac{1}{f^2} - \frac{1}{i^2} \right) \]
   
3. It prints the energy change value (in Joules).
4. The program determines whether **energy is emitted** (if i > f) or **absorbed** (if f > i).
5. A visual representation of the transition is drawn using **Turtle graphics**.

## Example Output

```
Enter i energy level: 3
Enter f energy level: 2
-3.027E-19
Energy emitted
```

(Visual transition is displayed)

## Future Improvements

- Implement **Matplotlib** for spectrum visualization.
- Add GUI interface for better user experience.
- Expand functionality to include different elements.

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



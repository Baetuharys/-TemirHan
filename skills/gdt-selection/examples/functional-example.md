# Example: four-hole mounting pattern

Input: a plate has four mounting holes and must mate to a fixed bolt pattern.

Do not immediately assign a position tolerance value.

Reasoning:
- Functional risk is hole-pattern location relative to the mating interface.
- The primary datum should normally represent the main seating surface if that surface establishes assembly orientation.
- Secondary/tertiary datums should represent the functional locating features needed to clock the part.
- Position is a candidate control for the hole axes/pattern because location is the functional concern.
- The numerical tolerance remains an engineering requirement to be determined from mating clearance, bolt pattern, process capability, and inspection method.

Output must separate the selected control type from the still-undetermined tolerance value.

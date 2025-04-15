""""
Purpose: Mass (kg) ko energy (joules) mein convert karna using Einstein’s formula:

E = m × c²

C = 299792458 → speed of light in meters/second
m → user input mass in kilograms
E → calculated energy in joules

"""
C = 299792458  # Speed of light in m/s

def main():
    m = float(input("Enter kilos of mass: "))
    e = m * C**2
    print(f"e = m * C^2...\nm = {m} kg\nC = {C} m/s\n{e} joules of energy!")


main()
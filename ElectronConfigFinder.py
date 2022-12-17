"""Make a program that turns electron configuration to the element name and vice versa."""
def main():
    """Main function."""
    # Get input
    input_type = input("Enter 'e' for electron configuration or 'n' for element name: ")
    input_value = input("Enter the electron configuration or element name: ")
    # Get the element name
    if input_type == "e":
        element_name = get_element_name(input_value)
        print(element_name)
    # Get the electron configuration
    elif input_type == "n":
        electron_configuration = get_electron_configuration(input_value)
        print(electron_configuration)
    # Invalid input
    else:
        print("Invalid input")
def get_element_name(electron_configuration):
    """Get the element name from the electron configuration."""
    # Get the element name
    element_name = ""
    for element in ELEMENTS:
        if ELEMENTS[element] == electron_configuration:
            element_name = element
    # Return the element name
    return element_name
def get_electron_configuration(element_name):
    """Get the electron configuration from the element name."""
    # Get the electron configuration
    electron_configuration = ELEMENTS[element_name]
    # Return the electron configuration
    return electron_configuration
# Dictionary of elements and their electron configurations
ELEMENTS = {
    "Hydrogen": "1s1",
    "Helium": "1s2",
    "Lithium": "[He] 2s1",
    "Beryllium": "[He] 2s2",
    "Boron": "[He] 2s2 2p1",
    "Carbon": "[He] 2s2 2p2",
    "Nitrogen": "[He] 2s2 2p3",
    "Oxygen": "[He] 2s2 2p4",
    "Fluorine": "[He] 2s2 2p5",
    "Neon": "[He] 2s2 2p6",
    "Sodium": "[Ne] 3s1",
    "Magnesium": "[Ne] 3s2",
    "Aluminum": "[Ne] 3s2 3p1",
    "Silicon": "[Ne] 3s2 3p2",
    "Phosphorus": "[Ne] 3s2 3p3",
    "Sulfur": "[Ne] 3s2 3p4",
    "Chlorine": "[Ne] 3s2 3p5",
    "Argon": "[Ne] 3s2 3p6",
    "Potassium": "[Ar] 4s1",
    "Calcium": "[Ar] 4s2",
    "Scandium": "[Ar] 3d1 4s2",
    "Titanium": "[Ar] 3d2 4s2",
    "Vanadium": "[Ar] 3d3 4s2",
    "Chromium": "[Ar] 3d5 4s1",
    "Manganese": "[Ar] 3d5 4s2",
    "Iron": "[Ar] 3d6 4s2",
    "Cobalt": "[Ar] 3d7 4s2",
    "Nickel": "[Ar] 3d8 4s2",
    "Copper": "[Ar] 3d10 4s1",
    "Zinc": "[Ar] 3d10 4s2",
    "Gallium": "[Ar] 3d10 4s2 4p1",
    "Germanium": "[Ar] 3d10 4s2 4p2",
    "Arsenic": "[Ar] 3d10 4s2 4p3",
    "Selenium": "[Ar] 3d10 4s2 4p4",
    "Bromine": "[Ar] 3d10 4s2 4p5",
    "Krypton": "[Ar] 3d10 4s2 4p6",
    "Rubidium": "[Kr] 5s1",
    "Strontium": "[Kr] 5s2",
    "Yttrium": "[Kr] 4d1 5s2",
    "Zirconium": "[Kr] 4d2 5s2",
    "Niobium": "[Kr] 4d4 5s1",
    "Molybdenum": "[Kr] 4d5 5s1",
    "Technetium": "[Kr] 4d5 5s2",
    "Ruthenium": "[Kr] 4d7 5s1",
    "Rhodium": "[Kr] 4d8 5s1",
    "Palladium": "[Kr] 4d10",
    "Silver": "[Kr] 4d10 5s1",
    "Cadmium": "[Kr] 4d10 5s2",
    "Indium": "[Kr] 4d10 5s2 5p1",
    "Tin": "[Kr] 4d10 5s2 5p2",
    "Antimony": "[Kr] 4d10 5s2 5p3",
    "Tellurium": "[Kr] 4d10 5s2 5p4",
    "Iodine": "[Kr] 4d10 5s2 5p5",
    "Xenon": "[Kr] 4d10 5s2 5p6",
    "Cesium": "[Xe] 6s1",
    "Barium": "[Xe] 6s2",
    "Lanthanum": "[Xe] 5d1 6s2",
    "Cerium": "[Xe] 4f1 5d1 6s2",
    "Praseodymium": "[Xe] 4s2 4f3 6s2",
    "Neodymium": "[Xe] 4f4 6s2",
    "Promethium": "[Xe] 4f5 6s2",
    "Samarium": "[Xe] 4f6 6s2",
    "Europium": "[Xe] 4f7 6s2",
    "Gadolinium": "[Xe] 4f7 5d1 6s2",
    "Terbium": "[Xe] 4f9 6s2",
    "Dysprosium": "[Xe] 4f10 6s2",
    "Holmium": "[Xe] 4f11 6s2",
    "Erbium": "[Xe] 4f12 6s2",
    "Thulium": "[Xe] 4f13 6s2",
    "Ytterbium": "[Xe] 4f14 6s2",
    "Lutetium": "[Xe] 4f14 5d1 6s2",
    "Hafnium": "[Xe] 4f14 5d2 6s2",
    "Tantalum": "[Xe] 4f14 5d3 6s2",
    "Tungsten": "[Xe] 4f14 5d4 6s2",
    "Rhenium": "[Xe] 4f14 5d5 6s2",
    "Osmium": "[Xe] 4f14 5d6 6s2",
    "Iridium": "[Xe] 4f14 5d7 6s2",
    "Platinum": "[Xe] 4f14 5d9 6s1",
    "Gold": "[Xe] 4f14 5d10 6s1",
    "Mercury": "[Xe] 4f14 5d10 6s2",
    "Thallium": "[Xe] 4f14 5d10 6s2 6p1",
    "Lead": "[Xe] 4f14 5d10 6s2 6p2",
    "Bismuth": "[Xe] 4f14 5d10 6s2 6p3",
    "Polonium": "[Xe] 4f14 5d10 6s2 6p4",
    "Astatine": "[Xe] 4f14 5d10 6s2 6p5",
    "Radon": "[Xe] 4f14 5d10 6s2 6p6",
    "Francium": "[Rn] 7s1",
    "Radium": "[Rn] 7s2",
    "Actinium": "[Rn] 6d1 7s2",
    "Thorium": "[Rn] 6d2 7s2",
    "Protactinium": "[Rn] 5f2 6d1 7s2",
    "Uranium": "[Rn] 5f3 6d1 7s2",
    "Neptunium": "[Rn] 5f4 6d1 7s2",
    "Plutonium": "[Rn] 5f6 7s2",
    "Americium": "[Rn] 5f7 7s2",
    "Curium": "[Rn] 5f7 6d1 7s2",
    "Berkelium": "[Rn] 5f9 7s2",
    "Californium": "[Rn] 5f10 7s2",
    "Einsteinium": "[Rn] 5f11 7s2",
    "Fermium": "[Rn] 5f12 7s2",
    "Mendelevium": "[Rn] 5f13 7s2",
    "Nobelium": "[Rn] 5f14 7s2",
    "Lawrencium": "[Rn] 5f14 6d1 7s2",
    "Rutherfordium": "[Rn] 5f14 6d2 7s2",
    "Dubnium": "[Rn] 5f14 6d3 7s2",
    "Seaborgium": "[Rn] 5f14 6d4 7s2",
    "Bohrium": "[Rn] 5f14 6d5 7s2",
    "Hassium": "[Rn] 5f14 6d6 7s2",
    "Meitnerium": "[Rn] 5f14 6d7 7s2",
    "Darmstadtium": "[Rn] 5f14 6d9 7s1",
    "Roentgenium": "[Rn] 5f14 6d10 7s1",
    "Copernicium": "[Rn] 5f14 6d10 7s2",
    "Nihonium": "[Rn] 5f14 6d10 7s2 7p1",
    "Flerovium": "[Rn] 5f14 6d10 7s2 7p2",
    "Moscovium": "[Rn] 5f14 6d10 7s2 7p3",
    "Livermorium": "[Rn] 5f14 6d10 7s2 7p4",
    "Tennessine": "[Rn] 5f14 6d10 7s2 7p5",
    "Oganesson": "[Rn] 5f14 6d10 7s2 7p6"
}
main()

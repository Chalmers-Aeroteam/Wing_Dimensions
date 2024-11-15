# Script that dimesions an aircraft based on Raymers approach
# Written by Jesper Nordling
# Last updated 2024-11-11

def main():
    import numpy as np
    from tabulate import tabulate

    from aircraft.main_wing import MainWing
    from aircraft.vertical_tail import VerticalTail
    from aircraft.horizontal_tail import HorizontalTail


    # Parameters
    L_HT = 1014  # Wing MAC to tail MAC
    L_VT = 996.50
    cv_HT = 0.5  # Tail volume ratios
    cv_VT = 0.04

    # Main win
    wing_span = 4000
    wing_cord = 280

    # Horizontal tail
    HT_span = 800    # Horizontal tail span
    c_HT = 200       # Horizontal tail cord
    c_elevator_ratio = 0.4

    # Vertical tail - triangular

    MAC_VT = 329.5
    VT_span = 494
    c_rudder_ratio = 0.3

    # Create objects
    main_wing = MainWing(wing_span, wing_cord)
    vertical_tail = VerticalTail(VT_span, MAC_VT, c_rudder_ratio, L_VT, cv_VT, main_wing)
    horizontal_tail = HorizontalTail(HT_span, c_HT, c_elevator_ratio, L_HT, cv_HT, main_wing)

    # Calculate areas
    wing_area = main_wing.wing_area
    vertical_tail_area = vertical_tail.vertical_tail_area()
    current_vertical_tail_area = 494.326*329.545
    horizontal_tail_area = horizontal_tail.horizontal_tail_area()
    elevator_area = horizontal_tail.elevator_area()
    rudder_area = vertical_tail.rudder_area()

    # Calculate percentages
    vt_percentage = (vertical_tail_area / wing_area) * 100
    ht_percentage = (horizontal_tail_area / wing_area) * 100
    elevator_percentage = (elevator_area / horizontal_tail_area) * 100
    rudder_percentage = (rudder_area / vertical_tail_area) * 100

    # Checks for areas
    if abs(vertical_tail_area - (VT_span * MAC_VT)) > 200:
        print(f"\033[91m\033[1mWARNING:\033[0m Vertical tail area is too far off the expected value.")
        print(f"Current Vertical Tail Area: {current_vertical_tail_area}")
        print(f"Expected Area (VT_span * MAC_VT): {vertical_tail_area}")

    if abs(horizontal_tail_area - (HT_span * c_HT)) > 500:
        print(f"\033[91m\033[1mWARNING:\033[0m Horizontal tail area is too far off the expected value.")
        print(f"Current Horizontal Tail Area: {HT_span * c_HT}")
        print(f"Expected Area (HT_span * c_HT): {horizontal_tail_area}")

    # Print specifications and percentages
    aircraft_specs = [
        ["Wing Span", f"{wing_span:.2f} mm"],
        ["Wing Cord", f"{wing_cord:.2f}"],
        ["Wing Area", f"{wing_area:.2f} mm2"],
        ["Vertical Tail Area", f"{vertical_tail_area:.2f} mm2"],
        ["Vertical Tail % of Wing", f"{vt_percentage:.2f}%"],
        ["Horizontal Tail Area", f"{horizontal_tail_area:.2f} mm2"],
        ["Horizontal Tail % of Wing", f"{ht_percentage:.2f}%"],
        ["Elevator Area", f"{elevator_area:.2f} mm2"],
        ["Elevator % of Horizontal Tail", f"{elevator_percentage:.2f}%"],
        ["Rudder Area", f"{rudder_area:.2f} mm2"],
        ["Rudder % of Vertical Tail", f"{rudder_percentage:.2f}%"]
    ]

    print(tabulate(aircraft_specs, headers=["Parameter", "Value"], tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()

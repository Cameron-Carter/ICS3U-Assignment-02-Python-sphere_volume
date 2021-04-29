#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program calculates the volume of a sphere based on inputted radius

import math


def main():
    # This function calculates volume
    print("This program calculates the volume of a sphere.")

    # Input
    radius = float(input("Enter the radius of a circle (cm): "))

    # Process
    volume = (4 / 3) * math.pi * radius ** 3

    # Output
    print("The volume is {} cm³.".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()

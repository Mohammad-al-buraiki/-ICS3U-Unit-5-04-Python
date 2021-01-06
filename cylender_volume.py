# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is the volume of the cylinder

import math


def volume(radius, height):
    # this function calculates the volume of the cylinder

    # process
    volume = math.pi*radius**2*height

    return volume


def main():
    # input
    while True:
        user_radius_str = input("Enter the radius (mm): ")
        user_height_str = input("Enter the height (mm): ")

        try:
            user_radius_int = int(user_radius_str)
            user_height_int = int(user_height_str)

            # calling functions
            volume_calculated = volume(user_radius_int, user_height_int)
            print("the volume of the cylinder {0:.2f}mm³."
                  .format(volume_calculated))

            break
        except Exception:
            print("that is invalid input")
            print("try again")


if __name__ == "__main__":
    main()

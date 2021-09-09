#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return float(a**(1/2))


def square(a: float) -> float:
    return float(a**2)


def average(a: float, b: float, c: float) -> float:
    return float((a + b + c)/3)


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degre_decimal = angle_degs + (angle_mins/60) + (angle_secs/3600)
    radian = math.radians(degre_decimal)
    return radian


def to_degrees(angle_rads: float) -> tuple:
    angle_degres_decimal = (math.degrees(angle_rads))
    angle_degre = (math.degrees(angle_rads))//1
    angle_minutes = (angle_degres_decimal % 1)*60
    angle_minutes = ((angle_degres_decimal % 1)*60)//1
    angle_secondes = ((angle_degres_decimal % 1)*60) % 1
    angle_secondes = (((angle_degres_decimal % 1)*60) % 1) * 60
    angle_secondes = ((((angle_degres_decimal % 1)*60) % 1) * 60) // 1

    return angle_degre, angle_minutes, angle_secondes


def to_celsius(temperature: float) -> float:
    return (temperature - 32)/(9/5)


def to_farenheit(temperature: float) -> float:
    return ((9/5) * temperature) + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

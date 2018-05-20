#!/usr/bin/env python3

def getDensity():
    """
    Get fluid density from user
    """
    density = float(input('fluid density [kg/m^3] : '))
    return density

def getVelocity():
    """
    Get free stream flow velocity from user
    """
    velocity = float(input('flow velocity [m/s] : '))
    return velocity

def getLength():
    """
    Get length from user
    """
    length = float(input('length [m] : '))
    return length

def getDynViscosity():
    """
    Get fluid dynamic viscosity from user
    """
    dynViscosity = float(input('fluid dynamic viscosity [kg/(m.s)] : '))
    return dynViscosity

def main():
    """
    Main program logic
    """

    density = getDensity()
    velocity = getVelocity()
    length = getLength()
    dynViscosity = getDynViscosity()

    reynoldsNo = (density * velocity * length) / dynViscosity
    print('Renynolds number = {0}'.format(reynoldsNo))

    return

main()

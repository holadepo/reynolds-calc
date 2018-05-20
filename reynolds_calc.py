#!/usr/bin/env python3

def main():
    # get density, flow velocity, length and viscosity from user,
    # then calculte Reynolds number

    density = float(input('fluid density [kg/m^3] : '))
    velocity = float(input('flow velocity [m/s] : '))
    length = float(input('length [m] : '))
    viscosity = float(input('fluid viscosity [kg/(m.s)] : '))

    reynolds_no = (density * velocity * length) / viscosity
    print('Renynolds number = {0}'.format(reynolds_no))

    return

main()

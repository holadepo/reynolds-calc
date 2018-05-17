#!/usr/bin/env python3

def main():
    # get density, flow velocity, length and viscosity from user,
    # then calculte Reynolds number

    density = float(input('fluid density: '))
    velocity = float(input('flow velocity: '))
    length = float(input('length: '))
    viscosity = float(input('fluid viscosity: '))

    reynolds_no = (density * velocity * length) / viscosity
    print('Renynolds number = {0}'.format(reynolds_no))

    return

main()

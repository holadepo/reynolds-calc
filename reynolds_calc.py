#!/usr/bin/env python3
import sys

def getInput(variable):
    '''
    Get input variables from user
    INPUT:
        variable (string): the name of the variable to get. This
            can be 'density', 'velocity', 'length', 'dynViscosity',
            'kinViscosity', or 'reynoldsNo'.
    OUTPUT:
        inputValue (float): the value entered by the user
    '''
    message =   {
                    'density'       :'fluid density [kg/m^3] : ',
                    'velocity'      :'flow velocity [m/s] : ',
                    'length'        :'length [m] : ',
                    'dynViscosity'  :'fluid dynamic viscosity [kg/(m.s)] : ',
                    'kinViscosity'  :'fluid kinematic viscosity [m^2/s] : ',
                    'reynoldsNo'    :'flow Reynolds number'
                }

    inputValue = None
    try:
        inputValue = float(input(message[variable]))
    except KeyError:
        print('variable \'{0}\' not recognised'.format(variable))
        print('Program terminated\n')
        sys.exit()
    return inputValue

def main():
    """
    Main program logic
    """

    # spacing: for clarity
    print('')
    
    # inputs
    density = getInput('density')
    velocity = getInput('velocity')
    length = getInput('velocity')
    dynViscosity = getInput('dynViscosity')

    reynoldsNo = (density * velocity * length) / dynViscosity
    print('Renynolds number = {0}'.format(reynoldsNo))
   
   # spacing: for clarity
    print('')
    
    return

main()

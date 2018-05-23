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
    while True:
        try:
            inputValue = float(input(message[variable]))
        except KeyError:
            print('variable \'{0}\' not recognised'.format(variable))
            print('Program terminated\n')
            sys.exit()
        except ValueError:
            print('Invalid input, please try again')
            continue
        else:
            # successful read
            break

    return inputValue


def calcReynolsNo():
    return 0

def calcDensity():
    return 0
        
def calcVelocity():
    return 0

def calcLength():
    return 0
        
def calcDynViscosity():
    return 0

def main():
    """
    Main program logic
    """

    options = {
        1: 'Reynolds number',
        2: 'Fluid density',
        3: 'Flow velocity',
        4: 'Length',
        5: 'Dynamic viscosity',
        #6: 'Kinematic viscosity'
    }

    # display options
    print('Reynolds Number Calculator\n')
    print('What do you want to calculate?')
    for i in options.keys():
        print('{0}. {1}'.format(i, options[i]))
    print('')
    
    # validate input
    option = None
    while True:
        option = (input('Please select an option (default: 1) (1/2/3/4/5): ')).strip()
        if option == '':
            # this is the default, that is, Reynolds no
            option = 1
            break

        try:
            option = int(float(option))
        except:
            print('Invalid option, please try again')
            continue

        if option in options.keys():
            break
        else:
            print('Invalid option, please try again')
            continue
    print('')

    #process option
    output = None
    if option == 1:
        output = calcReynolsNo()
    elif option == 2:
        output = calcDensity()
    elif option == 3:
        output = calcVelocity()
    elif option == 4:
        output = calcLength()
    elif option == 5:
        output = calcDynViscosity()

    print('{0} = {1}'.format(options[option], output))

    '''
    # inputs
    density = getInput('density')
    velocity = getInput('velocity')
    length = getInput('length')
    dynViscosity = getInput('dynViscosity')

    reynoldsNo = (density * velocity * length) / dynViscosity
    print('Renynolds number = {0}'.format(reynoldsNo))
    '''
   # spacing: for clarity
    print('')
    
    return

main()

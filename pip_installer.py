from subprocess import call


"""
Installs user defined packages from pip during compile time
packages - a list of the names of the required packages
pythons - the python or pythons command you wish to install them to - Default is python and python3
pips - the usable pip commands, Defaulted to pip and pip3
"""


def install(packages, pythons=['python3 ', 'py3 '], pips=['pip ', 'pip3 ']):
    # assigning default values and cleaning the arrays

    print('Now installing ' + str(packages))

    for i in range(len(pythons)):
        pythons[i] = pythons[i].strip()
        pythons[i] += ' '
        if '-m' not in pythons[i]:
            pythons[i] += ' -m '

    for i in range(len(pips)):
        pips[i] = pips[i].strip()
        if 'install' not in pips[i]:
            pips[i] += ' install '
        else:
            pips[i] += ' '

    # handles
    for i in range(len(packages)):
        packages[i] = packages[i].strip()

    # actual installing
    for pip in pips:
        for package in packages:
            try:
                call(pip + package, shell=True)
            except:
                for python in pythons:
                    try:
                        call(python + pip + package, shell=True)
                    except:
                        None

    # clears the terminal
    try:
        call('cls', shell=True)
    else:
        call('clear', shell=True)

########################################################################################################################
# ------ MODULE INITIALIZER                                                                                            #
# Install all required modules and dependencies.                                                                       #
# Only run it once, at the installation of the BimLearning project                                                     #
########################################################################################################################

import os

# os.system('sudo apt install python3')
# os.system('sudo apt install python-tk')
# os.system('sudo apt install python-pip')

pip_commande = 'pip install '
pip_dependences = [
    '--upgrade dnspython',                                              # Upgrade (precaution)
    '--upgrade setuptools',                                             # Upgrade (precaution)
    '--ignore-install enum34 tensorflow',                               # Neural Network module
    'keras==2.1.0',                                                     # Neural Network module
    'numpy',                                                            # Neural Network module
    'matplotlib',                                                       # Neural Network module
    'pandas',                                                           # Neural Network module
    'psycopg2-binary',                                                  # Request module
    'requests',                                                         # Request module
    'olefile',                                                          # File module
    'Pillow',                                                           # Image module
    'flask',                                                            # API module
    'flask_sqlalchemy',                                                 # API module
    'flask_marshmallow'                                                 # API module
]

# Install all dependences with pip
for pip_dependence in pip_dependences:
    os.system(pip_commande + pip_dependence)

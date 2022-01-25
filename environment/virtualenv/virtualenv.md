# virtualenv
We use a module named virtualenv which is a tool to create isolated Python environments.
virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

# Installing virtualenv
    
    pip install virtualenv

# Test your installation:

    virtualenv --version

#Using virtualenv

    virtualenv my_name

# Creating python3 env
    
    virtualenv -p /usr/bin/python3 virtualenv_name

# To create a Python 2.7 virtual environment, use the following command:

    virtualenv -p /usr/bin/python2.7 virtualenv_name

# activating the virtual environment

    source virtualenv_name/bin/activate

# Deactivate the environment
    (virtualenv_name)$ deactivate

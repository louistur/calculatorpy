# Calculator

This is a CLI calculator built using Python 3, built step by step in SCCM4910.

# What it will do

It will be able to add, subtract, multiply and divide two numbers, displaying the result.

# How to run it

You will need python3 installed, python3 --version.
From Calculator folder: ./run.sh
Enter the first number, the operator (+ - * /), then the second number.
The program will print the result. 
To exit, CTRL + C.

To test the program, first enter the virtual environment with:
source /opt/python-venv/sccm-4910/bin/activate

Then check that pytest is installed with:
python3 -m pytest --version

Then you can run the testing script by running ./check.sh in the calculator folder.
Make sure that the program has worked correctly by running echo $? immediately after,
a value of 0 means that the program worked successfully.

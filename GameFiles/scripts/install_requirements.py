import subprocess
import sys
import os

# Define Install_Reqs() function which will be use in main.py to pip install 
# python libraries used for the program.

def Install_Reqs():
    file = os.path.join(os.path.dirname(__file__), "..", "requirements.txt")
    if os.path.exists(file):
        # if requirements.txt exists, pip install the libraries needed for the program,
        # using try and except, so it doesn't cause an error. 
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r",file])
            print("All packages installed ✅")
        except Exception as exception:
            print(f"Error downloading all the required packages ❌: {exception}")
    else:
        # if requirements.txt doesn't exist, create one as well as add the libraries needed.
        print(file, "does not exist. Creating one...")

        # will open the requirement.txt if exists and override it, if doens't exist then will
        # make one.
        with open(file, "w") as f:
            f.write("tensorflow\n")
            f.write("numpy\n")
            f.write("pygame\n")
        print(file, "created!")

        # Use of recursion to rerun the function now that requirements.txt exists
        Install_Reqs()


        

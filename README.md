# Getting started

To get started, check-out the git repository with the exercise:

```bash
git clone ttps://github.com/ASvyatkovskiy/PythonWorkshop
cd PythonWorkshop
```
If you do not have git or you do not wish to install it, just download the repository as zip, and unpack it:

```bash
wget https://github.com/ASvyatkovskiy/PythonWorkshop/archive/master.zip
#For Mac users:
#curl -O https://github.com/ASvyatkovskiy/PythonWorkshop/archive/master.zip
unzip master.zip
```

Then change to the the repository folder.

## Install Python3

To install Python3 for this course got to: https://www.python.org/downloads/release/python-351/
Scroll down to the "Files" section and select file which best matches your OS.
Once finished with the installation, test it by typing:

```bash
python3
```

in the command line, it will open up a Python REPL, printing out the details on the version of Python.

## Install Anaconda and pip

Two package managers are going to use for this course: Anaconda and pip3. 
These  package managers are also available on Princeton clusters. 

If you have not installed Anaconda yet, please go to this page: https://www.continuum.io/downloads
and select the version for Python 3 compatible with your operating system.

Type:

```bash
conda --help
```

to confirm the installation is succesful.

## Create isolated Anaconda environment for the course

Once this is installed, create an isolated Anaconda nevironment for today's course, and install ipython notebook in it:

```bash
conda create -n PythonWorkshop python=3.5.1 anaconda
source activate PythonWorkshop
conda install --name PythonWorkshop ipython-notebook=4.0.4
conda install --name PythonWorkshop pip
```

Note: pip3 is a part of the stock install for Python > version 3.4. But we need a different pip - the one from Anaconda to be able to use it inside our isolated environment.

## Start the interactive notebook

```bash
ipython3 notebook
```

After the notebook is opened, navigate to the workshop folder and open the 0.Setup.ipynb from the browser window.


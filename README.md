# Getting started

To be able to follow the workshop exercises, you are going to need a laptop with Anaconda and Tensorflow installed. Following instruction are geared for Mac or Ubuntu linux users.

## Download and install Anaconda

Please go to the following website: https://www.continuum.io/downloads
download and install *the latest* Anaconda version for Python 2.7 for your operating system. 

Note: we are going to need Anaconda 4.1.x or later

After that, type:

```bash
conda --help
```
and read the manual.
Once Anaconda is ready, download the following requirements file: https://github.com/ASvyatkovskiy/PythonWorkshop/blob/master/requirements.txt
and proceed with setting up the environment:

```bash
conda create --name PythonWorkshop --file requirements.txt
source activate PythonWorkshop
```

## Install Tensorflow

Select a binary and install protobufs, and TensorFlow. For this workshop, we will use CPU-only version of Tensorflow.

Mac users:

```bash
#source activate PythonWorkshop
pip install --user --upgrade protobuf
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.10.0-py2-none-any.whl
pip install --user --upgrade $TF_BINARY_URL
pip install --user --upgrade Pillow
```

Ubuntu linux users:

```bash
sudo apt-get install --user python-pip python-dev python-matplotlib
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
sudo pip install --user --upgrade $TF_BINARY_URL
sudo pip install --user --upgrade Pillow
```

Test the installation was succesfull, launch the Jupyter notebook

```bash
jupyter notebook
```
create a new notebook selecting the Python kernel using your anaconda environment from the upper right dropdown menu, and type:

```python
In [1]: import tensorflow as tf
        tf.__version__
        
Out[1]: 0.10.0
```

### Check-out the git repository with the exercise 

```bash
git clone https://github.com/ASvyatkovskiy/PythonWorkshop
```

If you do not have git or you do not wish to install it, just download the repository as zip, and unpack it:

```bash
wget https://github.com/ASvyatkovskiy/PythonWorkshop/archive/master.zip
#For Mac users:
#curl -O https://github.com/ASvyatkovskiy/PythonWorkshop/archive/master.zip
unzip master.zip
```

## Start the interactive notebook

Change to the the repository folder, and start interactive jupyter (ipython) notebook:
```bash
cd PythonWorkshop
jupyter notebook
```

After the notebook is opened, navigate to the workshop folder and open the 1.PythonBasics.ipynb from the browser window.

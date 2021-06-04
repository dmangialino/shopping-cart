# shopping-cart

## Installation
Clone this repository to your local machine. Then, using the command line, navigate to the root folder of the repository.


## Setup
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env"

conda create -n shopping-env python=3.8
conda activate shopping-env


After activating the virtual environment, run the below to install packages dependencies (identified in the requirements.txt file):

pip install -r requirements.txt 


## Create .env file to specify sales tax rate

After activating the environment and installing the required packages, create a .env file to specify a sales tax rate to be used by the program. To do so, navigate to the root directory of the local repository and create a new file called ".env"

In the file, copy the below text. Provide the value of the sales tax rate where .0875 appears in the below (i.e., if you wish to use a sales tax rate other than 8.75%, replace the .0875 with the desired value).

TAX_RATE = .0875


## Run the App
To run the application, run the below command on the command line:

python shopping_cart.py
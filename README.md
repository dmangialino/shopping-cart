# shopping-cart

## Installation
Clone this repository to your local machine. This program utilizes the "products.csv" file for the grocery store's product inventory. 

Be sure to also make a copy of the "products.csv" file and save it in the root directory.

Then, using the command line, navigate to the root folder of the repository.

## Setup
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env"

```sh
conda create -n shopping-env python=3.8  
conda activate shopping-env
```

After activating the virtual environment, run the below to install packages dependencies (identified in the requirements.txt file):

```sh
pip install -r requirements.txt 
```

## Create .env file

After activating the environment and installing the required packages, create a .env file to specify environment variable values to be used by the program. To do so, navigate to the root directory of the local repository and create a new file called ".env".

We will configure three variables in the .env file (`TAX_RATE`, `SENDGRID_API_KEY`, and `SENDER_ADDRESS`), as outlined in the following two sections.

### Configure Tax Rate

In the file, copy the below for the `TAX_RATE` environment variable. Provide the value of the sales tax rate where .0875 appears in the below (i.e., if you wish to use a sales tax rate other than 8.75%, replace the .0875 with the desired value).

```sh
TAX_RATE = .0875
```

### Configure SendGrid Account and Variables

To enable email receipts, first sign up for a SendGrid account using the following link: https://signup.sendgrid.com/

Then, follow the instructions to complete the "Single Sender Verification" by clicking the link in a confirmation email sent to the email you provided to verify your account.

Next, create a SendGrid API key using the following link. Be sure to select "full access" permissions: https://app.sendgrid.com/settings/api_keys

Once the API key is generated, copy the value and store it in an environment variable in the .env file called `SENDGRID_API_KEY`.

Lastly, add a a `SENDER_ADDRESS` variable to the .env file and specify the sender address for the program to utilize. Be sure to use the same email address as the single sender address associated with the SendGrid account you created.

## Run the App
To run the application, run the below command on the command line:

```sh
python shopping_cart.py
```

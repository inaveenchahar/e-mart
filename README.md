# e-mart now WatchPool

                                 e-mart now WatchPool


#About WatchPool


WatchPool is an e-commerce website which can be used to sell any item(currently named WatchPool)
.  
It has all functionally like adding product to cart, payment and order tracking(manual). It uses razorpay as its 
payment gateway.  

There is a separate  dashboard created for seller, where all order(pending, shipped, delivered)
can be seen together and from there seller can easily update the order status(pending to shipped, shipped to deliver).
Seller must be superuser.


# Technology Used
Django, Html5, Css, Bootstrap

# Structural description of the project
Contains following apps:
1) accounts - all user account related models like address and password reset view
2) cart - contains all views/templates necessary for cart to work
3) main - for homepage
4) products - category, product models and their detail page
5) seller - seller dashboard and views to change order status easily.
6) e-mart -->  is the project directory

# INSTALLATION GUIDE FOR UBUNTU 16+

## Step1:
Open the terminal in the directory where you want to download/clone the project. Run
``` 
git clone https://github.com/inaveenchahar/e-mart.git
```

# GUIDE TO USE THE PROJECT

## Step1: Setting up the virtual environment 
(create a virtual environment named 'env')
```
python3 -m venv env
```
(activate the environment)
```  
source env/bin/activate  
```
## Step2: Change into project directory 
``` 
cd watchpool
```
name it whatever is necessary or required

## Step3: Set up the system requirements
``` 
pip install -r requirements.txt 
```

Note: If an error occurs during the installation of a pre-installed library then remove that particular library from requirements.txt and execute the command again to complete the remaining installations.


## Step4: Get secret id/key
Go to razorpay.com and get your own test secret id and key. Next,
visit google to get your email key.

Now create a new file with extension .env in e-mart app and paste your keys  
```
RAZORPAY_KEY_ID = "your own key id"
RAZORPAY_KEY_SECRET = "your key secret"

EMAIL_USER = your gmail
EMAIL_PASSWORD = 'gmail secret key'
```



## Step5: Make Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Step6: Run server

```
python3 manage.py runserver
```


## Happy Reading
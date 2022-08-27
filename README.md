DJANGO
                                          -By Kiran Oruganti


	Django is a framework for web applications. To build a website we need hmtl,css,javascript. HTML is for designing ,CSS is for styling and JAVASCRIPT is to make page interactive to users .HTML,CSS,JAVASCRIPT are for frontend .But what about backend in backend we have to write the code to look dynamic .for eg Instagram everyone has different feed acc to their taste. We use PHP,JAVA.JAVASCRIPT,SERVLET,PYTHON. But how can I do with it? Python. That’s where Django comes into place. Using Django Framework will write back end code for the publications using Python. Generally we use MVC(MODEL VIEW CONTROLLER) which helps us to build a proper web application but in Django we don’t use MVC we use MVT(MODEL VIEW TEMPLATE).
Why do you use Django when there are other frameworks available in Python?
1.	Fast= Django helps us to build application faster.


2.	Components= to do a dish we need lots of components like. Etc,Etc. Same way. Application we must have database, login credentials and so on. All these components comes bundled in Django. But it is an advantage and it is also an Advantage and a disadvantage because. All of the all the components will be on you. You have to take care of it by yourself.

3.	Security= nowadays users need lots of security. For example, I am an Instagram user  and I’ve been sending messages to my friend and that message should be secured. That Security is provided by Django

4.	Scalability= For example, I build an application which is limited to 1000 users, but all of a sudden you can famous. And 1 lakh people are trying to access the website then Django provides me the feature to increase the scalability of my website.


DJANGO SETUP
If you want to install Python in your system. Make sure to check box on add Python 3.9 to path while downloading Python.
Go to cmd and install Django
1.	First let’s create a virtual environment in Python. The use of virtual environment is for different different programs they have different different versions. For example Jarvis project interpretor version is 3.9. If I want to use 3.3 version for Django Project, I can use it using virtual environment. It does not make any conflict to my 3.9 version of Jarvis project interpretor
	
	Pip install virtualenvwrapper-win

Now lets create a virtual environment of our choice lets say it as test.Type the following command in cmd

	mkvirtualenv  test
 
now you can we enteretd into a virtual environment before our C:\Users we have (test) in bracket

Here we have to install our Django 
(test) C:\Users\kiran>pip install Django
To Check our Django version type (test) C:\Users\kiran>django-admin --version 

Our django version is 4.1.To go to virtualenv test type 
workon test command 
 Now lets create a folder and add our project in the folder
Command to create a folder in django
	(test) C:\Users\kiran>mkdir django project
 
As you can see a folder named django projects has been created and its empty


Now Lets Create a project in the django projects folder the project name is ecommercewebsite 
(test) C:\Users\kiran> django-admin startproject ecommercewebsite

 

As soon as I enter the command. A folder named ecommercewebsite has been created in djangoproject folder and in that I am having 2 files one is a manage.py file(yellow line)  another folder named ecommercewebsite in which I have python files(represented with red line).

url.py = as we are building a website we need a url file 
wsgi.py= used to deploy our website into the server
__init__.py= we don’t use it so no need to talk about it 
Settings.py= very imp file

Even though. We did not create any application we can run the server using manage.py file But to run a website database. This is where Django helps us. Django says ”I will provide you a lite database you can run your server in it” 
Before you run the server change your directory to the project directory(cd ecommercewebsite) otherwise you get an error 
Command to run the server 
	python manage.py runserver

As soon as you run the above command a db.sqlite3 will be created in project folder
 
After you run python manage.py runserver you will get a server link click on it and paste it in your chrome a django website will open

You can stop the server py pressing CTRL+C in laptop and CTRL+BREAK IN PC
When you don’t run the server or stop the server your webpage will not open

HOW TO CREATE AN APP IN Django?

 
Now lets print hello world on our webpage for that we need an IDE here lets use VS Code.Open ur project folder in VSCode
If you open the following folder you cannot create appp or run it
 

You have open ecommerce folder not djangoprojects folder

 
Now lets create an app in django named calc for that you have to type following command before that make sure you are in virtualenv (test)
	Python manage.py startapp calc
The moment you press enter a folder named calc will be created
 
	
We have urls.py in admin but we should also have it in url because we should also use it 
So create a urls.py folder in calc app and add urls.py file in it also and write the following code
 

Write the following code in views.py of calc app folder
 
Here we have created the method home as we have used it in urls.py of calc app
If we run the server we will get an error because we did not specify the path in urls.py of ecommerce website folder so lets do it
Type the following code in urls.py of ecommerce website folder 
 

Now type the command python manage.py migrate  this migrates all over changes to the code 

Now run the server and see you can see HelloWorld in  the website

 

What we have done is not a static page. It is a dynamic pace because we have sent the Hello world from BackEnd(Python)
We can also use HTML tags in views.py 
  
I used <h1> and as you can see it has reflected in the page but when we create a bigger webpage it is very hard to write HTML tags for every line.This is very Django helps us with it templates 
DTL(Django Templet Language)
Create a folder in ecommerce website. The folder name is templates. Create home.HTML file in templates folder. Write the following code in it.
 

Now write the following code in views.py of CALC folder. 
 
HTTP response we are using the render here
Now Open settings.py file folder of  E-commerce website folder. And write the following code. 
 
Go to TEMPLATES list in the settings.py code and add the templates path using os module in ‘DIRS’
Now run the server and open webpage
 

Now do the following changes
 

As you can see I have created a name key in view.py(of calc app) and used it in home.htmlby using {{name}} (two flower brackets).When I did this and ran the server the changes are reflected in the browser .So when ever I change  name in views.py it reflects in website 
That’s what we called Dynamic Content.We have created Dynamic content using DTL(Django Template Language)

Create a base.html file in templates folder in this base.html we have the base template for all pages .Type the following code in base.html and home.html and run the server you can see cyan color in background
 

Download  jinja extension otherwise it wont work 

Addition of Two Numbers in Django
Create a results.html folder in templates and write the following code in url.py,result.html,home.html,views.py
 
Run the server and do the following

 
As you can see when we are entering 2 numbers and clicked in submit we are getting the result
This is a dynamic webpage here users wont give 5 and 6 always they will change even if the change also we will get the output acc to user convenience
 

POST VS GET(HTTP REQUEST METHODS)
When you want to fetch resource(image etc) from a website we use GET and when we want to send or submit data to a website from backend we use POST
PUT VS DELETE
PUT is used to update the data in the server and DELETE is to delete data from the server
GET 
When I use get in the address bar we can see what we have done their 
To get rid of it we use csrf tokens(u can see in home.html) what this basically does is it hides what user has done 
 
Csrf is a middleware which is given by default by django to developers we have to use it. To use it we write it in home.html file 


MVT(Model View Template)

 

User want to fetch data so he sends a request that request will go to webapplication here it is django so the request will go to django framework.In django framework when we do a specific project we will get urls.py folder. In the urls we will to all the mapping like where we want to send request etc etc. That navigation will be send to views We will write the business logic in views
 
Views will use the model object and template .What data has to be sent from  the template.py will be decide by the view and connection with the models will be done by view
Simple Explanation
User will send request to Django, Django will uses URL and URL will call Views and Views will set models and templates.
Static Files
Our website UI is not so great its just basic one.Designers design the UI templates here we will download it from the website.Templates will be free and paid here lets download free one
Search travello colorlib and download it
 
As we are creating a new website we have to create new app

CREATING A NEW APP NAMED AS TRAVELLO
		python manage.py startapp travello

 
Copy the index.html in templates folder of ecommercewebsite

Create a urls.py file in travello folder and type the following code in urls.py,views.py(of travello)
What we have basically done here is pasted the index.html file in template folder of ecommercewebsite
In urls.py and views.py we have specified the path of index.html
After doing this run the server

 

After I run the server I got the same page
 

The thing we have done wrong here is I did not specify the path of (travello.urls) in urls.py of ecommercewebsite folder .Its the same calc.urls that’s why we are getting the same page
Change it to travello.urls as follows 

Now run the server 

 
As you can see the travello website opened but there are no image.We just downloaded the html file but we did not get static files(image files )in it so we have to set the static files in it.
To have proper layout we should use CSS
Creating Static folder
Lets Create a static folder named as folder in 1st ecommercewebsite folder  and paste the static files in it.

 

Write following code in settings.py 
What we are basically doing here is we have are setting static folder path and saying django to collect the static folder files to asset folder 
Type the command python manage.py collectstatic after creating assets folder
Why assets means we have kept name assets in the code


Before running the above command a folder named in assets in ECOMMERCEWEBSITE folder (not small letters one) see above image for clear clarity if you see below one u will confuse
 

The assets folder will have the same folders as static folder but assets has one file extra that is css files in it


When I run the server I get the same output with no changes.
 

To get rid of this we have to add jinja code in it and add  {} where ever there is css and static word  in index.html file
What {} do is they help understand the Django >if we don’t place{} we get error and page wont load .  
You have to add {} in the entire code where ever there is static or css 



Now run the server and load the page
 

As you can see the page has loaded
But you cannot do any actions in this as of now when u click on home or any button you will get errors
 

As you can see the price here is static but the price wont be the same all the time it changes regularly we have to make the price dynamic so lets do it
 
As you can see the price here is static but the price wont be the same all the time it changes regularly we have to make the price dynamic so lets do it
The price of Hyderabad is $650 lets change it.(if you want to  enjoy entire hyderabad city this is the amount you have to pay)
 
Write the above code in models.py and views.py of travello folder and when you make changes here it reflects in your webpage.
We can enter any number of data in views.py.You can even add your own city in it this is possible because of the for loop we placed in index.html file
 

In our webpage we have special offer for all the cities but only few cities must have special offer then only it makes sense
For that add offer varibale and make its data type bool in model.py if you want to keep special offer keep it true otherwise keep it else in views.py (dest.offer=True or False)
 

Write a if statement in index.html
 
Run the server
 
As you can see special offer is only available for Hyderabad and banglore

# NEXA_COURSE_ORDERING_PROGRAM
A new technology from NEXA Industries, this project is able to organize all courses you have in a excel file. Then you can obtain details from prompts that you give before to start the algorithm genetic. 

Created by his owner: **Mauricio Castillo** 

## GUIDE ABOUT INSTALLATIONS DONE

#### RULES
``RULES``
``REQUERIMENTS.TXT``
    If you want to know what packages you've installed in a virtual environment, you can use the next
    command line where it shows all packages required for intallation:

    pip freeze >  requeriments.txt

    * This one give you a requeriments.txt file, where you need to install (if you have a virtual environment
    you must be inside) using the next command line:

    pip install -r requirements.txt

    * This one will satisfy all the required installations.

#### VIRTUAL ENVIRONMENT
``1.-``
``VIRTUAL ENVIRONMENT``
For a virtual environment in your computer where you can try the code without installing them for global
>> Installation: **pip install virtualenv**

``STEP 1``	
    Create the new virtual environment using the next command line 
        (you must do this step if you want to create a virtualenv for your pip installations)
    
    Type the next command line in your text editor where "my_virtualenv" is the virtual environment name 
    selected typed by default(me), you can change this option if you prefer: 

    virtualenv my_virtualenv

``STEP 2``
    Once created the virtual environment, we can activate this one using the next command line in your 
    prefered text editor (where you did the previous step):

    my_virtualenv\Scripts\activate
    
    * You will see the name of your virtual environment in parentheses on the indicator of your terminal
    * "my_virtualenv" is the default name I chose, if you chose a different name in step 1, 
    in this step you need to change the name like in the previous step

``STEP 3``
    Once you have stopped working, you can deactivate the virtual enviroment with the next command line:

    deactivate



#### CUSTOMTKINTER
``2.-``
``CUSTOMTKINTER`` For the main interface.
>> Installation: **pip install customtkinter**
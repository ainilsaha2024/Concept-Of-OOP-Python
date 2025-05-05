# Importing necessary modules
import google.generativeai as genai  # Google Gemini AI SDK
import os  # For environment variable access (if needed in future)


# Class 1: NLPmodel
# OOP Concept Used:
# Encapsulation (model logic encapsulated in method)
# Reusability (can be inherited and reused)


class NLPmodel:
 # This class represents a base model handler for the NLP app
    def get_model(self):
    # Hardcoded API key for Gemini model - should be replaced with environment variable for security
        GOOGLE_API_KEY = "AIzaSyBdT2Hf0YlV_CEcOycn43pyrytSis-_PYY"
        try:
            # Configure the API key for Gemini model
            genai.configure(api_key=GOOGLE_API_KEY)
            # Load the Gemini model (version: 2.0 flash)
            model = genai.GenerativeModel("gemini-2.0-flash")
            return model  # Return the model object
        except Exception as e :
            print(e) # Catch and print any exception that occurs

        self.fast_menu()




# Class 2: NLPapp (Inherits from NLPmodel)
# OOP Concept Used:
# Inheritance (NLPapp inherits NLPmodel)
# Encapsulation (__database is private)


class NLPapp(NLPmodel):
    # Private attribute to hold user data (email -> [name, password])
    def __init__(self):
        self.__database ={}
         # Starts with the first menu
        self.fast_menu() 


# Method: fast_menu()
# Concept:
# Menu-driven control flow
# Uses encapsulated methods  

    def fast_menu(self):
        # Displays the initial menu for Register/Login/Exit
        fast_input = input("""
        HI ! How would you like to proceed ?
         1. Not a member ? Register
         2. Already a member ? Login
         3.Bhai galati se aa gaya kia ? exit              
        """)

        if fast_input =="1":
            # Register
            self.__register()
        elif fast_input =="2":
            # Login 
            self.__login()
        else:
            # Exit 
            print("GOOD BYE !")
            exit()


# Method: second_menu()
# Concept:
# Layered menu system
# Further abstraction of features
    
    def second_menu(self):
        # Displays NLP feature options
        second_input = input("""
        HI ! How would you like to proceed?
        1. Sentiment Analysis
        2. Language Translation
        3. Language detection
                            
        """)
        if second_input =="1":
            # sentiment analysis
            self.__sentiment_analysis()
        elif second_input =="2":
            # Language Translation 
            self.__language_translation()
        elif second_input =="3":
            # Language detection
            self.__language_detection()
        else:
            # Exit 
            print("GOOD BYE 2nd menu!")
            exit()


#  Method: __register()
# Concept:
# Data encapsulation with __database
# Basic user management

    def __register(self):
        # Handles new user registration
        name = input("Enter your name :")
        email = input("Enter your Email :")
        password = input("Enter your password :")
        # Check if user already exists
        if email in self.__database:
            print("User email already exists !")
        else:
            self.__database[email] = [name,password]
            print("User registeres successfully ! now you can Login !")
            self.fast_menu()



# Method: __login()
# Concept:
# Access control
# Condition-based flow

    def __login(self):
        # Handles user login
        email = input("Enter your email :")
        password = input("Enter your password :")

        if email in self.__database:
            if self.__database [email] [1] == password:
                print("Login successful !")
                self.second_menu()
            else:
                print("Email not found . please register first !")
                self.fast_menu()


# Method: __sentiment_analysis()
# Concept:
# Polymorphism (super() to access parent method)
# External API interaction


    def __sentiment_analysis(self):
        user_text = input("Enter your text ")
        model = super().get_model()
        response =model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text 
        print(results)
        self.second_menu()


# Method: __language_translation()
# Concept:
# Abstraction of translation logic
# Reuse of parent class method


    def __language_translation(self):
        user_text = input("Enter your text ")
        model = super().get_model()
        response =model.generate_content(f"Give me the hindi transilation of this sentence: {user_text}")
        results = response.text 
        print(results)
        self.second_menu()


#  Method: __language_detection()
# Concept:
# Language detection using AI
# Same structure reuse as other features

    def __language_detection(self):
        user_text = input("Enter your text ")
        model = super().get_model()
        response =model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text 
        print(results)
        self.second_menu()


# Script Execution Entry Point
# Concept:
# Ensures the class runs only when the file is executed directly

if __name__ == "__main__" :
    nlp = NLPapp()


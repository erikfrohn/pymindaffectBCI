
#import necessary libraries
import streamlit as st

"""
A class that holds an array of all the pages in the application
It's also used to create/edit the array and run a particular page
"""
class MultiPage: 
  
"""
Constructor of the class, it creates the array that holds the references to the pages

...

Methods
-------

add_page(self, title, func)
         Appends a new page to the array created by the constructor
         
"""

    def __init__(self):

        self.pages = []
    
    def add_page(self, title, func):
        """
        Appends a new page to the array, using the name of the page and a reference to the app method function call.
        
        Parameters
        ----------
        title : str
                Name of the page
        func: 
             Holds the definition of the function call to the app method of the particular page
        """
        self.pages.append(
            { 
                "title": title, 
                "function": func
            }
        )

    def run(self):
        """
        Calls the app function of the page seleected by the user
        """

        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        page['function']()

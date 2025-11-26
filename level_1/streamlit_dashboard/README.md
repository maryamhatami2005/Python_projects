# Password Generator Dashboard

The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. It allows users to generate different types of passwords quickly, either randomly, as a memorable sequence of words, or as a pin code, based on their preferences.

## Project Structure

- `password_generators.py`: A Python module containing the password generators classed:
    - `PinGenerator`
    - `RandomPasswordGenerator`
    - `MemorablePasswordGenerator`
- `main.py`: A Python script using Streamlit to create a web app for the password generators.
  

## Getting Started
__Prerequisites__ :

    - Python 3.7+
    - Streamlit
    - NLTK
  
  To install NLTK:
  ` pip install nltk`

  After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:
  ```
  import nltk
  nltk.download('word')
  ```
  Then install Streamlit:
  ```
  pip install streamlit
  ```
 Or: 
``` 
pip install -r requirements.txt
```
## Usage
After following the installation steps, you can run the Streamlit we app as follows:
```
streamlit run main.pu
````
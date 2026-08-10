# Gender and Race Prediction

A Python project that uses **Streamlit**, **DeepFace**, and **Names Dataset** to predict demographic attributes from either a person's name or an uploaded image.

## Features

- Predict sex from a given name.
- Identify the most associated country for a given name.
- Display the country's flag.
- Analyze an uploaded face image using DeepFace.
- Predict gender and race from an image.
- Simple interactive Streamlit interface.



## Project Structure

```text
sex_and_race_prediction/
├── src/
│   ├── app.py
│   ├── image_predictor.py
│   ├── name_predictor.py
│   ├── utils.py
│   └── test.ipynb
├── requirements.txt
└── README.md
````
## Usage

Install the dependencies:

```bash
pip install -r requirements.txt
```



Run the Streamlit application from the `src` directory:

```bash
cd src
streamlit run app.py
```


### 1. Name Prediction

Enter a name and the application uses `names-dataset` to retrieve information associated with that name, including:

* Predicted sex
* Most associated country
* Country flag

### 2. Image Prediction

Upload a `.jpg`, `.jpeg`, or `.png` image containing a face.

DeepFace analyzes the image and returns:

* Predicted gender
* Predicted race

The uploaded image is temporarily saved during analysis and removed afterward.


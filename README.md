# Project: Multiple-Disease-Predictor-ML-Flask-WebApp
### Project Intro/Objective 

It's an end-to-end Machine Learning Project. The purpose of this project is to predict whether a person is suffering from a particular disease or not on the basis of his/her input data. The prediction has been done by using Machine Learning (ML) classification algorithms and it has been deployed as a Flask web app on Heroku. Currently, this web app can predict 3 types of diseases (Diabetes, Parkinson's and Heart Disease). 

### See Project

Visit: https://multiple-disease-predictor-ml.herokuapp.com/

### Install

This project requires **Python** and the following Python libraries installed:

- NumPy
- Pandas
- matplotlib
- Seaborn
- scikit-learn
- Flask


### Screenshots

**Home Page**

![Home Page](https://user-images.githubusercontent.com/109678911/202175139-d1710976-f39b-461c-9def-e18611f2f3cf.PNG)


**Diabetes Prediction Page**

![Diabetes Prediction Page](https://user-images.githubusercontent.com/109678911/202175393-797bf0bb-ed0d-42ae-a872-69004e51c3d7.PNG)


### How this project has been created

**Step-1** : Build and trained ML models for each of the 3 diseases, whose code is written in the `diabetes.py`, `heart.py` and `parkinsons.py` files and saved the model in pickle file `diabetes.pkl`, `heart.pkl`, and `parkinsons.pkl` respectively.

**Step-2** : Created Flask web app whose code is written in `app.py` file. For the interactive user interface, HTML and CSS have been used. HTML files are stored in `templates` directory while CSS files and web app's background image is stored in `static` directory.

**Step-3** : Uploaded the project on GitHub and deployed the web app using Heroku.

### Procfile

Procfile is a mechanism for declaring the commands that are executed by an Heroku app on startup. So for this project, the Procfile contains ` web: gunicorn app:app` where the first app represents the name of the python file (`app.py`) that runs the whole application. The second app represents the app name (`app=Flask(__name__)`) that is named inside app.py file.

### Run

In a terminal or command window, navigate to the top-level project directory `Multiple-Disease-Predictor-ML-Flask-WebApp/` (that contains this README) and run the following command:

```bash
python app.py
```  

This will show you the localhost address, type the same address in the browser and it will open WebApp in your browser.

### Data

The datasets that are used for training the ML models are:

- **The diabetes dataset consists of 768 data points, with each datapoint having 8 features. This dataset is Pima Indians Diabetes Database found on the kaggle.**

**Features**
1. `Pregnancies`: Number of times pregnant
2. `Glucose`: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. `BloodPressure`: Diastolic blood pressure (mm Hg)
4. `SkinThickness`: Triceps skin fold thickness (mm)
5. `Insulin`: 2-Hour serum insulin (mu U/ml)
6. `BMI`: Body mass index (weight in kg/(height in m)^2)
7. `DiabetesPedigreeFunction`: Diabetes pedigree function
8. `Age`: Age (years)


**Target Variable**
9. `Outcome`: Class variable (0 or 1) 268 of 768 are 1, the others are 0

- **The heart dataset consists of 1025 data points, with each datapoint having 13 features. This dataset is Heart Disease Dataset found on the kaggle.**

**Features**
1. `age`: age in years
2. `sex`: (1 = male; 0 = female)
3. `cp`: chest pain type
4. `trestbps`: resting blood pressure (in mm Hg on admission to the hospital)
5. `chol`: serum cholestoral in mg/dl
6. `fbs`: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
7. `restecg`: resting electrocardiographic results
8. `thalach`: maximum heart rate achieved
9. `exang`: exercise induced angina (1 = yes; 0 = no)
10. `oldpeak`: ST depression induced by exercise relative to rest
11. `slope`: the slope of the peak exercise ST segment
12. `ca`: number of major vessels (0-3) colored by flourosopy 
13. `thal`: 0 = normal; 1 = fixed defect; 2 = reversable defect


**Target Variable**
14. `target`: Class variable (0 or 1) 526 of 1025 are 1, the others are 0. Value 0 = no heart disease and 1 = heart disease

- **The ParkinsonsDisease dataset consists of 195 data points, with each datapoint having 22 features. This dataset is Parkinsons Disease Dataset found on the kaggle.**

**Features**
1. `MDVP:Fo(Hz)`: Average vocal fundamental frequency
2. `MDVP:Fhi(Hz)`: Maximum vocal fundamental frequency
3. `MDVP:Flo(Hz)`: Minimum vocal fundamental frequency
4. `MDVP:Jitter(%)`
5. `MDVP:Jitter(Abs)`
6. `MDVP:RAP`
7. `MDVP:PPQ`
8. `Jitter:DDP`: Several measures of variation in fundamental frequency
9. `MDVP:Shimmer`
10. `MDVP:Shimmer(dB)`
11. `Shimmer:APQ3`
12. `Shimmer:APQ5`
13. `MDVP:APQ`
14. `Shimmer:DDA` :Several measures of variation in amplitude
15. `NHR`
16. `HNR`: Two measures of ratio of noise to tonal components in the voice
17. `RPDE`
18. `DFA`: Signal fractal scaling exponent
19. `spread1`
20. `spread2`
21. `PPE`: Three nonlinear measures of fundamental frequency variation
22. `D2`: Two nonlinear dynamical complexity measures


**Target Variable**
23. `status`: Class variable (0 or 1) 147 of 195 are 1, the others are 0. Value 1 - Parkinson's, 0 - healthy

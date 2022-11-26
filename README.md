# Project: Multiple-Disease-Predictor-ML-Flask-WebApp
### Project Intro/Objective 

It's an end-to-end Machine Learning Project. The purpose of this project is to predict whether a person is suffering from a particular disease or not on the basis of his/her input data. The prediction has been done by using Machine Learning (ML) classification algorithms and it has been deployed as a Flask web app on Heroku. Currently, this web app can predict 3 types of diseases (Diabetes, Parkinson's and Heart Disease). 

### See Project

Visit: https://multiple-disease-predictor-ml.herokuapp.com/  (This link might not work if the Heroku will discontinue its Free tier/plan, in that case, please scroll down and see how this deployed web app looks like on Heroku)


### Screenshots (of This Web App When it is Live On Heroku)

**Home Page**


![HomePage](https://user-images.githubusercontent.com/109678911/204099558-56535854-14dd-43c6-83f4-ba7ee329662d.PNG)


**Diabetes Prediction Page**

![DiabetesPredictionPage](https://user-images.githubusercontent.com/109678911/204099575-ea73c666-60a5-464f-8fee-ec4440a9674a.PNG)

**Diabetes Prediction Page With Inputs Provided by the User**

![DiabetesPredictionPageWithValues](https://user-images.githubusercontent.com/109678911/204099672-6693a3f3-de0c-4706-bb4b-cc12282866f2.PNG)

**Diabetes Prediction Page Displaying the Output for the Inputs Provided by the User**

![DiabetesPredictionPageOutput](https://user-images.githubusercontent.com/109678911/204099710-34179827-df57-48a2-96fa-883f2c82fba6.PNG)

**Parkinson's Prediction Page**

![ParkinsonsPredictionPage](https://user-images.githubusercontent.com/109678911/204099779-547b7a95-160d-45c7-b650-38abeb7cfd8d.PNG)

**Heart Disease Prediction Page**

![HeartDiseasePredictionPage](https://user-images.githubusercontent.com/109678911/204099841-0298aa88-9b1f-4d38-bf6e-14dd9527d9f6.PNG)

### Install

This project requires **Python** and the following Python libraries installed:

- NumPy
- Pandas
- matplotlib
- Seaborn
- scikit-learn
- Flask

### How this project has been created

**Step-1** : Build and trained ML models for each of the 3 diseases, whose code is written in the `diabetes.py`, `heart.py` and `parkinsons.py` files and saved the model in pickle file `diabetes.pkl`, `heart.pkl`, and `parkinsons.pkl` respectively.

**Step-2** : Created Flask web app whose code is written in `app.py` file. For the interactive user interface, HTML and CSS have been used. HTML files are stored in `templates` directory while CSS files and web app's background image is stored in `static` directory.

**Step-3** : Uploaded the project on GitHub and deployed the web app using Heroku.

### Procfile

Procfile is a mechanism for declaring the commands that are executed by an Heroku app on startup. So for this project, the Procfile contains ` web: gunicorn app:app` where the first app represents the name of the python file (`app.py`) that runs the whole application. The second app represents the app name (`app=Flask(__name__)`) that is named inside app.py file.

### Deployment on Heroku With Screenshots

**Step-1** : Login to Heroku, then Create the new app.

![Createapp](https://user-images.githubusercontent.com/109678911/204100024-e9c2b32d-46a8-4858-b0c3-1d428323bbe7.PNG)

**Step-2** : Connect to the GitHub and then Connect to the Repository `sidroy9/Multiple-Disease-Predictor-ML-Flask-WebApp` where this project exists.

![Deployment](https://user-images.githubusercontent.com/109678911/204100265-8d0ce13f-cea2-4c2c-87a5-db7e3e05e422.PNG)

**Step-3** : Go to Manual Deploy Section, then choose the main branch to deploy and then click on the Deploy Branch. Now, Build main will start.

![Manual Deploy](https://user-images.githubusercontent.com/109678911/204100750-e803df4f-c8b7-4b33-987a-e56d1c14b733.jpg)


**Step-4** : After sometime, the app will be deployed successfully. You can click on View to see the live web app. 

![Deployed](https://user-images.githubusercontent.com/109678911/204101351-721158a6-3e81-4893-844b-8f03329b2e5e.jpg)



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

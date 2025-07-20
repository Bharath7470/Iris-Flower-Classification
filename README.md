# 🌸 Iris Flower Classification using Machine Learning

This project focuses on classifying iris flowers into three species—Setosa, Versicolor, and Virginica—based on sepal and petal measurements. The project includes training a machine learning model and building an interactive web app for real-time predictions.

## 📌 Project Overview

- **Student Name:** Bharath  
- **Semester:** 5th Semester B.Tech  
- **Internship Track:** Machine Learning – Elevate Labs  
- **Model Used:** Logistic Regression  
- **UI Framework:** Streamlit

## 🧰 Tools and Technologies Used

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Joblib  
- Streamlit

## 📂 Files Included

| File                             | Description                                 |
|----------------------------------|---------------------------------------------|
| `Iris_Flower_Classification.ipynb` | ML model training and evaluation notebook |
| `iris_model.pkl`                | Saved Logistic Regression model             |
| `app.py`                        | Streamlit UI script                         |
| `Iris_Classification_Report.docx` or `.pdf` | Final internship report        |
| `README.md`                     | Project overview and instructions           |

## 🚀 Project Workflow Summary

- The dataset is loaded from Scikit-learn’s built-in Iris dataset.  
- A DataFrame is created and visualized using pairplots and heatmaps.  
- A Logistic Regression model is trained to classify flower species based on 4 features:  
  - Sepal Length  
  - Sepal Width  
  - Petal Length  
  - Petal Width  
- The model is evaluated using accuracy and classification report.  
- It is saved as `iris_model.pkl` using Joblib.  
- A Streamlit app (`app.py`) is created to allow users to input values and get predictions instantly.

## 🌐 How to Use the Web App

1. Install Streamlit (if not already installed):  
   `pip install streamlit`

2. Navigate to the project folder:  
   `cd "Iris Flower Classifier"`

3. Run the app:  
   `streamlit run app.py`

4. A browser window will open where you can input flower measurements and get predictions.

## 📊 Sample Prediction

**Input:**  
- Sepal Length: 5.1  
- Sepal Width: 3.5  
- Petal Length: 1.4  
- Petal Width: 0.2

**Output:**  
🌼 Predicted Iris Species: **Setosa**

## 🎓 Learning Outcomes

- Data handling and visualization with Pandas & Seaborn  
- Model training and testing with Scikit-learn  
- Saving and reloading ML models using Joblib  
- Web UI development with Streamlit  
- Real-world deployment workflow understanding

## 👨‍💻 Author

**Bharath**  
5th Semester B.Tech  
Internship Project – Elevate Labs (Machine Learning Track)

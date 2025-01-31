# Heart Disease Prediction

This project predicts whether a person has heart disease or not based on various medical parameters. The dataset used contains multiple features like age, cholesterol level, resting blood pressure, maximum heart rate achieved, and other relevant features. Three machine learning models are applied to solve the problem: Logistic Regression, Random Forest, and Support Vector Machine.

## Files in this repository:
1. **project_report.pdf** - A detailed project report with analysis and findings.
2. **predict_heart_disease.py** - Python code for training and predicting heart disease using various machine learning algorithms.
3. **README.md** - Project overview and setup instructions.

## How to run this project:
1. Clone the repository or download the files to your local system.
2. Ensure you have **Python 3.x** installed.
3. Install the necessary libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```
4. Run the `heart_disease_model.py` file to train the models and make predictions.
    ```
    python heart_disease_model.py
    ```

## Dependencies:
- **pandas** - For data manipulation and analysis.
- **numpy** - For numerical computations.
- **matplotlib** & **seaborn** - For data visualization.
- **scikit-learn** - For machine learning algorithms and tools.

## Project Steps:
1. Data is loaded from a CSV file and explored using various summary statistics and visualizations.
2. Data is preprocessed with scaling for numeric features and one-hot encoding for categorical features.
3. Three machine learning models (Logistic Regression, Random Forest, and SVM) are trained and evaluated.
4. The performance of the models is assessed using classification reports, accuracy scores, and confusion matrices.

## License:
This project is licensed under the MIT License.


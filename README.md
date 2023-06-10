# Data_science_salary_pred_proj
This model predicts the salary of Data scientist and other similar jobs such as MLE, Data Engineer, Research scientist of US.

### Skills Used in this project
1. Machine Learning
2. Python
3. Web Scrapping
4. Statistics

Steps involving in building a salary prediction model for Data Science jobs using web scraping and machine learning algorithms:

### Data Collection: 
Scrape the job postings and salary information from Glassdoor or any other job search website. Uses web scraping libraries like Selenium to extract the relevant data such as job title, company, location, salary, and other features.

### Data Cleaning: 
Clean the collected data to remove any irrelevant or incomplete entries. Perform tasks like handling missing values, standardizing the text, and converting salary values into a consistent format. You may need to use techniques like regular expressions and data manipulation libraries such as pandas for this step.

### Feature Engineering: 
Extract meaningful features from the collected data that can help in predicting the salary. This can include features like job title, company size, location, industry, years of experience, and education level. Additionally, you may need to preprocess the text features by converting them into numerical representations using techniques like one-hot encoding or word embeddings.

### Data Exploration and Visualization: 
Perform exploratory data analysis (EDA) to gain insights into the data and identify any patterns or relationships. Visualize the data using libraries like matplotlib or seaborn to understand the distribution of variables and their impact on the target variable (salary).

### Model Building: 
Select suitable machine learning algorithms to train the salary prediction model. Some commonly used algorithms for regression tasks include random forest, support vector machines (SVM), and multiple linear regression. Consider using libraries like scikit-learn to implement these algorithms.

### Model Evaluation and Selection: 
Evaluate the trained models using appropriate evaluation metrics such as mean absolute error (MAE), mean squared error (MSE), or R-squared. Compare the performance of different models and select the one that provides the best accuracy and generalization.

### Hyperparameter Tuning: 
Optimize the model's performance by tuning the hyperparameters. Use techniques like grid search or random search to find the best combination of hyperparameters for the selected algorithms. This can be done using tools like GridSearchCV from scikit-learn.

Note that the model deployement part is not done in this.

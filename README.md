# Welcome to the repository of Credit-Risk-Assessment

This project is about development of predictive model to classify bank clients as default or non-default based on their payment behaviors on their credit obligations.

This data was taken from Google BigQuery Public Dataset with table name credit_card_default, where it can be accessed through this link:
https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

To see the final result of this project (a web app on Hugging Face), you can find it on the link below:
https://huggingface.co/spaces/catherinehelenna/Credit-Risk-Assessment

----------------------------------------------------------------------------------------------------------
### Background of the project

Founded in 2003, CreditGuide was a startup company partnering with financial institutions to detect the defaulters or bad customers who cannot fulfil their credit obligations. CreditGuide proposed the prototype predictive model to classify potential defaulters on October 2005 based on their credit payment pattern to a local bank by taking clients' data from April to September 2005. This program was the first prototype CreditGuide developed which lead CreditGuide into promising partnerships in the future.

----------------------------------------------------------------------------------------------------------
### Problem Statement

The ultimate goal is to classify potential defaulters on October 2005 so that the local bank can adjust some measures to prevent them from defaulting.

----------------------------------------------------------------------------------------------------------
### What can you find in this project?

Query to fetch data from BigQuery, exploratory data analysis, classification model building process with improvement (hyperparameter tuning), as well as the deployment folder to make the web app.

### Some notes about the model

- Among all the classification algorithms used, the logistic regression model has the best performance.
- Evaluation Metrics => F1-score: 54% and AUC: 0.78.

----------------------------------------------------------------------------------------------------------
Please do let me know if you have feedbacks or improvements for this project by reaching through catherinehelenna888@gmail.com

Thank you for reading!!






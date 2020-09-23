# Disaster Response Pipeline Project

### Motivation
This project aims to apply data ETL pipelines and machine learning pipelines with natural language processing to complete disaster response message classification.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Notes:
1. The model pkl file is not included because the file size is around 193 MB (GitHub has limit of 100 MB on file size), but it should be fine to generate on local machine.
2. Python 3.6 is used to match Udacity's Web API
3. Reported accuracy of trained model is included in [accuracy.txt](https://github.com/xixiaodong/DisasterResponse/blob/master/accuracy.txt).

Here are the plots:
![plots](https://github.com/xixiaodong/DisasterResponse/blob/master/DisasterPlots.png)

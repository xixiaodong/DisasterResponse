# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

Category: offer 
              precision    recall  f1-score   support

          0       1.00      1.00      1.00      5222
          1       0.00      0.00      0.00        22

avg / total       0.99      1.00      0.99      5244

Accuracy of                     offer: 1.00
Category: aid_related 
              precision    recall  f1-score   support

          0       0.76      0.86      0.81      3082
          1       0.75      0.62      0.68      2162

avg / total       0.76      0.76      0.75      5244

Accuracy of               aid_related: 0.76
Category: medical_help 
              precision    recall  f1-score   support

          0       0.92      1.00      0.96      4817
          1       0.58      0.06      0.11       427

avg / total       0.89      0.92      0.89      5244

Accuracy of              medical_help: 0.92
Category: medical_products 
              precision    recall  f1-score   support

          0       0.95      1.00      0.97      4968
          1       0.74      0.09      0.16       276

avg / total       0.94      0.95      0.93      5244

Accuracy of          medical_products: 0.95
Category: search_and_rescue 
              precision    recall  f1-score   support

          0       0.98      1.00      0.99      5117
          1       0.89      0.06      0.12       127

avg / total       0.98      0.98      0.97      5244

Accuracy of         search_and_rescue: 0.98
Category: security 
              precision    recall  f1-score   support

          0       0.98      1.00      0.99      5157
          1       0.00      0.00      0.00        87

avg / total       0.97      0.98      0.97      5244

Accuracy of                  security: 0.98
Category: military 
              precision    recall  f1-score   support

          0       0.97      1.00      0.98      5058
          1       0.60      0.08      0.14       186

avg / total       0.95      0.97      0.95      5244

Accuracy of                  military: 0.97
Category: child_alone 
              precision    recall  f1-score   support

          0       1.00      1.00      1.00      5244

avg / total       1.00      1.00      1.00      5244

Accuracy of               child_alone: 1.00
Category: water 
              precision    recall  f1-score   support

          0       0.96      1.00      0.98      4908
          1       0.88      0.35      0.50       336

avg / total       0.95      0.96      0.95      5244

Accuracy of                     water: 0.96
Category: food 
              precision    recall  f1-score   support

          0       0.94      0.99      0.96      4652
          1       0.84      0.53      0.65       592

avg / total       0.93      0.94      0.93      5244

Accuracy of                      food: 0.94
Category: shelter 
              precision    recall  f1-score   support

          0       0.94      0.99      0.96      4780
          1       0.81      0.31      0.45       464

avg / total       0.93      0.93      0.92      5244

Accuracy of                   shelter: 0.93
Category: clothing 
              precision    recall  f1-score   support

          0       0.99      1.00      0.99      5164
          1       0.89      0.10      0.18        80

avg / total       0.98      0.99      0.98      5244

Accuracy of                  clothing: 0.99
Category: money 
              precision    recall  f1-score   support

          0       0.98      1.00      0.99      5128
          1       0.60      0.03      0.05       116

avg / total       0.97      0.98      0.97      5244

Accuracy of                     money: 0.98
Category: missing_people 
              precision    recall  f1-score   support

          0       0.99      1.00      0.99      5182
          1       0.00      0.00      0.00        62

avg / total       0.98      0.99      0.98      5244

Accuracy of            missing_people: 0.99
Category: refugees 
              precision    recall  f1-score   support

          0       0.97      1.00      0.98      5078
          1       0.50      0.01      0.01       166

avg / total       0.95      0.97      0.95      5244

Accuracy of                  refugees: 0.97
Category: death 
              precision    recall  f1-score   support

          0       0.96      1.00      0.98      5015
          1       0.86      0.10      0.19       229

avg / total       0.96      0.96      0.94      5244

Accuracy of                     death: 0.96
Category: other_aid 
              precision    recall  f1-score   support

          0       0.87      1.00      0.93      4549
          1       0.57      0.04      0.07       695

avg / total       0.83      0.87      0.82      5244

Accuracy of                 other_aid: 0.87
Category: infrastructure_related 
              precision    recall  f1-score   support

          0       0.93      1.00      0.97      4896
          1       0.33      0.00      0.01       348

avg / total       0.89      0.93      0.90      5244

Accuracy of    infrastructure_related: 0.93
Category: transport 
              precision    recall  f1-score   support

          0       0.96      1.00      0.98      5016
          1       0.76      0.07      0.13       228

avg / total       0.95      0.96      0.94      5244

Accuracy of                 transport: 0.96
Category: buildings 
              precision    recall  f1-score   support

          0       0.95      1.00      0.98      4981
          1       0.80      0.11      0.19       263

avg / total       0.95      0.95      0.94      5244

Accuracy of                 buildings: 0.95
Category: electricity 
              precision    recall  f1-score   support

          0       0.98      1.00      0.99      5136
          1       0.50      0.03      0.05       108

avg / total       0.97      0.98      0.97      5244

Accuracy of               electricity: 0.98
Category: tools 
              precision    recall  f1-score   support

          0       0.99      1.00      1.00      5211
          1       0.00      0.00      0.00        33

avg / total       0.99      0.99      0.99      5244

Accuracy of                     tools: 0.99
Category: hospitals 
              precision    recall  f1-score   support

          0       0.99      1.00      0.99      5188
          1       0.00      0.00      0.00        56

avg / total       0.98      0.99      0.98      5244

Accuracy of                 hospitals: 0.99
Category: shops 
              precision    recall  f1-score   support

          0       1.00      1.00      1.00      5224
          1       0.00      0.00      0.00        20

avg / total       0.99      1.00      0.99      5244

Accuracy of                     shops: 1.00
Category: aid_centers 
              precision    recall  f1-score   support

          0       0.99      1.00      0.99      5181
          1       0.00      0.00      0.00        63

avg / total       0.98      0.99      0.98      5244

Accuracy of               aid_centers: 0.99
Category: other_infrastructure 
              precision    recall  f1-score   support

          0       0.96      1.00      0.98      5010
          1       0.00      0.00      0.00       234

avg / total       0.91      0.95      0.93      5244

Accuracy of      other_infrastructure: 0.95
Category: weather_related 
              precision    recall  f1-score   support

          0       0.87      0.95      0.91      3791
          1       0.84      0.63      0.72      1453

avg / total       0.86      0.86      0.86      5244

Accuracy of           weather_related: 0.86
Category: floods 
              precision    recall  f1-score   support

          0       0.95      1.00      0.97      4823
          1       0.89      0.42      0.57       421

avg / total       0.95      0.95      0.94      5244

Accuracy of                    floods: 0.95
Category: storm 
              precision    recall  f1-score   support

          0       0.94      0.99      0.97      4767
          1       0.78      0.42      0.54       477

avg / total       0.93      0.94      0.93      5244

Accuracy of                     storm: 0.94
Category: fire 
              precision    recall  f1-score   support

          0       0.99      1.00      0.99      5188
          1       0.00      0.00      0.00        56

avg / total       0.98      0.99      0.98      5244

Accuracy of                      fire: 0.99
Category: earthquake 
              precision    recall  f1-score   support

          0       0.97      0.99      0.98      4746
          1       0.90      0.74      0.81       498

avg / total       0.97      0.97      0.97      5244

Accuracy of                earthquake: 0.97
Category: cold 
              precision    recall  f1-score   support

          0       0.98      1.00      0.99      5136
          1       0.89      0.07      0.14       108

avg / total       0.98      0.98      0.97      5244

Accuracy of                      cold: 0.98
Category: other_weather 
              precision    recall  f1-score   support

          0       0.95      1.00      0.97      4960
          1       0.38      0.02      0.03       284

avg / total       0.92      0.95      0.92      5244

Accuracy of             other_weather: 0.95
Category: direct_report 
              precision    recall  f1-score   support

          0       0.86      0.98      0.92      4251
          1       0.78      0.32      0.46       993

avg / total       0.85      0.85      0.83      5244

Accuracy of             direct_report: 0.85

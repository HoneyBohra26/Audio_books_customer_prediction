In the process of developing a predictive model for audiobook purchase behavior, I undertook several key steps across different notebooks and files.

**Data Preprocessing:**
In the **audiobook_data_preprocessing.ipynb** notebook, I focused on preparing the dataset for modeling. This involved addressing class imbalance by balancing the dataset to ensure that both classes (repeat purchase and no repeat purchase) were adequately represented. Additionally, I performed essential preprocessing steps such scaling numerical features to ensure the data was ready for training the model.

**Model Development:**
In the **dl_audiobook_model.ipynb** notebook, I designed and trained a deep learning model to predict whether a customer would make a repeat purchase from the audiobook company. I carefully outlined the architecture of the neural network, selecting appropriate layers, activation functions, and optimization parameters based on experimentation and model performance metrics. After defining the model, I trained it using the preprocessed data, optimizing its parameters through iterative training cycles to achieve optimal predictive accuracy.

**Dataset Description:**
The **Audiobooks_data.csv** file served as the primary dataset for training the model. To maintain data integrity during training, this file was deliberately structured without column headers, with the respective column names provided separately in **column_names_audiobooks.txt**. This dataset encompassed two years of customer engagement data, with an additional six months specifically collected to construct the target variable ('Targets'), which indicates whether a customer made a repeat purchase.

**Predictive Analysis and Deployment:**
For predicting on new data, I utilized the **New_Audiobooks_Data.csv** file. The **dl_predictingNewData.ipynb** notebook details the process of preprocessing entirely new data to align with the model's requirements and making predictions using the trained deep learning model. This involved applying the same preprocessing steps as used during model training to ensure consistency and reliability in prediction outcomes.

**Web Application Development:**
In **app.py**, I implemented a Flask web application to operationalize the predictive model. The application loads a previously saved scaler and the trained deep learning model. It accepts uploaded CSV files containing new data for prediction, processes these files to extract relevant features, scales them using the loaded scaler, and utilizes the model to predict whether customers will make repeat purchases. Results are then displayed on an HTML page (**index.html**), which is designed to showcase prediction outcomes in a user-friendly format.


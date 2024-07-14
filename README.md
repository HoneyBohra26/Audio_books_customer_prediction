In the "audiobook_data_preprocessing.ipynb" notebook, I conducted data preprocessing tasks including dataset balancing and general data preparation.

In "dl_audiobook_model.ipynb", I designed and trained a deep learning model to predict repeat audiobook purchases. This involved defining the model architecture and performing training and testing procedures.

The "Audiobooks_data.csv" file, utilized for model training, lacks column headers to avoid text interference during training. Column names are detailed in "column_names_audiobooks.txt", with data spanning two years plus an additional six months used to establish the 'Targets' column for purchase prediction.

For predicting outcomes, "New_Audiobooks_Data.csv" is employed in "dl_predictingNewData.ipynb". This notebook outlines how to preprocess new data and execute predictions using the trained model.

In "app.py", a Flask-based web application was created to forecast audiobook purchase behavior. The app loads a scaler and the trained model, processes uploaded CSV files to generate predictions, scales data, and displays results on an HTML page. The corresponding HTML code is housed in "index.html".

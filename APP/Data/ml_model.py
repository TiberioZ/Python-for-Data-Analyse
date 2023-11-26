import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



class MachineLearning():

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.X = self.df.drop(self.df.columns[12:31], axis=1)
        self.models = self.train_models()

    def train_models(self):
        models = []
        drug_columns = self.df.columns[12:31]

        for drug_name in drug_columns:
            X = self.X
            y = self.df[drug_name]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LogisticRegression()

            # Train the model
            model.fit(X_train, y_train)
            models.append(model)

        return models

    def prediction_drug_consumption(self, user_data: pd.DataFrame, model: LogisticRegression):
        y_pred = model.predict(user_data)
        return y_pred
    
    def prediction_drugs(self, user_data: pd.DataFrame):
        predictions = [[]]
        columns_name = [
        'Alcohol', 
        'Amphet', 
        'Amyl', 
        'Benzos', 
        'Caffeine', 
        'Cannabis', 
        'Chocolate',
        'Coke',
        'Crack',
        'Ecstasy',
        'Heroin',
        'Ketamine',
        'Legalh',
        'LSD',
        'Meth',
        'Mushrooms',
        'Nicotine',
        'Semer',
        'VSA'
        ]

        for model in self.models:
            prediction = self.prediction_drug_consumption(user_data, model)
            predictions[0].append(prediction)

        result_df = pd.DataFrame(predictions, columns=columns_name)

        return result_df
    

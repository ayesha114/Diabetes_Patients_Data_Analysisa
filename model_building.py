from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_and_predict(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return y_test, y_pred

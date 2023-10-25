from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

def evaluate(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
    values = [accuracy, precision, recall, f1]

    # Visualization of metrics
    plt.bar(metrics, values, color=['blue', 'green', 'red', 'purple'])
    plt.ylabel('Score')
    plt.title('Model Evaluation Metrics')
    for i, v in enumerate(values):
        plt.text(i, v + 0.01, "{:.2f}".format(v), ha='center', va='bottom', fontsize=10)
    plt.ylim([0, 1.1])
    plt.show()

    return accuracy, precision, recall, f1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
def preprocess_data(filename):
    df = pd.read_csv(filename)
    # Filter out records where Age < 21
    df = df[df['Age'] >= 21]
    return df

# Show histograms for each feature
def plot_histograms(df):
    df.drop('Outcome', axis=1).hist(figsize=(12, 10))
    plt.suptitle('Distribution of Diagnostic Measurements')
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.show()

# Show boxplots for each feature vs. Outcome
def plot_boxplots(df):
    features = df.columns[:-1]
    for feature in features:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Outcome', y=feature, data=df)
        plt.title(f'{feature} vs. Outcome')
        plt.show()

# Show scatter plots for pairs of features
def plot_scatterplots(df):
    sns.pairplot(df, hue='Outcome', diag_kind='kde')
    plt.show()

def main():
    df = preprocess_data('diabetes.csv')
    plot_histograms(df)
    plot_boxplots(df)
    plot_scatterplots(df)

if __name__ == '__main__':
    main()

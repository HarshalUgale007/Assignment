import pandas as pd
import matplotlib.pyplot as plt


def read_data(test_file, label_file):
    test_data = pd.read_csv(test_file)
    label_data = pd.read_csv(label_file)
    return test_data, label_data


def plot_time_series(test_data, label_data):
    plt.figure(figsize=(12, 6))
    plt.plot(test_data['Time'], test_data['Value'], label='Time Series Data')
    for i, row in label_data.iterrows():
        plt.axvspan(row['start_time'], row['end_time'], color='red', alpha=0.3, label='Anomaly Region')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Time Series Data with Anomaly Regions')
    plt.legend()
    plt.show()


def perform_eda(test_data):
    eda_results = {}
    return eda_results


def find_root_cause(eda_results):
    root_cause = []
    return root_cause


test_file = 'files/files/test.csv'
label_file = 'files/files/test_label.csv'

print(f"Processing {test_file} and {label_file}")
test_data, label_data = read_data(test_file, label_file)
print(test_data.columns)
plot_time_series(test_data, label_data)
eda_results = perform_eda(test_data)
root_cause = find_root_cause(eda_results)
print("Root cause of anomaly:", root_cause)

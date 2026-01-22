import matplotlib.pyplot as plt
import seaborn as sns

def plot_yearly_sales(series):
    plt.figure(figsize=(10,5))
    plt.plot(series.index, series.values, marker='o')
    plt.title("Sales Per Year")
    plt.grid(True)
    plt.show()

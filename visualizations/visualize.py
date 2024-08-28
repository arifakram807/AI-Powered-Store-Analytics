import matplotlib.pyplot as plt
import pandas as pd

def create_plot(data, x_column, y_column):
    # Convert x_column to string if it's categorical
    data[x_column] = data[x_column].astype(str)

    # Ensure y_column is numeric
    data[y_column] = pd.to_numeric(data[y_column], errors='coerce')

    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column])
    plt.title(f'{y_column} over {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.savefig("static/plot.png")
    plt.show()

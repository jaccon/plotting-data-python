# KVus Gauge Visualization

This project displays a gauge chart that visualizes the amount of KVus (a fictional unit) over a period of time. The data is read from a CSV file, and the gauge chart is created using the Plotly library with annotations for each data point. 

Before running this project, make sure you have Python 3 installed on your machine along with the required libraries. You can verify if Python is installed by running the following command in your terminal: `python --version`. If Python is not installed, you can download it [here](https://www.python.org/downloads/). 

To get started, clone the repository using `git clone https://github.com/your-username/your-repository.git` and navigate to the project directory with `cd your-repository`. To avoid dependency conflicts, it’s recommended to create a virtual environment: `python -m venv venv` and activate it using `source venv/bin/activate` (on Windows use `venv\Scripts\activate`). Install the necessary libraries using pip: `pip install pandas plotly matplotlib`. 

Ensure you have a CSV file named `dados.csv` in the `data` directory, formatted with the appropriate columns for `Data` and `Kvus`. Finally, execute the Python script to generate the gauge chart with `python your_script.py` (replace `your_script.py` with the name of your Python script). The gauge chart will be displayed in your web browser. 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

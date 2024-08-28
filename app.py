from flask import Flask, render_template, request
from data_ingestion.ingest import load_csv
from data_analysis.analysis import generate_insights
from reports.generate_report import create_report
from visualizations.visualize import create_plot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = load_csv(file)
    data_summary = df.describe().to_string()
    report = create_report(data_summary)
    create_plot(df, df.columns[0], df.columns[1])
    return render_template('report.html', report=report, plot_url='static/plot.png')

if __name__ == "__main__":
    app.run(debug=True)

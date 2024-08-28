from data_analysis.analysis import generate_insights

def create_report(data_summary):
    # Generate insights using the OpenAI API
    insights = generate_insights(data_summary)

    # Create a report combining the data summary and insights
    report = f"Data Summary:\n{data_summary}\n\nInsights:\n{insights}"

    # Save the report to a file (optional)
    with open("static/report.txt", "w") as file:
        file.write(report)

    return report

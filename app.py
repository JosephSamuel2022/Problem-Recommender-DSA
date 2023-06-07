import base64
import io
from flask import Flask, render_template, request
import user_data_recommendation
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use('Agg')

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html')


@app.route('/visualizations')
def visualizations():
    df = pd.read_csv('problem_sets_data.csv')
    # Plot a histogram of the 'rating' column
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'], bins=10)
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of Ratings')
    rating_hist = get_plot_data(plt)
    plt.close()

  # Code for visualization 2: Pie chart of top 10 most common tags
    top_tags = df['tags'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    plt.pie(top_tags.values, labels=top_tags.index, autopct='%1.1f%%')
    plt.title('Top 10 Most Common Tags')
    plt.axis('equal')  # Ensures the pie chart is circular
    top_tags_pie_chart = get_plot_data(plt)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.scatter(df['rating'], df['solvedCount'])
    plt.xlabel('Rating')
    plt.ylabel('Solved Count')
    plt.title('Rating vs. Solved Count')
    rating_solved_count = get_plot_data(plt)
    plt.close()

    plt.figure(figsize=(10, 6))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    corr_heatmap = get_plot_data(plt)
    plt.close()

    plt.figure(figsize=(10, 6))
    contest_counts = df['contestId'].value_counts()
    plt.bar(contest_counts.index, contest_counts.values)
    plt.xlabel('Contest ID')
    plt.ylabel('Count')
    plt.title('Distribution of Contest IDs')
    plt.xticks(rotation=90)
    contest_id_distribution = get_plot_data(plt)
    plt.close()

    return render_template('visualizations.html', rating_hist=rating_hist, top_tags_bar_chart=top_tags_pie_chart, rating_solved_count=rating_solved_count, corr_heatmap=corr_heatmap, contest_id_distribution=contest_id_distribution)


def get_plot_data(plt):
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plot_data = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    return plot_data


@app.route('/recommend', methods=['POST'])
def recommend():
    if not request.form.get('userhandle'):
        return "type a userhandle"
    handle = request.form.get('userhandle')
    s_data, w_data = user_data_recommendation.user_dataframe(handle)
    s, w = user_data_recommendation.problems_recommended(s_data, w_data)
    return render_template('success.html',  tables=[s.to_html(classes='data', header="true", render_links=True, escape=False)], titles=s.columns.values, wtables=[w.to_html(classes='data', header="true", render_links=True, escape=False)], wtitles=w.columns.values)


if __name__ == '__main__':
    app.run(debug=True)

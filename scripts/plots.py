import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_country_cases(df, country):
    cdf = df[df['location'] == country]
    plt.figure(figsize=(10,5))
    sns.lineplot(data=cdf, x='date', y='new_cases')
    plt.title(f'Daily New Cases - {country}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_global_heatmap(df):
    latest = df[df['date'] == df['date'].max()]
    fig = px.choropleth(latest, locations='iso_code', color='total_cases_per_million',
                        hover_name='location', title='Total Cases per Million (Latest)')
    fig.show()

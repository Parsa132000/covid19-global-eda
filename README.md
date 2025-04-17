# covid19-global-eda
# 🌍 COVID-19 Global EDA Dashboard

An interactive and lightweight Exploratory Data Analysis (EDA) project that analyzes the spread, impact, and vaccination trends of COVID-19 worldwide using real-time data from [Our World in Data](https://ourworldindata.org/coronavirus).

This project is built entirely in Python using tools like `pandas`, `matplotlib`, `seaborn`, `plotly`, and `scikit-learn`. It is designed to work with low storage environments (Google Colab or lightweight local setup).

---

## ✨ Features

- 📊 Time-series analysis of daily cases, deaths, and vaccinations by country
- 🧪 Correlation analysis between vaccination rate and drop in daily cases
- 🔮 7-day case prediction using linear regression for selected countries
- 🗺️ Interactive global heatmap using Plotly
- 📈 Visualization with `matplotlib`, `seaborn`, and `plotly`
- 📎 Deployable via Streamlit or exportable as PDF
- 💾 Minimal storage usage: works in Google Colab or Kaggle without downloads

---

## 📁 Project Structure

covid19-global-eda/
├── covid19-global-eda.ipynb    # Main Colab notebook for COVID-19 analysis
├── scripts/                     # Python helper scripts (loading, plotting, predicting)                    
├── requirements.txt             # Python dependencies for local or Streamlit use
├── LICENSE                      # MIT License
└── README.md                    # Project overview and documentation



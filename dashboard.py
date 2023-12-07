# dashboard.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from io import BytesIO

def dashboard_page():
    from main import budget, revenue,data

    st.markdown(
        """
        <style>
            body {
                border: 5px solid #C61A27;
                padding: 20px;
                width:100px;
                height:200px
            }
            .dashboard-content {
                border: 5px solid #C61A27;
                padding: 20px;
                width: 50%;
                height: auto;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .container {
                max-width: 70%;
                margin: auto;
            }
            .stPlot {
                max-width: 50%;  /* Ajustez la largeur du graphique en pourcentage */
                margin: auto;
            }
            img{
                width:40px;
                height:500px
            }
        </style>
        <div class="container"> 
            <div style="height: 15vh;">
                <h1 style="text-align: center;">Dashboard Content 📊</h1>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
 
    # Créez le graphique de dispersion
    st.markdown("## Scatter plot (Graphique de dispersion):")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.scatterplot(x=budget, y=revenue)
    ax.set_xlabel("Budget")
    ax.set_ylabel("Revenue")
    ax.set_title("Budget vs Revenue")
    ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)

    # Afficher le graphe de corrélation
    st.markdown("## Correlation Matrix:")
    numeric_data = data.select_dtypes(include='number').dropna() 
    correlations = numeric_data.corr(method='pearson')
    f, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(correlations, annot=True)
    st.pyplot(f)

    # Afficher la paire de graphiques avec Seaborn
    st.markdown("## Pair Plot:")
    pair_plot = sns.pairplot(data)
    st.pyplot(pair_plot)

    # image_stream = BytesIO()
    # plt.savefig(image_stream, format='png')

    # st.image(image_stream, width=400, height=200)
    # st.markdown(f'<img src="data:image/png;base64,{image_stream.getvalue().decode()}" alt="graphique" width="400" height="200">', unsafe_allow_html=True)
    # st.markdown(f'<div class="stPlot">{fig}</div>', unsafe_allow_html=True)

    # if st.button("Retour à la page précédente"):
    #     # Modifier l'URL pour retourner à app.py
    #     st.experimental_set_query_params(dashboard=False)

    # st.markdown("[Retour à la page précédente](<URL_APP.PY>)")
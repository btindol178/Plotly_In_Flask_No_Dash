from flask import Flask, render_template,request
import pandas as pd
import json
import plotly
import plotly.express as px


app = Flask(__name__)

df_scatter = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
    
  
@app.route('/',methods=['post', 'get'])
def index():
    # Graph Zero
    fig0 = px.bar(df_scatter, x='Fruit', y='Amount', color='City',barmode='group')
    graph0JSON = json.dumps(fig0, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph One
    fig1 = px.bar(df_scatter, x='Fruit', y='Amount', color='City',barmode='group')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph two
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species',  title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    if request.method == 'POST':
        projectpath = request.form['fruits']
        print(projectpath)
        df2 = df_scatter[df_scatter['Fruit'] != projectpath]
        fig0 = px.bar(df2, x='Fruit', y='Amount', color='City',barmode='group')
        fig1 = px.bar(df2, x='Fruit', y='Amount', color='City',barmode='group')

        graph0JSON = json.dumps(fig0, cls=plotly.utils.PlotlyJSONEncoder)
        graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
        #return render_template('indexer2.html',graph0JSON=graph0JSON,graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON)

    return render_template('indexer2.html',graph0JSON=graph0JSON,graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON)

if __name__ == '__main__':
    app.run()
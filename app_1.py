from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
#simulates two different dash apps
#requests pathname prefix tells the dash renderer where to look and request data

#dummy app 1
app1 = Dash(__name__,
			requests_pathname_prefix='/app1/')

app1.layout = html.Div([
	html.H1('App 1'),
	dcc.Graph(id='id',
			figure=fig)]
	)

if __name__ == '__main__':
	app1.run_server(debug=True)
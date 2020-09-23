from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({'Tako':[1, 2], 
					'Cats':[3,4]})

#simulates two different dash apps
#requests pathname prefix tells the dash renderer where to look and request data

#dummy app 1
app1 = Dash(__name__,
			requests_pathname_prefix='/app1/')

app1.layout = html.Div([
	html.H1('App 1'),
	dcc.Graph(id='id',
			figure=px.scatter(df, 'Tako', 'Cats'))]
	)


#dummy app 2
app2 = Dash(__name__,
			requests_pathname_prefix='/app2/')


app2.layout = html.Div([
	html.H1('App 2'),
	dcc.Graph(id='id',
			figure=px.scatter(df, 'Tako', 'Cats'))]
	)
	
if __name__ == '__main__':
	app2.run_server(debug=True)
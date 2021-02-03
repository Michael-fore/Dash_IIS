from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px

#simulates two different dash apps
#requests pathname prefix tells the dash renderer where to look and request data

#dummy app 2
app2 = Dash(__name__,
			requests_pathname_prefix='/app2/')

tako = 'https://github.com/Michael-fore/Dash_IIS/blob/master/tako.jpg?raw=true'
keana = 'https://github.com/Michael-fore/Dash_IIS/blob/master/keana.jpg?raw=true'

img_style = {
	'width': '50%',
	'height': 'auto'
	}

app2.layout = html.Div([
	html.H1('App 2'),
	html.Div(
		[
		html.Div(
			[html.H3('Tako'),
			html.Img(src=tako, style=img_style)]
		),
		html.Div(
			[html.H3('Keana'),
			html.Img(src=keana, style=img_style)]
		)],
		style={'display':'flex'})
	]
	)
	
if __name__ == '__main__':
	app2.run_server(debug=True)
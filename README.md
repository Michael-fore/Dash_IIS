# Contact

[Add me on Linkedin](https://www.linkedin.com/in/michael-fore-11a46a58/), if you want any custom work done this is a good place to reach me.

I don't use [Twitter](https://twitter.com/Wolfman_Brother) all that much, but here it is.

# Dash_IIS

Reposity for a youtube tutorial on how to run multiple dash apps in IIS.

This will run on a local venv and use a local wfastcgi.

Reposity for a youtube tutorial on how to run a flask app in IIS.

0. Clone this repo to wwwroot

1. Create virtual environment: `python -m venv venv`

1.5 Install requirements: `"venv/Scripts/python.exe" -m pip install -r requirements.txt`

2. Enable [CGI for IIS](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/cgi)

3. Ensure proper file permissions 

4. Configure Web.config

Youtube Tutorial: 

* Make sure the entire dash_iis folder is readable by IIS_IUSRS, or whichever group is running the IIS process




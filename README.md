# Contact

[Add me on Linkedin](https://www.linkedin.com/in/michael-fore-11a46a58/), if you want any custom work done or need extra help this is a good place to reach me.

I don't use [Twitter](https://twitter.com/Wolfman_Brother) all that much, but here it is.

# Dash_IIS

Reposity for a youtube tutorial on how to run multiple dash apps in IIS.

This will run on a local venv and use a local wfastcgi.

Reposity for a youtube tutorial on how to run a flask app in IIS.

0. Clone this repo to wwwroot

0.5. Set the created repo as the current directory `cd dash_iis`

1. Create virtual environment: `python -m venv venv`

2. Install requirements: `"venv/Scripts/python.exe" -m pip install -r requirements.txt`

3. Enable [CGI for IIS](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/cgi)

4. Ensure proper file permissions 

5. Configure Web.config

6. Add application to iis

Youtube Tutorial: https://www.youtube.com/watch?v=sgFTX-SVh20

* Make sure the entire dash_iis folder is readable by IIS_IUSRS, or whichever group is running the IIS process




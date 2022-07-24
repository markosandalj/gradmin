How to set enviornment?
Run this command from root folder in terminal

Unix based (MacOS or Linux):
export DJANGO_SETTIGNS_MODULE=gradmin.settings.local (or gradmin.settings.dev or gradmin.settings.prod)

Windows:
set DJANGO_SETTINGS_MODULE=mysite.settings.local (or gradmin.settings.dev or gradmin.settings.prod)


Command for installing all pacakges 
pip install -r /path/to/requirements.txt

Command for saving all pacakges in a single file
pip freeze > requirements.txt

git clone https://github.com/markosandalj/gradmin.git gradmin
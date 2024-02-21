# Toodl
Welcome to Toodl, a time management system.

Located at <a href="https://toodl.azurewebsites.net/">toodl.azurewebsites.net
<div>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" title="Django" alt="Django"/>&nbsp;
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" title="PostgreSQL" alt="PostgreSQL"/>&nbsp;
  <img src="https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white" title="Azure" alt="Azure"/>&nbsp;
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" title="Github" alt="Github"/>&nbsp;
</div>

## Steps to install Toodl to your machine
Note: Make sure you have Python installed and a valid Azure PostgreSQL database to link to.
1. Clone the repository to your local machine
   ```
   git clone https://github.com/Conner-Fulford/toodl.git
   ```
2. Open the project in your editor and copy .env.example into your .env file, replacing the values with your own.
   ```
   cp .env.example .env
   ```
3. Create a virtual environment and install the required packages
   ```
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Make migrations and migrate to your Azure PostgreSQL database
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the server and navigate to https://127.0.0.1:8000
   ```
   python manage.py runserver
   ```

## File Structure:
```---  Folder Structure ---
[toodl]
    ├── [.devcontainer]
        └── devcontainer.json
    ├── .env.example
    ├── .gitignore
    ├── CONTRIBUTING.md
    ├── [home]
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── [migrations]
            ├── 0001_initial.py
            ├── __init__.py
        ├── [migrations_old]
            ├── 0001_initial.py
            ├── 0003_alter_event_id.py
            ├── 0004_alter_event_description_alter_event_endtime_and_more.py
            ├── 0005_alter_event_id.py
            └── __init__.py
        ├── models.py
        ├── [templates]
            ├── calendar.html
            ├── index.html
            ├── login.html
            └── register.html
        ├── [tests]
            ├── test_forms.py
            ├── test_models.py
            ├── test_urls.py
            ├── test_views.py
            └── __init__.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── __init__.py
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── [static]
        ├── [dist]
            ├── [css]
                ├── <css files>
            ├── [img]
                ├── <css images>
            └── [js]
                ├── <javascript files>
        └── [plugins]
            ├── [bootstrap]
                └── [js]
                    ├── <javascript files>
            ├── [fontawesome-free]
                ├── [css]
                    ├── <css files>
                └── [webfonts]
                    ├── <font files>
            ├── [icheck-bootstrap]
                ├── <css files>
            └── [jquery]
                ├── <javascript files>
    ├── [staticfiles]
        ├── [admin]
            ├── [css]
                ├── <css files>
            ├── [img]
                ├── <svg files>
            └── [js]
                ├── <javascript files>
        ├── [dist]
            ├── [css]
                ├── <css files>
            ├── [img]
                ├── <img files>
            └── [js]
                ├── <javascript files>
            ├── [fontawesome-free]
                ├── [css]
                    ├── <css files>
                └── [webfonts]
                    ├── <font files>
            ├── [icheck-bootstrap]
                ├── <css files>
            └── [jquery]
                ├── <javascript files>
    └── [toodl]
        ├── asgi.py
        ├── azure_storage.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        ├── __init__.py
```
## Collaborators:
```
Conner-Fulford; Conner Fulford;     
4am-walking;    Chandler Matheny;    
Durantye;       Damion Mason;       
VHT692;         Ian Powers;         
utchaozhou;     Eric Chang;         
```

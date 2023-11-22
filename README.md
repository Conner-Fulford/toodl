# Toodl
Welcome to Toodl, a time management system.
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

Collaborators:
```
Conner-Fulford; Conner Fulford;     DNF283
4am-walking;    Chandler Matheny;   HTC878 
Durantye;       Damion Mason;       DLB636
VHT692;         Ian Powers;         VHT692
utchaozhou;     Eric Chang;         KXM618
```

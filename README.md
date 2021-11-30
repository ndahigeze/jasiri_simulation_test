# JUNIOR SOFTWARE DEVELOPER JOB SIMULATION ACTIVITY

* jasir_simulation_test is django project for managing user contacts and their basic informations

# Process and steps for hosting this application on ubuntu server

## Installing required libraries  for environment

## Use the following commands to install python libaries and nginx webserver 

    $sudo apt-get update
    $sudo apt-get install python3-pip python3-dev libpq-dev nginx

## Use the following command to install mysql
    $ sudo apt install mysql-server
 
##configure mysql 
 
### run the security script which will take you ththroug a series of prompt for mysql installation's security options 
       $ sudo mysql_secure_installation
     
 ### create user and grant all privileges
     
        $sudo  mysql -u root -p
        
        #### run the followinf to create user and and password
        mysql> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
        
        #### grant all privilege
        mysql>GRANT PRIVILEGE ON database.table TO 'username'@'host';
        mysql>FLUSH PRIVILEGES;
        mysql>exit
        $sudo  mysql -u newUser -p
   * create project datatabase
        

 ## Prepared virtual environment for the project
   * Clone this project in your desire folder
   * Enther int the project root directory
   
   ### Install virtualenv for creating project virtual environment 
    $ sudo -H pip3 install --upgrade pip
    $ sudo -H pip3 install virtualenv
   
   ### create virtual environment
    $ virtualenv myprojectenv
   
   ### Activate virtual environment and install gunicorn for running the application
    $ source myprojectenv/bin/activate
    $ pip install django gunicorn psycopg2
   
   ### Install all requirements for the projects 
    $ pip install -r requirements.txt  
   
   ### Prepare .env file for setting required environment variables 
        DB_NAME="YOUR_DB_NAE"
        DB_USER="yOUR_MYSQL_USER"
        DB_PASSWORD="DB_USER_PASSWORD"
        DB_HOST="DB_HOST"
        DB_PORT="MYSQL_PORT"
        DEBUG=True/False
        CSRF_COOKIE_SECURE=True/False
        CSRF_COOKIE_HTTPONLY=True/False
        SESSION_COOKIE_HTTPONLY=True/False

   ### Run migrations for setting the database 
       $python manage.py makemigrations
       $python manage.py migrate
       $python manage.py createsuperuser 
       $python manage.py collectstatic
  
   ### Allow pproject port
       $ sudo ufw allow 8000
       $ manage.py runserver 0.0.0.0:8000 // for testing if project can run on allowed port
       $ http://server_domain_or_IP:8000 //visit server name or ip with the port allowed 
       hit ctl-c for closing tha application
   
   ### Test Gunicorn
      $ gunicorn --bind 0.0.0.0:8000 myproject.wsgi // this will start gunicorn on the same interface application is runnig on 
      $ http://server_domain_or_IP:8000 //visit server name or ip with the port allowed 
      * hit ctl-c for closing tha application
  
  ## Create Gunicorn systmem Service file
    $ sudo nano /etc/systemd/system/gunicorn.service
    * Copy the following into THE FILE
     "  [Unit]
        Description=gunicorn daemon
        After=network.target

        [Service]
        User=sammy
        Group=www-data
        WorkingDirectory=/home/user/myproject
        ExecStart=/home/user/projectrootfolder/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/user/projectrootfolder/myproject.sock myproject.wsgi:application

        [Install]
        WantedBy=multi-user.target"
        
### restart gunicorn
      $ sudo systemctl start gunicorn
      $ sudo systemctl enable gunicorn
      
   ## Confirgure Nginx
   
### create new server block for the project
    $ sudo nano /etc/nginx/sites-available/myproject
   
   * Copy the following into the file 
   
    server {
            listen 80;
            server_name server_domain_or_IP;

            location = /favicon.ico { access_log off; log_not_found off; }
            location /static/ {
                root /home/user/projectrootfolder;
            }
            location / {
                include proxy_params;
                proxy_pass http://unix:/home/user/projectrootfolder/myproject.sock;
            }
        } 
        
        
   ### link the file created with nginx sites-enabled folder
      $ sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
      $ sudo ufw allow 'Nginx Full'  <!--Allowing nginx in firewall -->
      $ systemctl restart nginx
      
      after this You access the server domain name or ip to access the application 
      
        
        

   

  

 
    
  
  
  
  
  
   
   

  
   

   
   
   
   
   
   
 
 
        
        

        





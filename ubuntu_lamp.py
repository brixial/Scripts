#!/usr/bin/env python2
import os
import random
import subprocess
print("Launching Terminal User Interface")  
print("\t\tWELCOME TO INSTALL LAMP\t\t") 
print("\t-------------------------------------------------\t") 
print("Entering for Setup")
while True:
    print("""
	1.Install Apache
	2.NGINX
	3.MARIADB
	4.Mysql Secure Installation
	5.PHP
	6.Phpmyadmin
	7.Exit
    """)
    ch=int(input("Enter your choice: "))
    if (ch == 1):
        os.system("sudo apt-get update && apt get upgrade -y")
        os.system("sudo apt-get install apache2 -y")
        os.system("sudo systemctl restart apache2")
        os.system("sudo systemctl enable apache2")
        print("<------apache installaed and enabled properly------>")
    elif ch == 2:
        os.system("sudo apt-get update && apt get upgrade -y")
        os.system("sudo apt-get install nginx -y")
        os.system("sudo systemctl start nginx")
        os.system("sudo systemctl enable nginx")
        print("<------nginx installaed and enabled properly------>")
    elif ch == 3:
        os.system("sudo apt-get update && apt get upgrade -y")
        os.system("sudo apt-get install mariadb-server -y")
        os.system("sudo systemctl start mariadb")
        os.system("sudo systemctl enable mariadb")
    elif ch == 4:
        rpassword = ''
        for _ in range(10): 
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            rpassword += (chr(random_integer))
        
        user_pass = ''
        for _ in range(10): 
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            user_pass += (chr(random_integer))
        os.system(f"sudo mysqladmin -u root password {rpassword}")
        with open("/tmp/db.setup" , "a+" , buffering = 1)as db1:
            db1.write("UPDATE mysql.user SET plugin ='mysql_native_password' WHERE User ='root'; \n")
            db1.write("DELETE FROM mysql.user WHERE User='';\n")
            db1.write("DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1'); \n")
            db1.write("DROP DATABASE IF EXISTS test;\n")
            db1.write("DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';\n")
            db1.write(f"CREATE USER 'phpmyadmin'@'localhost' IDENTIFIED BY '{user_pass}';\n")
            db1.write("GRANT ALL PRIVILEGES ON *.* TO 'phpmyadmin'@'localhost';\n")
            db1.write("FLUSH PRIVILEGES;\n")
            db1.close()
        os.system(f"sudo mysql -u root --password={rpassword} < /tmp/db.setup")
        print("mysql root password is:")
        os.system(f"sudo echo {rpassword}")
        print("password for user phpmyadmin is:")
        os.system(f"sudo echo {user_pass}")
    elif ch == 5:
        print("setting environment for php installation")
        os.system("sudo apt-get install software-properties-common -y")
        os.system("sudo add-apt-repository ppa:ondrej/php")
        os.system("sudo apt-get update")
        print(""" 
            1.Php 7.0 
            2.Php 7.1 
            3.Php 7.2 
            4.Php 7.3
            5.Php 7.4 
            6.Exit
            """)
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            os.system("apt-get install -y php7.0 php7.0-mbstring php7.0-mysql php7.0-xml")
        elif ch == 2:
            os.system("apt-get install -y php7.1 php7.1-mbstring php7.1-mysql php7.1-xml")
        elif ch == 3:
            os.system("apt-get install -y php7.2 php7.2-mbstring php7.2-mysql php7.2-xml")
        elif ch == 4:
            os.system("apt-get install -y php7.3 php7.3-mbstring php7.3-mysql php7.3-xml")
        elif ch == 5:
            os.system("apt-get install -y php7.4 php7.4-mbstring php7.4-mysql php7.4-xml")
        elif ch == 6:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 6:
        os.system("sudo apt-get install phpmyadmin -y")
        os.system("sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-available/phpmyadmin.conf")
        os.system("sudo a2enconf phpmyadmin")
        os.system("sudo phpenmod mbstring")
        os.system("sudo service apache2 restart")
        print("phymyadmin Installed and configured properly use phpmyadmin user to login")
    elif ch == 7:
        print("Exiting Script")
        exit()
    else:
        print("Invalid entry")

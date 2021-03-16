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
	7.selinux
    8.Exit
    """)
    ch=int(input("Enter your choice: "))
    if (ch == 1):
        os.system("sudo yum update -y")
        os.system("sudo yum install httpd -y")
        os.system("sudo systemctl restart httpd")
        os.system("sudo systemctl enable httpd")
        print("<------apache installed and enabled properly------>")
    elif ch == 2:
        os.system("sudo yum update-y")
        os.system("sudo yum install nginx -y")
        os.system("sudo systemctl start nginx")
        os.system("sudo systemctl enable nginx")
        print("<------nginx installed and enabled properly------>")
    elif ch == 3:
        os.system("sudo yum update -y")
        os.system("sudo yum install mariadb-server -y")
        os.system("sudo systemctl start mariadb")
        os.system("sudo systemctl enable mariadb")
    elif ch == 4:
        crpassword = ''
        for _ in range(10): 
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            crpassword += (chr(random_integer))
        
        cuser_pass = ''
        for _ in range(10): 
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            cuser_pass += (chr(random_integer))

        with open("/tmp/db.setup" , "a+" , buffering = 1)as db1:
            db1.write(f"UPDATE mysql.user SET Password=PASSWORD('{crpassword}') WHERE User='root';\n")
            db1.write("UPDATE mysql.user SET plugin ='' WHERE User ='root'; \n")
            db1.write("DELETE FROM mysql.user WHERE User='';\n")
            db1.write("DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1'); \n")
            db1.write("DROP DATABASE IF EXISTS test;\n")
            db1.write("DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';\n")
            db1.write(f"CREATE USER 'phpmyadmin'@'localhost' IDENTIFIED BY '{cuser_pass}';\n")
            db1.write("GRANT ALL PRIVILEGES ON *.* TO 'phpmyadmin'@'localhost';\n")
            db1.write("FLUSH PRIVILEGES;\n")
            db1.close()
        os.system(f"sudo mysql -u root < /tmp/db.setup")
        print("mysql root password is:")
        os.system(f"sudo echo {crpassword}")
        print("password for user phpmyadmin is:")
        os.system(f"sudo echo {cuser_pass}")
    elif ch == 5:
        print("setting environment for php installation")
        os.system("sudo yum install wget vim net-tools -y")
        os.system("sudo wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
        os.system("sudo rpm -Uvh epel-release-latest-7.noarch.rpm")
        os.system("sudo yum install -y epel-release")
        os.system("sudo wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm")
        os.system("sudo rpm -Uvh remi-release-7.rpm")
        os.system("sudo yum install -y yum-utils")
        print(""" 
            1.Php 7.0 
            2.Php 7.1 
            3.Php 7.2 
            4.Php 7.3
            5.Php 7.4 
            6.Php 5.4
            7.Exit
            """)
        ch=int(input("Enter your choice: "))
        if(ch == 1):
            os.system("yum-config-manager --enable remi-php70")
            os.system("sudo yum install -y php")
        elif ch == 2:
            os.system("yum-config-manager --enable remi-php71")
            os.system("sudo yum install -y php")
        elif ch == 3:
            os.system("yum-config-manager --enable remi-php72")
            os.system("sudo yum install -y php")
        elif ch == 4:
            os.system("yum-config-manager --enable remi-php73")
            os.system("sudo yum install -y php")
        elif ch == 5:
            os.system("yum-config-manager --enable remi-php74")
            os.system("sudo yum install -y php")
        elif ch == 6:
            os.system("sudo yum install -y php")
        elif ch == 7:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 6:
        os.system("sudo yum --enablerepo=remi install -y phpMyAdmin")
        a_file = open("/etc/httpd/conf.d/phpMyAdmin.conf", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[12] = "Require all granted\n"
        list_of_lines[13] = "#Require local\n"
        a_file = open("/etc/httpd/conf.d/phpMyAdmin.conf", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        os.system("sudo systemctl restart httpd")
        print("phymyadmin Installed and configured properly use phpmyadmin user to login")
    elif ch == 7:
        a_file = open("/etc/selinux/config", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[6] = "SELINUX=disabled\n"
        a_file = open("/etc/selinux/config", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        print("Selinux Disabled Done")
    elif ch == 8:
        print("Exiting Script")
        exit()
    else:
        print("Invalid entry")

#!/usr/bin/bash
dnf install wget firewalld  -y
echo "Successfully installed Jdk"
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum upgrade -y
dnf install jenkins java-1.8.0-openjdk-devel -y
systemctl daemon-reload
systemctl start jenkins
systemctl enable jenkins
systemctl start firewalld
systemctl enable firewalld
firewall-cmd --permanent --zone=public --add-port=8080/tcp
firewall-cmd --reload
echo "Jenkins installed and Running"
JenPass=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo "Creating User1 in Jenkins"
wget http://localhost:8080/jnlpJars/jenkins-cli.jar
echo 'jenkins.model.Jenkins.instance.securityRealm.createAccount("user1", "password1")' | java -jar ./jenkins-cli.jar -s "http://localhost:8080" -auth admin:$JenPass -noKeyAuth groovy = –
echo "Creating User2"
echo 'jenkins.model.Jenkins.instance.securityRealm.createAccount("user2", "password2")' | java -jar ./jenkins-cli.jar -s "http://localhost:8080" -auth admin:$JenPass -noKeyAuth groovy = –
echo "Users Created Successfully !"
```bash
groupadd -g 1000 snnb && useradd -u 1000 -g 1000 -m snnb
chsh -s /bin/bash snnb
apt-get install sudo
usermod -aG sudo snnb
passwd snnb
su snnb

sudo apt-get install postfix nano pip systemctl mailutils rsyslog sudo
```

for docker logs:
sudo apt-get install -q -y syslog-ng
service syslog-ng start

1. Add the following at the end of /etc/postfix/master.cf

naloemailapi unix - n n - - pipe
flags=FR user=localuser argv=/path/to/email_forwarder.py
${nexthop} ${user}

2. Add the following at the end of /etc/postfix/main.cf

transport_maps = hash:/etc/postfix/transport

3. Add the following line to /etc/postfix/transport

-   naloemailapi:

4. Run the following to update the postfix configuration

sudo postmap /etc/postfix/transport
sudo systemctl reload postfix

5. Put script somewhere postfix can access and add necessary permissions

6. pip install requests

7. If issues with public/pickup run:

sudo mkfifo /var/spool/postfix/public/pickup
sudo service postfix restart

chown syslog:adm /var/log/mail.log
chmod 640 /var/log/mail.log

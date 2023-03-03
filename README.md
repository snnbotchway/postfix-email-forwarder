# Instructions

1. Add the following at the end of /etc/postfix/master.cf(localuser must be a user on the system.)

```txt
yourtransportname  unix  -       n       n       -       -       pipe
  flags=FR user=localuser argv=/path/to/email_forwarder.py
  ${nexthop} ${user}
```

2. Add the following at the end of /etc/postfix/main.cf

```
transport_maps = hash:/etc/postfix/transport
```

3. Add the following line to /etc/postfix/transport

```
*   yourtransportname:
```

4. Run the following to update the postfix configuration

```
sudo postmap /etc/postfix/transport
sudo systemctl reload postfix
```

5. Put script somewhere postfix can access and add necessary permissions

6. `pip install requests`

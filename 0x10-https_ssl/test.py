import requests as r
import sys


@tckiprotich ➜ /workspaces/alx-system_engineering-devops (master) $ sudo certbot certonly --standalone -d www.tckiprotich.tech
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator standalone, Installer None
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for www.tckiprotich.tech
Waiting for verification...
Challenge failed for domain www.tckiprotich.tech
http-01 challenge for www.tckiprotich.tech
Cleaning up challenges
Some challenges have failed.

IMPORTANT NOTES:
 - The following errors were reported by the server:

   Domain: www.tckiprotich.tech
   Type:   connection
   Detail: 107.23.27.91: Fetching
   http://www.tckiprotich.tech/.well-known/acme-challenge/yiDhmGuOwz11lG-RwItaKNZAm1FmWEZ56BfTczFgwqs:
   Connection refused

   To fix these errors, please make sure that your domain name was
   entered correctly and the DNS A/AAAA record(s) for that domain
   contain(s) the right IP address. Additionally, please check that
   your computer has a publicly routable IP address and that no
   firewalls are preventing the server from communicating with the
   client. If you're using the webroot plugin, you should also verify
   that you are serving files from the webroot path you provided.
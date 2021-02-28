# scheduler-rpi
 
example of `data.yml`:
```yaml
backup:
  upload_dir: /rpi-services-backup
  dirs:
    - /home/pi/rpi-services
  ignore:
    - .git
    - .idea
    - .xml
    - .iml
    - .pyc
    - __pycache__
dropbox:
  token: 

cloudflare:
  token: cloudflare token

ip-changer:
  zone: zone id from cloudflare
  names:
    - example.com
```
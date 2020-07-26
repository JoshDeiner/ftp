

# if you want to test this repo, set this up locally with the below or similar

* https://linuxconfig.org/how-to-setup-ftp-server-on-ubuntu-20-04-focal-fossa-linux

* https://linuxconfig.org/how-to-setup-sftp-server-on-ubuntu-20-04-focal-fossa-linux


## you can also expirement with sftp server with docker https://hub.docker.com/r/atmoz/sftp/

* docker run -p 2222:22 -d atmoz/sftp foo:pass:::upload

* sftp -P 2222 foo@hostip

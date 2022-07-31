# Exercise v. 1.0

### DONE
- GITHUB REPOSITORY: https://github.com/sachama/exercise10
- README.md
- vagrant box: alvistack/centos-8-stream
  - forwarded_port: guest: 80, host: 8080
  - provision: ansible
- ansible playbook: playbook.yml
  - install and configure nginx
    - listen 80
    - location /app:  proxy_pass http://localhost:6000/app;
    - location /health proxy_pass http://localhost:5000/metrics;
    - location / proxy_pass http://localhost:3000/; # grafana
- install and configure python3 simple web: webapp.py
- grafana
  - default Grafana web interface with user authentication: # initial admin yet :( 
  - source: # source is needed add manually yet :(
      prometheus:
        HTTP:
          URL: http://localhost:7090
          Acess: Browser

### TODO
- location /grafana/dashboard
- read-only Grafana dashboard
- store application passwords in Ansible vault (the master password can be stored in clear text form in the repo)
- harden a system's security with firewall and SELinux
- ensure all services are up and running even after Vagrant box reboot


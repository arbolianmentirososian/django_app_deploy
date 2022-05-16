FROM python:3

RUN useradd -m python

WORKDIR /opt/django_app_deploy
COPY requirements.txt . 

RUN pip install --trusted-host devops-nexus-pl.ncplus.pl \
    --index-url https://pip:Nex8sCpl8s@devops-nexus-pl.ncplus.pl/repository/pypi-proxy/simple \
    --extra-index-url https://pip:Nex8sCpl8s@devops-nexus-pl.ncplus.pl/repository/python-releases/simple \
    --no-cache-dir -r requirements.txt
   
COPY . .

RUN chown -R python:python /opt/django_app_deploy

USER python

RUN chmod u+x run.sh

EXPOSE 8080

CMD ["./run.sh"]

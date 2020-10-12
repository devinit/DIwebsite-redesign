# Blue Green Deployment wih Docker Compose, Nginx, Consul and Registrator

- Blue-green deployment is used to minimise service downtime when deploying codebase changes to production.
- The app is deployed to two different production environments with identical configurations (i.e. “blue” and “green”). At any time, at least one of them will be alive and servicing requests in production while the other is idle and used as a failover. 

## The files of interest in this repository are

- docker-compose-consul.yml — Defines Consul and Registrator services.
- docker-compose.yml — Defines the blue and green services, Nginx service, and other application services.
- deploy.sh — Used to simulate application deployment. This is run by the CI(github actions)
- scripts/rollback.sh — Used to simulate application rollback from 1 environment to the other.
- short_deploy.sh - runs the application services(only if the server is already setup with all the variables present)
The combination of Consul, Registrator and Compose is used to implement service discovery in the application.

### Manual Setup on the server using (short_deploy.sh)

- Run docker network create consul to create a new network;
- Run ./short_deploy.sh to first run the blue instance;
- Open in browser `<http://ip_address` to view the blue app running;
- Run ./short_deploy.sh to imitate deploying of a new app;
- Open in browser `<http://ip_address>` to check a new version;
- Run scripts/rollback.sh to imitate a rollback;

### Auto Deployment via Github Actions using (deploy.sh)

- Add these required environment variables via github secrets

```sh
        PORT  - SSH port
        KEY - private ssh key
        DEV_ENV - staging environment
        DEV_HOST - Staging server IP
        USERNAME - username for the staging server
        DEV_BRANCH - branch for the staging environment
        PROD_ENV - production environment
        PROD_HOST - production server IP
        USERNAME - production username
        PROD_BRANCH - production branch
        RABBITMQ_PASSWORD - rabbitmq password
        ELASTIC_SEARCH_URL - elasticsearch url
        ELASTIC_PASSWORD - elasticsearch password
        SECRET_KEY
        ELASTIC_USERNAME
        CELERY_BROKER_URL
        DATABASE_URL
        DEFAULT_FROM_EMAIL
        EMAIL_HOST
        EMAIL_BACKEND
        EMAIL_HOST_USER
        EMAIL_HOST_PASSWORD
        HS_API_KEY
        HS_TICKET_PIPELINE
        HS_TICKET_PIPELINE_STAGE
```

- The deployment stage shall only run for the develop and master branches

### Nginx configuration with Consul

- The nginx config in the `config/nginx` directory relies on consul templates to automatically update an NGINX configuration file with the latest list of backend servers using Consul's service discovery.
- When building the nginx service with docker, nginx copies the `consul-template.service` to `/etc/service/consul-template/run` and `django.conf.ctmpl` to `/etc/consul-templates`. This queries the local Consul instance, rendering the template and restarting nginx if the template has changed.
- Incase a change is made to the nginx config, it needs to reflect in the consul template by running `docker-compose up -d --build nginx`.

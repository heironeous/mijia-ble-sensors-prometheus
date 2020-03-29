This is a folder to store your data that was gathered by prometheus.

This folder is used within `<REPOPATH>/quick-start/docker-compose.yml`. This folder 
makes sure that prometheus data is preserved between prometheus restarts. 

If you wish to have an ephemeral prometheus, please remove the volume mount
from the `<REPOPATH>/quick-start/docker-compose.yml`, and run `docker-compose up -d`.
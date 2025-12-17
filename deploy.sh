#!/bin/bash
# Connect to kooldock and run docker compose
# Assumes the project is at /Users/kooldock/odoo on the remote machine

echo "Syncing files to kooldock.local..."
rsync -avz --exclude 'node_modules' --exclude '.next' --exclude '.git' --exclude '.DS_Store' . kooldock@kooldock.local:/Users/kooldock/odoo

echo "Deploying to kooldock.local..."
ssh kooldock@kooldock.local "export PATH=\$PATH:/usr/local/bin && export DOCKER_CONFIG=\$(mktemp -d) && mkdir -p \$DOCKER_CONFIG/cli-plugins && ln -s ~/.docker/cli-plugins/* \$DOCKER_CONFIG/cli-plugins/ && echo '{\"credsStore\":\"desktop\"}' > \$DOCKER_CONFIG/config.json && cd /Users/kooldock/odoo && docker pull odoo:latest && docker compose down && docker compose up -d --build"

if [ $? -eq 0 ]; then
  echo "Deployment successful! App should be running at http://kooldock.local:8069"
else
  echo "Deployment failed."
fi

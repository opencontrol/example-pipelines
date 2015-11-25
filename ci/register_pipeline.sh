#!/bin/bash
fly --target dragon set-pipeline --var "github-private-key=$(cat ~/.ssh/id_rsa)" --load-vars-from cred.yml --config pipeline.yml --pipeline jinja-docker-image

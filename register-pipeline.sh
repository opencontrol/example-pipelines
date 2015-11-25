fly --target dragon set-pipeline --var "github-private-key=$(cat ~/.ssh/id_rsa)" --load-vars-from credentials.yml --config pws-fedramp.yml --pipeline pws-fedramp

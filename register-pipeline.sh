fly --target dragon configure --var "github-private-key=$(cat ~/.ssh/id_rsa)" --vars-from credentials.yml --config pws-fedramp.yml pws-fedramp 

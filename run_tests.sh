# Concourse does this for real, here's a little local demo
# Make a system data YML
python jinjame.py "inputs/*.y*ml" output/test-output.yml
# Make a gitbook markdown
# using the output folder as input here is weird...
python jinjame.py --template_path='templates/ssp-gitbook' --template_file='gitbook-markdown.template' "output/test-output.yml" output/test-gitbook.md

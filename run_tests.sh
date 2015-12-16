# Concourse does this for real, here's a little local demo
# Make a system data YML
python jinjame.py ssp --template_file='datatree.tmpl' "inputs/*.y*ml" output/test-output.yml
# Make a gitbook markdown
# using the output folder as input here is weird...
python jinjame.py markdown --template_path='./templates/ssp-gitbook' --manifest_file='manifest.tmpl' "output/test-output.yml" output/

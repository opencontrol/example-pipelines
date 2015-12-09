import jinjame
from jinjame import yaml_query
data_tree = jinjame.load_data_tree(["./inputs/*.y*ml"])
print data_tree
for node in yaml_query("**/Manifests", data_tree):
    print node
    print node.parent_node

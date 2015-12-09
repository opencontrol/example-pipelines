# example-pipelines
Example concourse pipelines for OpenControl pipelining

AKA: dpath-jinja

## FAQ

What?

Python Only?

Why? What problem does this solve?

How does it work?

Namespaces: implicit and explicit

Is it ready?

Is this the right way to do this?
Code Smell? Data Smell?
Immutable infrastructure as a YAML tree??

Related work:



## TODO:

* SUPPORT YAML TAGs for schema

```
# returns a list of oc_node objects with .path_seq and .parent_node
get_nodes(
  dpath="**/!component",
  where=["/satisfies/NIST-800-53/AC-2", "/verified_by/machine" ]
)
```

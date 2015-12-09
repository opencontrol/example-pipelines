#!/usr/bin/env python
"""
Merge a set of YAML files and use them to generate docs using jinja2 templates.
"""

import click
import os
import yaml
import pyaml
import dpath
import glob
from jinja2 import Environment, FileSystemLoader
import datetime
try:
    from UserDict import IterableUserDict as IUD
except ImportError:
    from collections import UserDict as IUD


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True)

def pyaml_dump(obj, indent=4):
    return pyaml.yaml.dump(obj, indent=indent)

TEMPLATE_ENVIRONMENT.globals['yaml_dump'] = pyaml_dump
TEMPLATE_ENVIRONMENT.filters['timestamp'] = datetime.datetime.now

def dpath_dot_loop(expr, context):
    return dpath.util.search(context, expr, yielded=True, separator=".")

def dpath_loop(expr, context, separator="/"):
    print ("Looping thru dpath of %s" % (expr))
    return dpath.util.search(context, expr, yielded=True, separator=separator)

def dpath_get(expr, context):
    print ("Getting %s" % (expr))
    return dpath.util.get(context, expr)

def dpath_search(expr, context):
    print ("Searching for %s" % (expr))
    try:
        return dpath.util.search(context, expr)
    except:
        return ""

def yaml_get(expr, context, separator="/"):
    return next(yaml_query(expr, context, separator=separator))

def yaml_query(expr, context, separator="/"):
    for (path, node) in dpath_loop(expr, context, separator=separator):
        path_seq = path.split(separator)
        yield oc_node(node, path_seq, context)

# Using tuples of (node, [path items], parent_node)
# allows us to make PARENT addressable nodes
class oc_node(IUD):
    def __init__(self, value, path_seq, context):
        self.path_seq = path_seq
        self.context = context
        self.data = value
    #
    # def __repr__(self):
    #     return self.value
    #
    # def __str__(self):
    #     return str(self.value)
    #
    # def __getitem__(self, item):
    #     return data.__getitem__(item)

    @property
    def parent_node(self):
        return yaml_get(self.path_seq[:-1], self.context)


TEMPLATE_ENVIRONMENT.globals['dpath_dot_loop'] = dpath_dot_loop
TEMPLATE_ENVIRONMENT.globals['dpath_loop'] = dpath_loop
TEMPLATE_ENVIRONMENT.globals['dpath_get'] = dpath_get
TEMPLATE_ENVIRONMENT.globals['dpath_search'] = dpath_search
TEMPLATE_ENVIRONMENT.globals['dpath'] = dpath
TEMPLATE_ENVIRONMENT.globals['yaml_get'] = yaml_get
TEMPLATE_ENVIRONMENT.globals['yaml_query'] = yaml_query

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def read_template_as_yaml(template_filename, context):
    return yaml.load(render_template(template_filename, context))

def load_data_tree(inputs):
    context = {'inputs' : []}
    data_tree = {}
    for path_glob in inputs:
        for filename in glob.glob(path_glob):
            print ("loading %s" % (filename))
            obj_tree = yaml.load(open(filename, 'r'))
            short_filename = filename.split("/")[-1]
            context['inputs'].append(short_filename)
            if 'system' not in obj_tree: # old schema
                dpath.util.merge(data_tree, { short_filename: obj_tree })
            else:
                dpath.util.merge(data_tree,
                    { obj_tree['system']: { obj_tree['name']: obj_tree } })
    context.update({'data_tree' : data_tree})
    return context

@click.group()
def cli():
    pass

@cli.command('ssp')
@click.option('--template_path', default="./templates", help='Path to templates')
@click.option('--template_file', default="system-data.template", help='Template to process')
@click.argument('inputs', nargs=-1)
@click.argument('output', nargs=1, type=click.File('w'))
def create_ssp_yaml(template_path, template_file, inputs, output):
    context = load_data_tree(inputs)
    TEMPLATE_ENVIRONMENT.loader = FileSystemLoader(os.path.join(PATH, template_path))
    yml = render_template(template_file, context)
    output.write(yml.encode('utf-8'))


@cli.command('markdown')
@click.option('--template_path', default="./templates", help='Path to templates')
@click.option('--manifest_file', default="manifest.tmpl", help='Template to process')
@click.argument('inputs', nargs=-1)
@click.argument('output_path', nargs=1, type=click.Path(exists=True))
def create_docbook_markdown(template_path, manifest_file, inputs, output_path):
    context = load_data_tree(inputs)
    TEMPLATE_ENVIRONMENT.loader = FileSystemLoader(os.path.join(PATH, template_path))
    manifest = read_template_as_yaml(manifest_file, context)
    for page in manifest['pages']:
        print ("Generating ", page['filename'])
        with open("%s/%s" % (output_path, page['filename']), 'w') as output:
            local_context = {'data_tree' : dpath_search(page['dpath_query'], context['data_tree'])}
            if 'extra_context' in page:
                local_context.update(page['extra_context'])
            # print ("Local context: ")
            # print pyaml.dump(local_context)
            yml = render_template(page['template'], local_context)
            output.write(yml.encode('utf-8'))


if __name__ == "__main__":
    cli()

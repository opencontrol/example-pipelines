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

def dpath_loop(expr, context):
    print ("Looping thru dpath of %s" % (expr))
    return dpath.util.search(context, expr, yielded=True)

def dpath_get(expr, context):
    print ("Getting %s" % (expr))
    return dpath.util.get(context, expr)

def dpath_search(expr, context):
    print ("Searching for %s" % (expr))
    try:
        return dpath.util.search(context, expr)
    except:
        return ""

TEMPLATE_ENVIRONMENT.globals['dpath_dot_loop'] = dpath_dot_loop
TEMPLATE_ENVIRONMENT.globals['dpath_loop'] = dpath_loop
TEMPLATE_ENVIRONMENT.globals['dpath_get'] = dpath_get
TEMPLATE_ENVIRONMENT.globals['dpath_search'] = dpath_search
TEMPLATE_ENVIRONMENT.globals['dpath'] = dpath

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def load_data_tree(inputs):
    context = {'inputs' : []}
    data_tree = {}
    for path_glob in inputs:
        for filename in glob.glob(path_glob):
            print ("loading %s" % (filename))
            obj_tree = yaml.load(open(filename, 'r'))
            context['inputs'].append(filename)
            if 'system' not in obj_tree: # old schema
                dpath.util.merge(data_tree, { filename: obj_tree })
            else:
                dpath.util.merge(data_tree,
                    { obj_tree['system']: { obj_tree['name']: obj_tree } })
    context.update({'data_tree' : data_tree})
    return context

@click.command()
@click.option('--template_path', default="./templates", help='Path to templates')
@click.option('--template_file', default="system-data.template", help='Template to process')
@click.argument('inputs', nargs=-1)
@click.argument('output', nargs=1, type=click.File('w'))
def create_ssp_yaml(template_path, template_file, inputs, output):
    context = load_data_tree(inputs)
    TEMPLATE_ENVIRONMENT.loader = FileSystemLoader(os.path.join(PATH, template_path))
    yml = render_template(template_file, context)
    output.write(yml)


if __name__ == "__main__":
    create_ssp_yaml()

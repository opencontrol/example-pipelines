#!/usr/bin/env python

import click
import os
import yaml
import dpath
import glob
from jinja2 import Environment, FileSystemLoader
import datetime

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    trim_blocks=True,
    lstrip_blocks=True)

TEMPLATE_ENVIRONMENT.filters['yaml_dump'] = yaml.dump
TEMPLATE_ENVIRONMENT.filters['timestamp'] = datetime.datetime.now


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


@click.command()
@click.option('--template_path', default="./templates", help='Path to templates')
@click.option('--template_file', default="system-data.template", help='Template to process')
@click.argument('inputs', nargs=-1, type=click.Path(exists=True))
@click.argument('output', nargs=1, type=click.File('w'))
def create_ssp_yaml(template_path, template_file, inputs, output):
    context = {'inputs' : []}
    for path in inputs:
        for filename in glob.glob("%s/*.y*ml" % (path)):
            print ("loading %s" % (filename))
            obj_tree = yaml.load(open(filename, 'r'))
            context['inputs'].append(filename)
            if 'system' not in obj_tree: # old schema
                dpath.util.merge(context, { filename: obj_tree })
            else:
                dpath.util.merge(context,
                    { obj_tree['system']: { obj_tree['name']: obj_tree } })
    # print (pyaml.dump(context))
    def dpath_loop(expr):
        print ("Looping thru dpath of %s" % (expr))
        return dpath.util.search(context, expr, yielded=True)
    def dpath_get(expr):
        print ("Getting %s" % (expr))
        return dpath.util.get(context, expr)
    def dpath_search(expr):
        print ("Searching for %s" % (expr))
        try:
            return dpath.util.search(context, expr)
        except:
            return ""
    context.update({'dpath_search' : dpath_search,
                    'dpath_loop' : dpath_loop,
                    'dpath_get' : dpath_get
                    })

    TEMPLATE_ENVIRONMENT.loader = FileSystemLoader(os.path.join(PATH, template_path))
    yml = render_template(template_file, context)
    output.write(yml)


if __name__ == "__main__":
    create_ssp_yaml()

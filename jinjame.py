#!/usr/bin/env python

import click
import os
import yaml
import dpath
import glob
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)
TEMPLATE_ENVIRONMENT.filters['yaml_dump'] = yaml.dump


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


@click.command()
@click.argument('inputs', nargs=-1, type=click.Path(exists=True))
@click.argument('output', nargs=1, type=click.File('w'))
def create_ssp_yaml(inputs, output):
    context = {}
    for path in inputs:
        for filename in glob.glob("%s/*.y*ml" % (path)):
            dpath.util.merge(context, yaml.load(open(filename, 'r')))
    def dpath_query(expr):
        return dpath.util.search(context, expr)
    context.update({'dpath_query' : dpath_query})
    yml = render_template('pws-system.template', context)
    output.write(yml)


if __name__ == "__main__":
    create_ssp_yaml()

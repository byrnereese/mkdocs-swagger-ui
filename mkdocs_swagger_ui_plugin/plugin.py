import os
import sys
import fnmatch
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
import mkdocs.structure.files

import yaml
import json
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
    
import requests
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError
    
class SwaggerUIPlugin(BasePlugin):

    config_scheme = (
        ('do_nothing', mkdocs.config.config_options.Type(str, default='')),
        ('spec_url', config_options.Type(str, default='https://petstore.swagger.io/v2/swagger.json')),
        ('template', config_options.Type(str, default='swagger.md.tmpl')),
        ('outfile', config_options.Type(str, default='docs/swagger.md'))
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def generate_page_contents(self):
        spec_url    = self.config['spec_url']
        tmpl_url    = self.config['template']
        cur_dir     = os.path.dirname(__file__)
        print("INFO     -  Generating swagger-ui for spec: " + spec_url)
        print("DEBUG    -  template: " + tmpl_url)
        print("DEBUG    -  directory: " + cur_dir)
        env = Environment(
            loader=FileSystemLoader(['tmpl',os.path.join(cur_dir,'tmpl')]),
            autoescape=select_autoescape(['html', 'xml'])
        )
        md = markdown.Markdown()
        env.filters['markdown'] = lambda text: Markup(md.convert(text))
  
        template = env.get_template( tmpl_url )
        tmpl_out = template.render( spec=spec_url )
        print("DEBUG    - " + tmpl_out)
        return tmpl_out
    
    def on_config(self, config):
        print("INFO     -  swagger-ui plugin ENABLED")

    def on_page_read_source(self, page, config):
        index_path = os.path.join(config['docs_dir'], self.config['outfile'])
        page_path = os.path.join(config['docs_dir'], page.file.src_path)
        if index_path == page_path:
            contents = self.generate_page_contents()
            return contents

    '''
    def on_pre_build(self, config):
        outfile  = self.config['outfile']
        contents = self.generate_page_contents()
        dest = os.path.join(config['docs_dir'], outfile)
        with open(dest, "w") as fh:
            fh.write(contents)
        return config
    '''

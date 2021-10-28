from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
import mkdocs.structure.files

import yaml, json

from jinja2 import Environment, FileSystemLoader, select_autoescape, Markup

import markdown
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import URLError
    
class SwaggerUIPlugin(BasePlugin):

    config_scheme = (
        ('do_nothing', mkdocs.config.config_options.Type(str, default='')),
        ('spec_url', config_options.Type(str, default='https://netstorage.ringcentral.com/dpw/api-reference/specs/rc-platform.yml')),
        ('show_schema_by_default', config_options.Type(bool, default=False)),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def generate_page_contents(self):
        spec_url    = self.config['spec_url']
        schema_model_expand_depth = 0
        if self.config['show_schema_by_default']: schema_model_expand_depth = 1


        print("INFO    -  Generating API index for spec: " + spec_url)
        try:
            uri_parsed = urlparse( spec_url )
            if uri_parsed.scheme in ['https', 'http']:
                url = urlopen( spec_url )
                yaml_data = url.read()
        except URLError as e:
            print("ERROR   -  " + e)

        env = Environment(
            loader=FileSystemLoader('tmpl'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        md = markdown.Markdown()
        env.filters['markdown'] = lambda text: Markup(md.convert(text))
    
        print("Loading specs...")
        try:
            data = yaml.safe_load( yaml_data )
        except yaml.YAMLError as e:
            print("ERROR   -  " + e)

        TEMPLATE = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <title>Swagger UI</title>
            <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui.css" >
            <style>
                html
                {
                box-sizing: border-box;
                overflow: -moz-scrollbars-vertical;
                overflow-y: scroll;
                }
                *,
                *:before,
                *:after
                {
                box-sizing: inherit;
                }
                body {
                margin:0;
                background: #fafafa;
                }
                .try-out {
                display: none;
                }
            </style>
          </head>
          <body>
            <div id="swagger-ui"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-bundle.js"> </script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-standalone-preset.js"> </script>
            <script>
                window.onload = function() {
                    var spec = %s;
                    // Build a system
                    const ui = SwaggerUIBundle({
                        spec: spec,
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        defaultModelsExpandDepth: %d,
                        presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIStandalonePreset
                        ],
                        plugins: [
                        SwaggerUIBundle.plugins.DownloadUrl
                        ],
                        layout: "StandaloneLayout"
                    })
                    window.ui = ui
                    let elem1 = document.getElementsByClassName("download-url-wrapper");
                    while(elem1.length > 0){
                        elem1[0].parentNode.removeChild(elem1[0]);
                    }
                    let elem2 = document.getElementsByClassName("topbar");
                    while(elem2.length > 0){
                        elem2[0].parentNode.removeChild(elem2[0]);
                    }
                }
            </script>
          </body>
        </html>
        """
        print("Writing specs...")
        file = open('docs/api-index.html', 'w+')
        file.write(TEMPLATE % (json.dumps(data), schema_model_expand_depth))
        file.close()
        return
    
    def on_config(self, config):
        print("INFO    -  api-index plugin ENABLED")

    def on_pre_build(self, config):
        self.generate_page_contents()
    

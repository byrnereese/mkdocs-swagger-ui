# mkdocs-swagger-ui

A MkDocs plugin created to help developer embed API Reference documentation into a mkdocs powered website. 

The output file can be modified by editing a template file.

## Setup

Install the plugin using pip:

`pip install mkdocs-swagger-ui`

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - swagger-ui:
      spec_url: 'https://netstorage.ringcentral.com/dpw/api-reference/specs/rc-platform.yml'
      outfile: 'docs/api.md'
```

Add the CSS file to your mkdocs.yml:

```yaml
extra_css:
- https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui.css
```

### Options

- `spec_url`: Sets the URL to the Swagger specification for the RingCentral platform. This should default to the official URL. Override this for development purposes only. 
- `outfile`: The file to output. This file is typically somewhere in your docs folder. 
- `template`: The name of the template file that generates the contents of the Swagger UI generated page. This file should be located in a `tmpl` directory.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## How the plugin works

This plugin works by loading a different template and markdown file that renders a Swagger UI page in a file's place. The key to making this work is to ensure that the `outfile` plugin config value matches the filename of some file in your documentation tree, as shown below. When mkdocs encounters this file and if the file matches the `outfile` then the plugin will render a Swagger UI in place of whatever file may already be in place. In other words, the contents of the file are completed ignored, and replaced by the output of this plugin. 

```yaml
plugins:
  - swagger-ui:
      outfile: api/quick-reference.md
pages:
  - 'Home': index.md
  - 'Quick Reference': api/quick-reference.md
```

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: https://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks

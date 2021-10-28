# mkdocs-swagger-ui-html

A MkDocs plugin created to help developer embed API Reference documentation into a mkdocs powered website. API specs data will be rendered with [Swagger Editor](https://editor.swagger.io/)-like style.

## Setup

1. Install the plugin using pip:

`pip install mkdocs-swagger-ui-html`

2. Copy over `docs/api-index.md` to `docs/api-index.md` under your project (assuming your mkdocs working path is `{root}/docs`)

3. Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - swagger-ui:
      spec_url: 'https://netstorage.ringcentral.com/dpw/api-reference/specs/rc-platform.yml'
```

### Options

- `spec_url`: Sets the URL to the Swagger specification for the RingCentral platform. This should default to the official URL. Override this for development purposes only. 

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## How the plugin works

- **Input**: API specs YAML file

- **Render**: The plugin takes API specs data and generates `api-index.html`

- **Injection**: `api-index.html` file will be injected into `api-index.md` file and rendered along with other md files under the same mkdocs theme when the server is running

```yaml
plugins:
  - swagger-ui:
      outfile: api/quick-reference.md
pages:
  - 'Home': index.md
  - 'API Reference': api-index.md
```

## Additional Note
- **Warning**: mkdocs has hot loading mechanism and this plugin writes files to your local storage, so change and save files when the server is running will cause infinite hot loading issue. Please stop and restart the server before you apply any changes.

## TODO
- Add JSON API specs support

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: https://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks

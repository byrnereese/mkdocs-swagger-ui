from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-swagger-ui-html',
    version='0.1.1',
    description='An MkDocs plugin to generate a markdown file containing an API reference built using Swagger UI from a base OAS3 specification.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs swagger api documentation',
    url='https://github.com/byrnereese/mkdocs-swagger-ui/tree/StructureBreakingChange',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    license='MIT',
    python_requires='>=3.0',
    install_requires=[
        'pyyaml',
        'jinja2',
        'markdown',
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'swagger-ui-html = mkdocs_swagger_ui_plugin.plugin:SwaggerUIPlugin'
        ]
    }
)

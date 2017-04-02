from jinja2 import FileSystemLoader, Environment


class Snippyt(object):
    def __init__(self, templates_path):
        self.env = Environment(
            loader=FileSystemLoader(templates_path),
        )

    def run(self, **kwargs):
        path = kwargs.get('path', 'helloworld')
        context = kwargs.get('context', {'name': 'World'})

        t = self.env.get_template(path)
        result = t.render(**context)
        return result
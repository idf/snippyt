import os
import re

from jinja2 import FileSystemLoader, Environment, meta


class Snippyt(object):
    def __init__(self, templates_path):
        self.templates_path = templates_path
        self.env = Environment(
            loader=FileSystemLoader(self.templates_path),
        )

    def run(self, **kwargs):
        path = kwargs.get('path', 'helloworld')
        context = kwargs.get('context', {'name': 'World'})

        undeclared = self.get_undeclared(path, context)
        if undeclared:
            print("Undeclared:", " ".join(list(undeclared)))
            return self.re_render(path, context)
        else:
            return self.jinja_render(path, context)

    def jinja_render(self, path, context):
        t = self.env.get_template(path)
        result = t.render(**context)
        return result

    def get_undeclared(self, path, context):
        with open(os.path.join(self.templates_path, path)) as f:
            t = f.read()
            ast = self.env.parse(t)
            undeclared = meta.find_undeclared_variables(ast) - \
                         set(self.env.globals.keys()) - context.keys()
            return undeclared

    def re_render(self, path, context):
        with open(os.path.join(self.templates_path, path)) as f:
            t = f.read()
            for k, v in context.items():
                t = re.sub(r"\{\{\s*%s\s*\}\}" % k, v, t)

            return t
import os
import re

from jinja2 import FileSystemLoader, Environment, meta
from snippyt import templates


class Snippyt(object):
    def __init__(self):
        self.templates_path = templates.templates_dir()
        self.dot_path = os.path.join(os.path.expanduser('~'), '.snippyt')

    def run(self, **kwargs):
        filename = kwargs.get('path', 'helloworld')
        context = kwargs.get('context', {'name': 'World'})

        if os.path.exists(os.path.join(self.dot_path, filename)):
            root_path = self.dot_path
        elif os.path.exists(os.path.join(self.templates_path, filename)):
            root_path = self.templates_path
        else:
            return "Template not found"

        env = Environment(
            loader=FileSystemLoader(root_path)
        )

        # support two paths
        undeclared = self.get_undeclared(root_path, env, filename, context)
        if undeclared:
            print("Undeclared:", " ".join(list(undeclared)))
            return self.re_render(root_path, filename, context)
        else:
            return self.jinja_render(env, filename, context)

    def jinja_render(self, env, filename, context):
        t = env.get_template(filename)
        result = t.render(**context)
        return result

    def get_undeclared(self, root_path, env, filename, context):
        with open(os.path.join(root_path, filename)) as f:
            t = f.read()
            ast = env.parse(t)
            undeclared = meta.find_undeclared_variables(ast) - \
                         set(env.globals.keys()) - context.keys()
            return undeclared

    def re_render(self, root_path, filename, context):
        with open(os.path.join(root_path, filename)) as f:
            t = f.read()
            for k, v in context.items():
                t = re.sub(r"\{\{\s*%s\s*\}\}" % k, v, t)

            return t
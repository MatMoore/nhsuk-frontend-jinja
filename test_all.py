from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())


def test_checkboxes():
    template = env.get_template("test/checkbox/checkbox.j2")
    html = template.render()
    html = ""
    with (Path(__name__).parent / "templates/test/checkbox/checkbox.html").open() as f:
        expected = f.read()

    assert html == expected

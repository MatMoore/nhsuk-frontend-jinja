from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape

root = Path(__name__).parent.absolute()


@pytest.fixture
def env():
    return Environment(
        loader=FileSystemLoader(root / "templates"), autoescape=select_autoescape()
    )


def test_checkboxes(env):
    template = env.get_template("test/checkbox/checkbox.j2")
    html = template.render()
    with (root / "templates/test/checkbox/checkbox.html").open() as f:
        expected = f.read()

    pretty_html = BeautifulSoup(html, "html.parser").prettify()
    pretty_expected = BeautifulSoup(expected, "html.parser").prettify()

    assert pretty_html == pretty_expected

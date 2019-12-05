from terminology import __version__
from pathlib import Path
import toml


def test_version():
    current_file = Path(__file__)
    with open((current_file / "../../pyproject.toml").resolve()) as pyproject_toml:
        project_version = toml.loads(pyproject_toml.read())["tool"]["poetry"]["version"]
    assert __version__ == project_version

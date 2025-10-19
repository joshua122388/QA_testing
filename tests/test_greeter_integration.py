import pytest
from app.greeter import load_names_from_file, greet

pytestmark = pytest.mark.integration

def test_load_names_and_greet(tmp_path):
    # Arrange: create a small names file
    p = tmp_path / "names.txt"
    p.write_text("Grace\n\nLinus\n  Guido  \n", encoding="utf-8")

    # Act
    names = load_names_from_file(str(p))
    greetings = [greet(n) for n in names]

    # Assert
    assert names == ["Grace", "Linus", "Guido"]
    assert greetings == ["Hello, Grace!", "Hello, Linus!", "Hello, Guido!"]

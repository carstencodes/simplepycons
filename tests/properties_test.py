import pytest
import simplepycons

from ._parameters import normalized_names as parameters

instances = [simplepycons.all_icons[k] for k in parameters]

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_title(to_test: "simplepycons.Icon"):
    prop = to_test.title
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_name(to_test: "simplepycons.Icon"):
    prop = to_test.name
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_original_file_name(to_test: "simplepycons.Icon"):
    prop = to_test.original_file_name
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_primary_color(to_test: "simplepycons.Icon"):
    prop = to_test.primary_color
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_raw_svg(to_test: "simplepycons.Icon"):
    prop = to_test.raw_svg
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_svg_tree_and_svg_is_parsable(to_test: "simplepycons.Icon"):
    from xml.etree import ElementTree
    prop = to_test.svg_tree()
    assert prop is not None and isinstance(prop, ElementTree.Element)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_source(to_test: "simplepycons.Icon"):
    prop = to_test.source
    assert prop is not None and isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_source(to_test: "simplepycons.Icon"):
    prop = to_test.guidelines_url
    assert prop is None or isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_license_one(to_test: "simplepycons.Icon"):
    prop, _ = to_test.license
    assert prop is None or isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_license_two(to_test: "simplepycons.Icon"):
    _, prop = to_test.license
    assert prop is None or isinstance(prop, str)

@pytest.mark.parametrize("to_test", instances)
def test_icon_has_aliases(to_test: "simplepycons.Icon"):
    prop = to_test.aliases
    assert prop is not None
    for item in prop:
        assert item is not None and isinstance(item, str)

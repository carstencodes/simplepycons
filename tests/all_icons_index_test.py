import pytest
import simplepycons

from ._parameters import normalized_names as parameters

@pytest.mark.parametrize("key", parameters)
def test_icons_index_exists(key: "str"):
    to_test = simplepycons.all_icons
    assert key in to_test.names()

@pytest.mark.parametrize("key", parameters)
def test_icon_class_create(key: "str"):
    to_test = simplepycons.all_icons
    icon = to_test[key]
    assert isinstance(icon, simplepycons.Icon)


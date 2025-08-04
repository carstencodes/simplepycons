import pytest
import simplepycons

from ._parameters import icon_class_names as parameters

@pytest.mark.parametrize("icon_class", parameters)
def test_icon_class_exists(icon_class: "str"):
    assert hasattr(simplepycons, icon_class)

@pytest.mark.parametrize("icon_class", parameters)
def test_icon_class_create(icon_class: "str"):
    clazz = getattr(simplepycons, icon_class)
    icon = clazz()
    assert isinstance(icon, simplepycons.Icon)


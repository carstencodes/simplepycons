import pytest
import simplepycons

from ._parameters import get_method_names as parameters

@pytest.mark.parametrize("get_method", parameters)
def test_icon_class_exists(get_method: "str"):
    to_test = simplepycons.all_icons
    assert hasattr(to_test, get_method)

@pytest.mark.parametrize("get_method", parameters)
def test_icon_class_factory(get_method: "str"):
    to_test = simplepycons.all_icons
    factory = getattr(to_test, get_method)
    assert factory is not None and isinstance(factory, simplepycons.IconFactory)

@pytest.mark.parametrize("get_method", parameters)
def test_icon_class_prototype(get_method: "str"):
    to_test = simplepycons.all_icons
    factory = getattr(to_test, get_method)
    prototype = factory.prototype
    assert prototype is not None and isinstance(prototype, simplepycons.Icon)

@pytest.mark.parametrize("get_method", parameters)
def test_icon_class_invocation(get_method: "str"):
    to_test = simplepycons.all_icons
    call_fn = getattr(to_test, get_method)
    icon = call_fn()
    assert isinstance(icon, simplepycons.Icon)

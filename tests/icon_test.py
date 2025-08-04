import simplepycons

class _IconToTest(simplepycons.SimpleIconsIcon):
    pass


def test_get_uncustomizesd_svg_primary_color():
    to_test = _IconToTest()
    svg = to_test.customize_svg()
    fill = svg.get("fill")
    assert fill is not None and fill == to_test.primary_color

def test_get_customizesd_svg_fill():
    to_test = _IconToTest()
    svg = to_test.customize_svg(fill="#F0F0F0")
    fill = svg.get("fill")
    assert fill is not None and fill == "#F0F0F0"

def test_get_customizesd_svg_fill_no_rgb():
    to_test = _IconToTest()
    svg = to_test.customize_svg(fill="lime")
    fill = svg.get("fill")
    assert fill is not None and fill == "lime"

def test_get_customizesd_svg_fill_no_validation():
    to_test = _IconToTest()
    svg = to_test.customize_svg(fill="this is no valid color")
    fill = svg.get("fill")
    assert fill is not None and fill == "this is no valid color"

def test_get_uncustomizesd_svg_no_color():
    to_test = _IconToTest()
    svg = to_test.customize_svg()
    color = svg.get("color", None)
    assert color is None

def test_get_customizesd_svg_color():
    to_test = _IconToTest()
    svg = to_test.customize_svg(color="#FF00FF")
    color = svg.get("color")
    assert color is not None and color == "#FF00FF"

def test_get_uncustomizesd_svg_as_bytes():
    to_test = _IconToTest()
    svg = to_test.customize_svg_as_bytes()
    assert svg is not None and isinstance(svg, bytes)

def test_get_uncustomizesd_svg_as_data_url():
    to_test = _IconToTest()
    svg = to_test.customize_svg_as_data_url()
    
    assert svg is not None and isinstance(svg, str) and svg.startswith("data:image/svg+xml;base64, ")

def test_get_uncustomizesd_svg_as_data_url_and_can_decode():
    to_test = _IconToTest()
    svg = to_test.customize_svg_as_data_url()
    
    svg = svg[len("data:image/svg+xml;base64, "):]
    import base64
    decoded = base64.b64decode(svg)
    assert decoded is not None and isinstance(decoded, bytes)

def test_get_uncustomizesd_svg_as_data_url_and_equals_regular():
    to_test = _IconToTest()
    svg = to_test.customize_svg_as_data_url()
    
    svg = svg[len("data:image/svg+xml;base64, "):]
    import base64
    decoded = base64.b64decode(svg).decode("utf-8")
    assert decoded is not None and decoded == to_test.customize_svg_as_str()
# simplepycons

![PyPI](https://img.shields.io/pypi/v/simplepycons?logo=python&logoColor=%23cccccc) ![Simple Icons version](https://img.shields.io/badge/dynamic/regex?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcarstencodes%2Fsimplepycons%2Frefs%2Fheads%2Fmain%2F.gitmodules&search=%5C%5Bsubmodule%20%22vendor%5C%2Fsimple-icons%22%5C%5D%5B%5E%5C%5B%5D%2Bbranch%5Cs*%3D%5Cs*%28%3F%3Cversion%3E%5Cd%2B%5C.%5Cd%2B%5C.%5Cd%2B%3F%29&replace=%24%3Cversion%3E&flags=ims&label=Simple%20Icons%20version) ![Latest Simple Icons Release](https://img.shields.io/github/v/release/simple-icons/simple-icons?label=Latest%20Simple%20Icons%20Release) ![License](https://img.shields.io/github/license/carstencodes/simplepycons?label=License) [![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

Python wrappers for [simple-icons](https://github.com/simple-icons/simple-icons)
inspired by the [wonderful work of sachinraja](https://github.com/sachinraja/simple-icons-py).

As latter project seems to be no longer maintained, this project starts as being compatible to
simple-icons 13.x

## Usage

The simplepycons namespace contains the following types:

* Icon: The basic icon class, from which all Icons are inherited. It is abstract and hence cannot be inherited. 
* all_icons: A collection of all icons found.
* IconFactory: A simple wrapper providing a callable interface and a prototype.

as well as a class for each icon provided.

So, you can run:

```python
from simplepycons import all_icons, PythonIcon

icon1 = PythonIcon()
icon2 = all_icons.get_python_icon()
icon3 = all_icons["python"]
```

All calls should provide a new `Icon` instance of the python icon.

For all simple-icons, a get icon method is provided using the name of the icon.

An instance of `Icon` offers the following properties:

* name (str): The name of the icon, i.e. the name of the simple-icon id.
* original_file_name (str): The name of the file it was created from.
* title (str): The name of the brand
* primary_color (str): The primary color of the brand.
* raw_svg (str): The RAW SVG graphics as string.
* guidelines_url (str | None): The url to the usage guidelines (optional).
* license (tuple[str | None, str | None]): The license as a tuple. The first element is the SPDX identifier, the second element is the URL to the license document (optional).
* source (str): The source URL of the icon.
* aliases (Iterable[str]): A list of aliases used as alternative titles

An instance of `Icon` offers the following methods:

* svg_tree() (xml.ElementTree.Element): The SVG as XML Element
* customize_svg(**svg_attr: str) (xml.ElementTree.Element): The SVG with custom attributes on the root node.
* customize_svg_as_bytes(**svg_attr: str) (bytes): The SVG with custom attributes on the root node, converted to a bytes object.
* customize_svg_as_str(**svg_attr: str) (str): The SVG with custom attributes on the root node, converted to string.
* customize_svg_as_data_url_(**svg_attr: str) (str): The SVG with custom attributes on the root node, converted to a base64 encoded data url.

The `svg_attr` keyword arguments can be used to add any arbitrary svg attribute to the SVG root node. If `fill` is not used, the `primary_color` is used.

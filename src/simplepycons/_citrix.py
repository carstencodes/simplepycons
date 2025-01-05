#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class CitrixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "citrix"

    @property
    def original_file_name(self) -> "str":
        return "citrix.svg"

    @property
    def title(self) -> "str":
        return "Citrix"

    @property
    def primary_color(self) -> "str":
        return "#452170"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Citrix</title>
     <path d="M11.983 0a1.78 1.78 0 0 0-1.78 1.78 1.78 1.78 0 0 0 1.78
 1.78 1.78 1.78 0 0 0 1.78-1.78A1.78 1.78 0 0 0 11.983 0zM5.17
 5.991a1.026 1.026 0 0 0-1.095 1.027c0 .308.136.616.376.822l6.162
 7.086-6.401 7.258a1.084 1.084 0 0 0-.309.787c0 .582.48 1.027 1.062
 1.027.342 0 .684-.17.89-.444l6.128-7.19 6.162
 7.19c.205.274.547.444.89.444.582.035 1.062-.445 1.062-1.027a1.14 1.14
 0 0 0-.309-.787l-6.402-7.258
 6.162-7.086c.24-.206.377-.514.377-.822v-.034c0-.582-.513-1.027-1.095-.993-.343
 0-.65.171-.856.445l-5.957 7.018L6.06 6.436a1.07 1.07 0 0
 0-.855-.445z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []

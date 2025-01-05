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


class WweIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wwe"

    @property
    def original_file_name(self) -> "str":
        return "wwe.svg"

    @property
    def title(self) -> "str":
        return "WWE"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WWE</title>
     <path d="M24 1.047L15.67 18.08l-3.474-8.53-3.474 8.53L.393
 1.048l3.228 8.977 3.286 8.5C3.874 19.334 1.332 20.46 0
 21.75c.443-.168 3.47-1.24 7.409-1.927l1.21 3.129 1.552-3.518a36.769
 36.769 0 0 1 3.96-.204l1.644 3.722 1.4-3.62c2.132.145 3.861.426
 4.675.692 0 0 .92-1.962 1.338-2.866a54.838 54.838 0 0
 0-5.138-.092l2.722-7.042zm-21.84.026L8.64 13.86l3.568-9.155 3.567
 9.155 6.481-12.788-6.433 8.452-3.615-8.22-3.615 8.22zm10.036
 13.776l1.115 2.523a42.482 42.482 0 0 0-2.363.306Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:WWE_N'''

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

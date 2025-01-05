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


class AlpinedotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alpinedotjs"

    @property
    def original_file_name(self) -> "str":
        return "alpinedotjs.svg"

    @property
    def title(self) -> "str":
        return "Alpine.js"

    @property
    def primary_color(self) -> "str":
        return "#8BC0D0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alpine.js</title>
     <path d="m24 12-5.72 5.746-5.724-5.741 5.724-5.75L24 12zM5.72
 6.254 0 12l5.72 5.746h11.44L5.72 6.254z" />
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

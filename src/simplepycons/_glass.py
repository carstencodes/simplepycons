#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class GlassIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "glass"

    @property
    def original_file_name(self) -> "str":
        return "glass.svg"

    @property
    def title(self) -> "str":
        return "Glass"

    @property
    def primary_color(self) -> "str":
        return "#FFCC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Glass</title>
     <path d="M11 0v24A12 12 0 0 1 0 12 12 12 0 0 1 11 0m13 13a11 11 0
 0 1-11 11V13zm-5.5-2a1 1 0 0 0 0-11 1 1 0 0 0 0 11" />
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

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


class EaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ea"

    @property
    def original_file_name(self) -> "str":
        return "ea.svg"

    @property
    def title(self) -> "str":
        return "EA"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>EA</title>
     <path d="M16.635 6.162l-5.928
 9.377H4.24l1.508-2.3h4.024l1.474-2.335H2.264L.79 13.239h2.156L0
 17.84h12.072l4.563-7.259 1.652 2.66h-1.401l-1.473 2.299h4.347l1.473
 2.3H24zm-11.461.107L3.7 8.604l9.52-.035 1.474-2.3z" />
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

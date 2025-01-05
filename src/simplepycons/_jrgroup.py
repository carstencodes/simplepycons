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


class JrGroupIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jrgroup"

    @property
    def original_file_name(self) -> "str":
        return "jrgroup.svg"

    @property
    def title(self) -> "str":
        return "JR Group"

    @property
    def primary_color(self) -> "str":
        return "#44AF35"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JR Group</title>
     <path d="M19.955 13.653h1.089c2.684 0 2.684-4.123
 2.684-4.123s0-4.162-2.684-4.162H9.18v8.869c0 1.556-3.112 1.478-3.112
 1.478s-3.073.116-3.073-1.478v-3.423H0v4.395c0 3.19 5.68 3.384 6.107
 3.423.428 0 6.107-.194 6.107-3.423V8.363h7.896c.661 0 .661 1.167.661
 1.167s0 1.167-.66 1.167h-6.069l5.952 7.702H24Z" />
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

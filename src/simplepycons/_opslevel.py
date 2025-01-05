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


class OpslevelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opslevel"

    @property
    def original_file_name(self) -> "str":
        return "opslevel.svg"

    @property
    def title(self) -> "str":
        return "OpsLevel"

    @property
    def primary_color(self) -> "str":
        return "#0A53E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpsLevel</title>
     <path d="M21.246 4.86 13.527.411a3.074 3.074 0 0 0-3.071 0l-2.34
 1.344v6.209l3.104-1.793a1.515 1.515 0 0 1 1.544 0l3.884
 2.241c.482.282.764.78.764 1.328v4.482a1.54 1.54 0 0 1-.764
 1.328l-3.884 2.241V24l8.482-4.897a3.082 3.082 0 0 0
 1.544-2.656V7.532a3.054 3.054 0 0 0-1.544-2.672ZM6.588
 14.222V2.652L2.754 4.876A3.082 3.082 0 0 0 1.21 7.532v8.915c0
 1.095.581 2.108 1.544 2.656L11.236 24v-6.209L7.352 15.55a1.525 1.525
 0 0 1-.764-1.328Z" />
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

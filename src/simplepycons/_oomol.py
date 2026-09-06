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


class OomolIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oomol"

    @property
    def original_file_name(self) -> "str":
        return "oomol.svg"

    @property
    def title(self) -> "str":
        return "OOMOL"

    @property
    def primary_color(self) -> "str":
        return "#0D1117"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OOMOL</title>
     <path d="M17.176 14.888a.83.83 0 0 1 .832.83.83.83 0 0
 1-.832.83.83.83 0 0 1-.832-.83.83.83 0 0 1 .832-.83M6.824
 7.513a.83.83 0 0 1 .832.83.83.83 0 0 1-.832.83.83.83 0 0
 1-.832-.83.83.83 0 0 1 .832-.83M12 0c6.627 0 12 5.373 12 12s-5.373
 12-12 12S0 18.627 0 12 5.373 0 12 0M6.824 6.222c-1.174
 0-2.126.95-2.126 2.12s.952 2.121 2.126 2.121A2.13 2.13 0 0 0 8.85
 8.988h.932a1.57 1.57 0 0 1 1.571 1.567v2.95a2.86 2.86 0 0 0 2.865
 2.858h.932a2.13 2.13 0 0 0 2.026 1.475c1.174 0 2.126-.949
 2.126-2.12s-.952-2.12-2.126-2.12a2.13 2.13 0 0 0-2.026
 1.475h-.932a1.57 1.57 0 0 1-1.571-1.567v-2.95a2.86 2.86 0 0
 0-2.865-2.859H8.85a2.13 2.13 0 0 0-2.026-1.475" />
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

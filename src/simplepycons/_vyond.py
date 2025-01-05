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


class VyondIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vyond"

    @property
    def original_file_name(self) -> "str":
        return "vyond.svg"

    @property
    def title(self) -> "str":
        return "Vyond"

    @property
    def primary_color(self) -> "str":
        return "#D95E26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vyond</title>
     <path d="M1.55 16.382 0 7.616h1.328l.928
 6.18.932-6.18h1.328l-1.55 8.766H1.55zm5.486-7.61H6.022l1.166
 3.776v2.68h.924v-2.68L9.28 8.772H8.262L7.65
 11.35l-.614-2.58v.002zm5.12
 1.92c0-.324-.128-.482-.372-.482s-.37.16-.37.482v2.616c0
 .324.126.492.37.492s.372-.166.372-.492v-2.616zm-.344-1.256c.69 0
 1.144.468 1.144 1.262v2.52c0 .872-.432 1.346-1.172
 1.346s-1.162-.468-1.162-1.376v-2.52c0-.766.44-1.24
 1.19-1.24m5.032-.656v4.2l-1.344-4.2h-.896v6.456h.924v-3.944l1.316
 3.944h.936V8.772h-.936zm5.07 6.32c.508 0
 .706-.322.706-.92v-4.22c0-.72-.336-1.044-1.08-1.044h-.31v6.184h.684zM19.89
 7.616h1.924c1.504 0 2.186.784 2.186 2.408v3.912c0 1.678-.62
 2.448-2.122 2.448H19.89V7.616z" />
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

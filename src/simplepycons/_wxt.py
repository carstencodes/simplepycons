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


class WxtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wxt"

    @property
    def original_file_name(self) -> "str":
        return "wxt.svg"

    @property
    def title(self) -> "str":
        return "WXT"

    @property
    def primary_color(self) -> "str":
        return "#67D55E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WXT</title>
     <path d="M10.18 0c-2.081 0-3.807 1.608-4 3.64H4.019A4.033 4.033 0
 0 0 0 7.66v4.017h1.498a2.13 2.13 0 0 1 2.143 2.144 2.13 2.13 0 0
 1-2.143 2.143H0V24h8.036v-1.498a2.13 2.13 0 0 1 2.144-2.143 2.13 2.13
 0 0 1 2.143 2.143V24h4.018a4.03 4.03 0 0 0 4.018-4.018v-2.163C22.392
 17.627 24 15.901 24 13.821s-1.608-3.807-3.64-4V7.66a4.03 4.03 0 0
 0-4.019-4.018h-2.162C13.986 1.608 12.26 0 10.179 0m0 1.875a2.13 2.13
 0 0 1 2.143 2.143v1.498h4.018a2.13 2.13 0 0 1 2.143
 2.143v4.018h1.498a2.13 2.13 0 0 1 2.143 2.144 2.13 2.13 0 0 1-2.143
 2.143h-1.498v4.018a2.13 2.13 0 0 1-2.143
 2.143h-2.162c-.193-2.033-1.919-3.64-4-3.64s-3.806 1.607-3.998
 3.64H1.875V17.82c2.033-.192 3.64-1.918
 3.64-3.998s-1.607-3.807-3.64-4V7.66a2.13 2.13 0 0 1
 2.143-2.143h4.018V4.018a2.13 2.13 0 0 1 2.144-2.143" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/wxt-dev/wxt/blob/0d540a6df'''

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

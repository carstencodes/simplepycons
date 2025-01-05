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


class FontbaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fontbase"

    @property
    def original_file_name(self) -> "str":
        return "fontbase.svg"

    @property
    def title(self) -> "str":
        return "FontBase"

    @property
    def primary_color(self) -> "str":
        return "#3D03A7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FontBase</title>
     <path d="M23.079
 13.996c-2.702-2.771-5.702-5.703-8.105-8.103-1.62-1.621-4.284-1.621-5.943
 0-2.97 2.963-5.248 5.21-8.104 8.066a3.12 3.12 0 0 0 0 4.437 3.12 3.12
 0 0 0 4.437 0l2.2-2.2 2.2 2.2a3.12 3.12 0 0 0 4.438 0 3.12 3.12 0 0 0
 0-4.438l4.4 4.4a3.12 3.12 0 0 0 4.438 0c1.274-1.16
 1.274-3.165.039-4.362z" />
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

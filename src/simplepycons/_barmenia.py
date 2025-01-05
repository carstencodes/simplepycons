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


class BarmeniaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "barmenia"

    @property
    def original_file_name(self) -> "str":
        return "barmenia.svg"

    @property
    def title(self) -> "str":
        return "Barmenia"

    @property
    def primary_color(self) -> "str":
        return "#009FE3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Barmenia</title>
     <path d="M7.046 13.427v6.395h5.709a5.41 5.41 0 0 0
 2.377-.422c1.021-.537 1.532-1.537 1.532-2.999a2.591 2.591 0 0
 0-1.492-2.571 5.834 5.834 0 0 0-2.347-.403zm0-9.26v5.287h5.714a4.722
 4.722 0 0 0 2.486-.592c.637-.398.955-1.101.955-2.109
 0-1.117-.421-1.855-1.263-2.213a8.63 8.63 0 0
 0-2.78-.368zm12.761-1.611a6.19 6.19 0 0 1 1.079 3.66 5.433 5.433 0 0
 1-1.089 3.531 5.617 5.617 0 0 1-1.791 1.388 5.232 5.232 0 0 1 2.716
 2.113 6.474 6.474 0 0 1 .915 3.481 7.069 7.069 0 0 1-1.05 3.854 6.467
 6.467 0 0 1-4.316
 3.093c-1.093.222-2.207.33-3.322.324H2.361V0H13.72c2.864.046 4.893.899
 6.087 2.556" />
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

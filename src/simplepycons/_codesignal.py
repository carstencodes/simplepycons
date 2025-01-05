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


class CodesignalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codesignal"

    @property
    def original_file_name(self) -> "str":
        return "codesignal.svg"

    @property
    def title(self) -> "str":
        return "CodeSignal"

    @property
    def primary_color(self) -> "str":
        return "#1062FB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeSignal</title>
     <path d="M24 1.212 13.012 2.787 12 5.62l-1.01-2.833L0 1.212 3.672
 11.45l4.512.646 3.815 10.691 3.816-10.691 4.512-.646zm-3.625
 4.406-4.52.648-.73 2.044 4.517-.647-.734 2.047-4.514.647L12
 17.064l-2.393-6.707-4.514-.647-.735-2.047
 4.518.647-.73-2.044-4.52-.648-.735-2.047 6.676.956L12
 11.345l2.434-6.818 6.676-.956Z" />
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

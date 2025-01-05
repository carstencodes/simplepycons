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


class TaromIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tarom"

    @property
    def original_file_name(self) -> "str":
        return "tarom.svg"

    @property
    def title(self) -> "str":
        return "TAROM"

    @property
    def primary_color(self) -> "str":
        return "#003366"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TAROM</title>
     <path d="M12.054 0C5.424 0 .028 5.37 0 11.973 0 18.603 5.424 24
 12.054 24 18.657 24 24 18.603 24 11.973 24 5.398 18.657 0 12.054 0Zm0
 .877c2.603 0 5.068.96 6.986 2.52L7.178 15.123a21.416 21.416 0 0
 1-.75-.101c-.55-.082-.988-.147-1.552-.089-.904.082-2.135.876-2.902
 1.725a11.18 11.18 0 0 1-1.015-4.711C.959 5.864 5.917.877
 12.054.877zm7.37 2.876c2.247 2.054 3.672 4.987 3.672 8.22 0
 2.137-.549 4.055-1.59 5.753l-10.218-1.862ZM4.876 16.738c.795.028
 1.644.084 2.521.33l9.534 4.712-5.15-4.219 9.479.547c-2 3.014-5.398
 4.96-9.179 4.96-4.328 0-8.082-2.465-9.945-6.054.96-.164 1.809-.303
 2.74-.276z" />
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

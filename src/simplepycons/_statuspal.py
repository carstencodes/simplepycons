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


class StatuspalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "statuspal"

    @property
    def original_file_name(self) -> "str":
        return "statuspal.svg"

    @property
    def title(self) -> "str":
        return "Statuspal"

    @property
    def primary_color(self) -> "str":
        return "#4934BF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Statuspal</title>
     <path d="M14.275 9.296c0-1.242-1.02-2.25-2.275-2.25-1.256 0-2.275
 1.008-2.275 2.25 0 .936.58 1.737 1.403 2.077L5.934 24c1.896-1.1
 3.98-1.651 6.066-1.651 2.085 0 4.17.55 6.066 1.65l-5.194-12.626a2.251
 2.251 0 001.403-2.077zm1.187 12.01A13.44 13.44 0 0012 20.849a13.44
 13.44 0 00-3.463.457L12 13.389zM16.55 13.5a5.58 5.58 0 00-.723-7.535
 5.732 5.732 0 00-7.654 0A5.58 5.58 0 007.45 13.5a6.167 6.167 0
 01.143-8.716c2.446-2.379 6.368-2.379 8.813 0a6.167 6.167 0 01.144
 8.716zm0 3c3.047-1.988 4.416-5.716 3.366-9.174C18.867 3.867 15.65 1.5
 12 1.5c-3.65 0-6.869 2.367-7.917 5.826-1.049 3.458.32 7.186 3.367
 9.174-3.481-2.029-5.16-6.111-4.096-9.968C4.417 2.675 7.96 0 12
 0c4.042 0 7.583 2.675 8.646 6.532 1.063 3.857-.615 7.94-4.096 9.968z"
 />
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

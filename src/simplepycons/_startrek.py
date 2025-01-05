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


class StarTrekIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "startrek"

    @property
    def original_file_name(self) -> "str":
        return "startrek.svg"

    @property
    def title(self) -> "str":
        return "Star Trek"

    @property
    def primary_color(self) -> "str":
        return "#FFE200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Star Trek</title>
     <path d="M14.943 14.596c.094 0 .3.095.576.462a57.71 57.71 0 0 1
 2.165 3.23c-1.627.646-3.595 1.01-5.684 1.01-.988
 0-1.948-.097-2.856-.26 1.417-1.507 2.918-2.856
 4.703-3.98.555-.278.819-.462 1.096-.462zm2.424-6.202c2.858 1.055
 4.788 2.906 4.788 4.998 0 1.415-.881 2.73-2.338
 3.755-.385-2.26-.898-4.477-1.644-6.616a38.69 38.69 0 0
 0-.808-2.136zM7.73 8.077a38.965 38.965 0 0 0-1.096 3.288 56.361
 56.361 0 0 0-1.327 6.404c-2.11-1.1-3.462-2.69-3.462-4.385.001-2.274
 2.44-4.337 5.885-5.307zM12.463.086c-.095 0-.08-.007-.174.086a25.88
 25.88 0 0 0-3.663 5.77C3.631 6.89 0 9.887 0 13.385c0 2.588 1.991
 4.903 5.048 6.317a64.85 64.85 0 0 0-.347 4.01c0
 .094.108.202.203.202h.086c.094 0 .08.007.173-.086a79.757 79.757 0 0 1
 2.538-3.203c1.338.336 2.78.52 4.299.52 2.455 0 4.738-.48
 6.635-1.298.46.772.908 1.555 1.385 2.395 0
 .094.194.086.288.086a.175.175 0 0 0 .173-.173 69.569 69.569 0 0
 0-.346-3.088c2.369-1.42 3.865-3.45 3.865-5.682
 0-3.252-3.156-6.072-7.615-7.212a33.526 33.526 0 0
 0-3.75-6c0-.094-.078-.087-.172-.087z" />
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

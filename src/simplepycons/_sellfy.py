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


class SellfyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sellfy"

    @property
    def original_file_name(self) -> "str":
        return "sellfy.svg"

    @property
    def title(self) -> "str":
        return "Sellfy"

    @property
    def primary_color(self) -> "str":
        return "#21B352"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sellfy</title>
     <path d="M23.179.818C15.533-.273 8.406-.273.8.818-.266 8.377-.266
 15.424.8 22.946 4.511 23.491 8.22 24 12.005 24c3.748 0 7.459-.51
 11.17-1.017 1.1-7.56 1.1-14.607 0-22.165h.004zm-11.54 18.314c-2.055
 0-4.226-.689-5.179-1.199l.807-3.126c1.064.705 2.682 1.395 4.446 1.395
 1.395 0 2.24-.436 2.24-1.305
 0-.615-.435-.975-1.575-1.26l-2.279-.631c-2.416-.66-3.557-1.891-3.557-3.855
 0-2.365 1.83-4.256 5.619-4.256 1.99 0 3.973.545 5.07 1.092l-.951
 2.976c-1.104-.615-2.79-1.125-4.226-1.125-1.365 0-1.95.436-1.95 1.092
 0 .619.404.87 1.291 1.092l2.488.734c2.566.736 3.707 1.966 3.707
 3.885-.076 2.701-2.461 4.517-5.957 4.517l.006-.026z" />
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

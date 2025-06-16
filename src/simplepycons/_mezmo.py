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


class MezmoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mezmo"

    @property
    def original_file_name(self) -> "str":
        return "mezmo.svg"

    @property
    def title(self) -> "str":
        return "Mezmo"

    @property
    def primary_color(self) -> "str":
        return "#E9FF92"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mezmo</title>
     <path d="M10.537 18.084c0 1.28.578 2.176 1.926 2.176 1.025 0
 1.731-.767 2.117-1.856l3.594-10.369c.288-.862.738-1.342
 1.636-1.342.675 0 1.253.48 1.253 1.342v11.778a.17.17 0 0 0
 .195.195h2.544a.17.17 0 0 0
 .196-.195V7.965c0-2.369-1.83-4.225-4.11-4.225-2.214 0-3.69
 1.366-4.396 3.456l-1.7 4.991c-.065.195-.097.258-.196.258a.117.117 0 0
 1-.13-.129V7.965c0-2.369-1.829-4.225-4.109-4.225-2.215 0-3.69
 1.366-4.396 3.456l-1.7 4.991c-.065.195-.097.258-.196.258a.118.118 0 0
 1-.128-.129V4.187a.17.17 0 0 0-.195-.195H.198a.17.17 0 0
 0-.196.195v13.89c0 1.28.587 2.175 1.926 2.175 1.027 0 1.733-.767
 2.119-1.856L7.64 8.027c.288-.8.803-1.342 1.636-1.342.681 0 1.26.48
 1.26 1.342z" />
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

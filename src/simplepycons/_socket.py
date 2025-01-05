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


class SocketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "socket"

    @property
    def original_file_name(self) -> "str":
        return "socket.svg"

    @property
    def title(self) -> "str":
        return "Socket"

    @property
    def primary_color(self) -> "str":
        return "#C93CD7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Socket</title>
     <path d="M2.93 11.171c0 5.92 3.778 10.957 9.063 12.829a13.652
 13.652 0 0 0 6.513-4.89 13.497 13.497 0 0 0 2.564-7.939V3.274L11.997
 0 2.933 3.274v7.897zm7.491-6.09h4.208L13.34 9.47h2.292l-6.264 9.446
 1.486-6.858H8.365z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/SocketDev/vscode-socket-se'''

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

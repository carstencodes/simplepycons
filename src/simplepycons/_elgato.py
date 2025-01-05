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


class ElgatoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elgato"

    @property
    def original_file_name(self) -> "str":
        return "elgato.svg"

    @property
    def title(self) -> "str":
        return "Elgato"

    @property
    def primary_color(self) -> "str":
        return "#101010"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elgato</title>
     <path d="m13.8818 8.3964.0261.0196 9.9494 5.7172c-.4884
 2.729-1.9196 5.2223-4.0384 7.0253A11.9262 11.9262 0 0 1 12.097
 24c-3.1925 0-6.1939-1.2477-8.4527-3.5144C1.3868 18.2188.1427
 15.2044.1427 12c0-3.2042 1.244-6.2187 3.5015-8.4854C5.9019 1.248
 8.9032 0 12.097 0c2.4394 0 4.7847.7333 6.783 2.1187 1.9526 1.354
 3.4466 3.2357 4.3227 5.4422.1112.2829.2149.5736.3051.8657l-2.1255
 1.2359a9.4924 9.4924 0 0
 0-.2619-.8694c-1.354-3.8303-4.9813-6.4048-9.0237-6.4048C6.8171 2.3883
 2.522 6.7005 2.522 12c0 5.2995 4.295 9.6115 9.5748 9.6115 2.052 0
 4.0084-.6442 5.6596-1.8647 1.6172-1.1955 2.8036-2.8337
 3.4309-4.7364l.0065-.0419L9.5906 8.3048v7.2256l4.0004-2.3138 2.06
 1.1811-5.9962 3.4688-2.12-1.2126V7.1943l2.1174-1.2245 4.2309
 2.4279-.0013-.0013" />
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

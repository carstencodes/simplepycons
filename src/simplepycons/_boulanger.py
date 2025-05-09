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


class BoulangerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "boulanger"

    @property
    def original_file_name(self) -> "str":
        return "boulanger.svg"

    @property
    def title(self) -> "str":
        return "boulanger"

    @property
    def primary_color(self) -> "str":
        return "#FD5300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>boulanger</title>
     <path d="M8.405 3.612v3.5777h5.6616c2.987.0347 5.3836 2.4311
 5.3836 5.4181-.0347 2.987-2.4313 5.3834-5.3836 5.4181h-3.1259c-2.987
 0-5.4181-2.431-5.4181-5.418V8.4052c0-2.084 1.1458-3.8903
 2.8824-4.7933zC3.7856 3.612 0 7.3975 0 12.017c0 4.6194 3.7162 8.371
 8.3704 8.371h7.2592C20.249 20.388 24 16.6711 24
 12.017c0-4.6542-3.6815-8.405-8.3704-8.405zm.0353 6.4255v2.5357c0
 1.3893 1.1457 2.535 2.535 2.535h3.0222c1.3893 0 2.535-1.1457
 2.535-2.535 0-1.3893-1.111-2.5357-2.535-2.5357z" />
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

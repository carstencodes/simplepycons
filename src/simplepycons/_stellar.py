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


class StellarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stellar"

    @property
    def original_file_name(self) -> "str":
        return "stellar.svg"

    @property
    def title(self) -> "str":
        return "Stellar"

    @property
    def primary_color(self) -> "str":
        return "#7D00FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stellar</title>
     <path d="M12.283 1.851A10.154 10.154 0 001.846 12.002c0
 .259.01.516.03.773A1.847 1.847 0 01.872 14.56L0
 15.005v2.074l2.568-1.309.832-.424.82-.417 14.71-7.496 1.653-.842L24
 4.85V2.776l-3.387 1.728-2.89 1.473-13.955 7.108a8.376 8.376 0
 01-.07-1.086 8.313 8.313 0 0112.366-7.247l1.654-.843.247-.126a10.154
 10.154 0 00-5.682-1.932zM24 6.925L5.055 16.571l-1.653.844L0
 19.15v2.072L3.378 19.5l2.89-1.473 13.97-7.117a8.474 8.474 0 01.07
 1.092A8.313 8.313 0 017.93 19.248l-.101.054-1.793.914a10.154 10.154 0
 0016.119-8.214c0-.26-.01-.522-.03-.78a1.848 1.848 0 011.003-1.785L24
 8.992Z" />
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

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


class BroadcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "broadcom"

    @property
    def original_file_name(self) -> "str":
        return "broadcom.svg"

    @property
    def title(self) -> "str":
        return "Broadcom"

    @property
    def primary_color(self) -> "str":
        return "#E31837"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Broadcom</title>
     <path d="M12 0c6.628 0 12 5.372 12 12a12 12 0 0 1-.56 3.63 13.641
 13.641 0 0 0-.867-.388c-1.372-.546-2.629-.363-3.888.4 0
 0-.459.28-.597.366-.586.37-1.14.717-1.672.717-.508
 0-1.007-.135-1.218-1.117-.33-1.533-1.135-5.298-1.486-7.162-.206-1.097-.319-1.688-.436-2.088-.208-.706-.586-1.09-1.124-1.15
 0 0-.084-.013-.152-.013-.068
 0-.162.014-.162.014-.531.064-.907.447-1.114 1.15-.117.4-.23.99-.436
 2.087-.351 1.864-1.156 5.63-1.486 7.162-.21.982-.71 1.117-1.218
 1.117-.531
 0-1.086-.348-1.672-.717-.138-.086-.597-.366-.597-.366-1.259-.763-2.516-.946-3.888-.4-.301.12-.586.251-.867.387A11.995
 11.995 0 0 1 0 12C0 5.372 5.372 0 12 0m8.375
 16.976c-.453.152-.855.42-1.256.672-.756.475-1.613 1.014-2.704
 1.014-1.614 0-2.749-.964-3.112-2.647C13.023 14.712 12 9.793 12
 9.793a496.28 496.28 0 0 1-1.303 6.222c-.362 1.683-1.497 2.647-3.112
 2.647-1.09
 0-1.946-.539-2.703-1.014-.401-.252-.804-.52-1.256-.672a2.319 2.319 0
 0 0-1.414-.01c-.33.097-.644.234-.951.386C3.227 21.292 7.207 24 11.91
 24s8.863-2.708 10.83-6.648a5.958 5.958 0 0 0-.95-.386 2.322 2.322 0 0
 0-1.415.01" />
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

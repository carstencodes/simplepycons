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


class IpfsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ipfs"

    @property
    def original_file_name(self) -> "str":
        return "ipfs.svg"

    @property
    def title(self) -> "str":
        return "IPFS"

    @property
    def primary_color(self) -> "str":
        return "#65C2CB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IPFS</title>
     <path d="M12 0L1.608 6v12L12 24l10.392-6V6zm-1.073 1.445h.001a1.8
 1.8 0 002.138 0l7.534 4.35a1.794 1.794 0 000 .403l-7.535 4.35a1.8 1.8
 0 00-2.137 0l-7.536-4.35a1.795 1.795 0 000-.402zM21.324
 7.4c.109.08.226.147.349.201v8.7a1.8 1.8 0 00-1.069 1.852l-7.535
 4.35a1.8 1.8 0 00-.349-.2l-.009-8.653a1.8 1.8 0
 001.07-1.851zm-18.648.048l7.535 4.35a1.8 1.8 0 001.069
 1.852v8.7c-.124.054-.24.122-.349.202l-7.535-4.35a1.8 1.8 0
 00-1.069-1.852v-8.7c.124-.054.24-.122.35-.202z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ipfs-inactive/logo/tree/73'''

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

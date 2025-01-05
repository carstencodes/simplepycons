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


class BlockchaindotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "blockchaindotcom"

    @property
    def original_file_name(self) -> "str":
        return "blockchaindotcom.svg"

    @property
    def title(self) -> "str":
        return "Blockchain.com"

    @property
    def primary_color(self) -> "str":
        return "#121D33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Blockchain.com</title>
     <path d="M19.8285 6.6117l-5.52-5.535a3.1352 3.1352 0 00-4.5
 0l-5.535 5.535 7.755 3.87zm2.118 2.235l1.095 1.095a3.12 3.12 0 010
 4.5L14.22 23.3502a2.6846 2.6846 0 01-.72.525V13.0767zm-19.893
 0l-1.095 1.095a3.1198 3.1198 0 000 4.5L9.78
 23.3502c.2091.214.4525.3914.72.525V13.0767z" />
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

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


class BnbChainIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bnbchain"

    @property
    def original_file_name(self) -> "str":
        return "bnbchain.svg"

    @property
    def title(self) -> "str":
        return "BNB Chain"

    @property
    def primary_color(self) -> "str":
        return "#F0B90B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BNB Chain</title>
     <path d="M5.631 3.676 12.001 0l6.367 3.676-2.34 1.358L12 2.716
 7.972 5.034l-2.34-1.358Zm12.737 4.636-2.34-1.358L12 9.272 7.972
 6.954l-2.34 1.358v2.716l4.026 2.318v4.636L12
 19.341l2.341-1.359v-4.636l4.027-2.318V8.312Zm0 7.352v-2.716l-2.34
 1.358v2.716l2.34-1.358Zm1.663.96-4.027
 2.318v2.717l6.368-3.677V10.63l-2.34 1.358v4.636Zm-2.34-10.63 2.34
 1.358v2.716l2.341-1.358V5.994l-2.34-1.358-2.342 1.358ZM9.657
 19.926v2.716L12 24l2.341-1.358v-2.716l-2.34
 1.358-2.343-1.358Zm-4.027-4.262 2.341
 1.358v-2.716l-2.34-1.358v2.716Zm4.027-9.67L12
 7.352l2.341-1.358-2.34-1.358-2.343 1.358Zm-5.69 1.358L6.31 5.994
 3.968 4.636l-2.34 1.358V8.71l2.34 1.358V7.352Zm0
 4.636-2.34-1.358v7.352l6.368 3.677v-2.717l-4.028-2.318v-4.636Z" />
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

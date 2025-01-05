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


class JsonWebTokensIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jsonwebtokens"

    @property
    def original_file_name(self) -> "str":
        return "jsonwebtokens.svg"

    @property
    def title(self) -> "str":
        return "JSON Web Tokens"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JSON Web Tokens</title>
     <path d="M10.2 0v6.456L12 8.928l1.8-2.472V0zm3.6
 6.456v3.072l2.904-.96L20.52 3.36l-2.928-2.136zm2.904 2.112l-1.8 2.496
 2.928.936 6.144-1.992-1.128-3.432zM17.832 12l-2.928.936 1.8 2.496
 6.144 1.992 1.128-3.432zm-1.128 3.432l-2.904-.96v3.072l3.792 5.232
 2.928-2.136zM13.8 17.544L12 15.072l-1.8 2.472V24h3.6zm-3.6
 0v-3.072l-2.904.96L3.48 20.64l2.928
 2.136zm-2.904-2.112l1.8-2.496L6.168 12 .024 13.992l1.128 3.432zM6.168
 12l2.928-.936-1.8-2.496-6.144-1.992-1.128
 3.432zm1.128-3.432l2.904.96V6.456L6.408 1.224 3.48 3.36Z" />
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

#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class BitwardenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitwarden"

    @property
    def original_file_name(self) -> "str":
        return "bitwarden.svg"

    @property
    def title(self) -> "str":
        return "Bitwarden"

    @property
    def primary_color(self) -> "str":
        return "#175DDC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitwarden</title>
     <path d="M3.75 0A3.75 3.75 0 000 3.75v16.5A3.75 3.75 0 003.75
 24h16.5A3.75 3.75 0 0024 20.25V3.75A3.75 3.75 0 0020.25 0zm1.36
 2.92h13.8c.208 0 .388.076.54.228a.737.737 0 01.227.539v9.2c0
 .687-.134 1.367-.401 2.042a7.618 7.618 0 01-.995 1.797 11.097 11.097
 0 01-1.413 1.528c-.547.495-1.052.906-1.515
 1.234-.464.327-.947.636-1.45.928-.503.291-.86.489-1.072.593-.212.104-.381.184-.51.24a.687.687
 0 01-.31.071.688.688 0 01-.312-.072 13.784 13.784 0 01-.51-.24 20.61
 20.61 0 01-1.071-.592 19.133 19.133 0 01-1.45-.928 16.457 16.457 0
 01-1.515-1.234 11.11 11.11 0 01-1.414-1.528 7.617 7.617 0
 01-.994-1.797 5.502 5.502 0
 01-.401-2.042v-9.2c0-.208.076-.387.227-.54a.737.737 0 01.54-.227zm6.9
 2.3v13.62c.95-.502 1.801-1.05 2.552-1.64 1.877-1.47 2.815-2.907
 2.815-4.313V5.22Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/bitwarden/brand/blob/6182c'''

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

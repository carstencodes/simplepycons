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


class MoneroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "monero"

    @property
    def original_file_name(self) -> "str":
        return "monero.svg"

    @property
    def title(self) -> "str":
        return "Monero"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Monero</title>
     <path d="M12 0C5.365 0 0 5.373 0 12.015c0 1.335.228 2.607.618
 3.81h3.577V5.729L12
 13.545l7.805-7.815v10.095h3.577c.389-1.203.618-2.475.618-3.81C24
 5.375 18.635 0 12 0zm-1.788 15.307l-3.417-3.421v6.351H1.758C3.87
 21.689 7.678 24 12 24s8.162-2.311 10.245-5.764h-5.04v-6.351l-3.386
 3.421-1.788 1.79-1.814-1.79h-.005z" />
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

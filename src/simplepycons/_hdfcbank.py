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


class HdfcBankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hdfcbank"

    @property
    def original_file_name(self) -> "str":
        return "hdfcbank.svg"

    @property
    def title(self) -> "str":
        return "HDFC Bank"

    @property
    def primary_color(self) -> "str":
        return "#004B8D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HDFC Bank</title>
     <path d="M.572 0v10.842h3.712V4.485h6.381V0Zm12.413
 0v4.485h6.383v6.357h4.06V0Zm-4.64 8.53v6.938h6.963V8.53ZM.572
 13.153V24h10.093v-4.486h-6.38v-6.361zm18.796
 0v6.361h-6.383V24h10.443V13.153Z" />
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
        yield from [
            "HDB",
        ]

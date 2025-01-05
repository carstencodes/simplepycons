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


class EthersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ethers"

    @property
    def original_file_name(self) -> "str":
        return "ethers.svg"

    @property
    def title(self) -> "str":
        return "Ethers"

    @property
    def primary_color(self) -> "str":
        return "#2535A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ethers</title>
     <path d="M24 17.443c-12.547 1.64-21.503 3.61-21.636-4.474 0 0
 .274-3.133 4.116-3.33 0 0 .13-2.782 3.065-3.097 1.578-.171 3.37 1.454
 3.565 3.165 0 0 3.883-.719 4.051 3.067.059 1.32-.238 3.563-3.983
 3.465 0 0-2.167-.294-2.461-3.644-.61 6.485 8.767 6.108
 8.902.218.06-2.547-1.572-5.167-5.246-4.676-2.014-5.066-7.375-4.775-9.37-.076-2.854
 0-5.035 2.196-5.003 5.064.11 9.23 12.954 6.447 24 4.318Z" />
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

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


class TypoThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "typo3"

    @property
    def original_file_name(self) -> "str":
        return "typo3.svg"

    @property
    def title(self) -> "str":
        return "TYPO3"

    @property
    def primary_color(self) -> "str":
        return "#FF8700"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TYPO3</title>
     <path d="M18.08 16.539c-.356.105-.64.144-1.012.144-3.048
 0-7.524-10.652-7.524-14.197 0-1.305.31-1.74.745-2.114C6.56.808 2.082
 2.177.651 3.917c-.31.436-.497 1.12-.497 1.99C.154 11.442 6.06 24
 10.228 24c1.928 0 5.178-3.168 7.852-7.46M16.134 0c3.855 0 7.713.622
 7.713 2.798 0 4.415-2.8 9.765-4.23 9.765-2.549
 0-5.72-7.09-5.72-10.635C13.897.31 14.518 0 16.134 0" />
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

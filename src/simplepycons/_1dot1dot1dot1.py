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


class OneDotOneDotOneDotOneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "1dot1dot1dot1"

    @property
    def original_file_name(self) -> "str":
        return "1dot1dot1dot1.svg"

    @property
    def title(self) -> "str":
        return "1.1.1.1"

    @property
    def primary_color(self) -> "str":
        return "#221E68"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>1.1.1.1</title>
     <path d="M5.389 0A5.377 5.377 0 0 0 0 5.389V18.61A5.377 5.377 0 0
 0 5.389 24H18.61A5.377 5.377 0 0 0 24 18.611V5.39A5.377 5.377 0 0 0
 18.611 0Zm11.546
 4.595h.942v3.122h.69v.868h-.69v1.201h-1.001V8.585H14.68v-.964zm-6.07.589h2.523v14.842h-3.094V9.79H6.68V7.805c.95-.042
 1.616-.103 1.997-.184.606-.13 1.1-.39
 1.48-.779.26-.266.457-.62.592-1.064.077-.267.116-.464.116-.594Zm5.989.73L15.513
 7.72h1.365V5.915Z" />
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

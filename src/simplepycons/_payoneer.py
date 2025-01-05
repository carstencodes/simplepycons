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


class PayoneerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "payoneer"

    @property
    def original_file_name(self) -> "str":
        return "payoneer.svg"

    @property
    def title(self) -> "str":
        return "Payoneer"

    @property
    def primary_color(self) -> "str":
        return "#FF4800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Payoneer</title>
     <path d="M1.474 3.31c.234 1.802 1.035 5.642 1.398
 7.263.095.459.201.853.298 1.013.501.865.907-.287.907-.287C5.644 6.616
 3.17 3.597 2.38
 2.787c-.139-.15-.384-.332-.608-.396-.32-.095-.374.086-.374.236.01.148.065.565.075.682zm21.835-1.463c.31.224
 1.386 1.355 0 1.526-1.984.234-5.76.373-12.022 5.61C8.92 10.968 3.607
 16.311.76 22.957a.181.181 0
 01-.216.106c-.255-.074-.714-.352-.48-1.418.32-1.44 3.201-8.938
 10.817-15.552 2.485-2.155 8.416-7.232 12.426-4.245z" />
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

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


class LabexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "labex"

    @property
    def original_file_name(self) -> "str":
        return "labex.svg"

    @property
    def title(self) -> "str":
        return "LabEx"

    @property
    def primary_color(self) -> "str":
        return "#2E7EEE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LabEx</title>
     <path d="M17.2 0a1.2 1.2 0 0 1 1.2 1.2v4a1.2 1.2 0 0 1-1.2
 1.2h-.402v1.212l6.976 9.687a1.2 1.2 0 0 1 .22.576L24 18v4.8a1.2 1.2 0
 0 1-1.2 1.2H1.2A1.2 1.2 0 0 1 0
 22.8V18c0-.252.08-.497.226-.701l6.975-9.687V6.4H6.8a1.2 1.2 0 0
 1-1.194-1.084L5.6 5.2v-4A1.2 1.2 0 0 1 6.8 0zM16 2.4H8V4h.4a1.2 1.2 0
 0 1 1.195 1.084l.006.116v2.703c0 .315-.1.622-.283.877L2.4
 18.386V21.6h19.2v-3.213L14.681 8.78a1.5 1.5 0 0
 1-.277-.743l-.006-.134V5.2a1.2 1.2 0 0 1 1.2-1.2H16zm-.48 14.4a1.2
 1.2 0 0 1 0 2.4h-2.88a1.2 1.2 0 0 1 0-2.4zm-6.137-4.449 2.135
 2.135a1.2 1.2 0 0 1 0 1.697l-2.135 2.135a1.2 1.2 0 1
 1-1.697-1.697l1.286-1.286-1.286-1.286a1.2 1.2 0 0
 1-.078-1.612l.078-.086a1.2 1.2 0 0 1 1.697 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://labex.io/questions/labex-logo-guideli'''
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

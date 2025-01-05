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


class AmericanAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "americanairlines"

    @property
    def original_file_name(self) -> "str":
        return "americanairlines.svg"

    @property
    def title(self) -> "str":
        return "American Airlines"

    @property
    def primary_color(self) -> "str":
        return "#0078D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>American Airlines</title>
     <path d="M0 .244h3.264c1.377 0 1.942.563 2.499 1.116.637.58 2.57
 3.196 6.657 8.303H7.997c-1.809 0-2.38-.308-3.08-1.375zm10.424
 17.072l-2.427-4.013c-.292-.455-.372-.854-.372-1.318 0-.51.217-.79
 1.053-1.233.973-.466 2.933-.67 4.954-.67 3.283 0 4.07 1.055 4.405
 2.192 0 0-.464-.185-1.554-.185-3.459 0-6.223 1.68-6.223 4.221 0
 .534.164 1.006.164 1.006zm4.936-3.417c-2.547.089-5.032 1.869-4.936
 3.416l2.7 4.486c.836 1.344 2.215 1.955 3.932
 1.955H24l-8.13-9.852a5.55 5.55 0 0 0-.51-.005Z" />
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

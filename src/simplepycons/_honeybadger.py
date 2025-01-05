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


class HoneybadgerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "honeybadger"

    @property
    def original_file_name(self) -> "str":
        return "honeybadger.svg"

    @property
    def title(self) -> "str":
        return "Honeybadger"

    @property
    def primary_color(self) -> "str":
        return "#EA5937"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Honeybadger</title>
     <path d="M11.999 0c-.346 0-.691.131-.955.395L.394 11.045a1.35
 1.35 0 0 0 0 1.91l6.243 6.24.915-1.95L2.306 12l9.693-9.693 1.158
 1.157 1.432-1.432L12.954.395A1.346 1.346 0 0 0 11.999 0Zm5.54
 1.106a.331.331 0 0 0-.218.102l-1.777 1.778-1.432 1.432-8.393
 8.392h4.726l-3.76
 9.26c-.139.34.29.626.55.366l1.321-1.32v-.001l1.432-1.432h.001l8.56-8.561h-4.727l2.083-4.91v.001l.854-2.012
 1.112-2.623c.108-.256-.108-.485-.333-.472Zm.25 4.125-.853 2.012 4.756
 4.756L12 21.693l-1.056-1.055-1.432 1.432 1.533 1.534a1.35 1.35 0 0 0
 1.91 0l10.65-10.65a1.35 1.35 0 0 0 0-1.91z" />
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

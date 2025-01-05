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


class NamesiloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "namesilo"

    @property
    def original_file_name(self) -> "str":
        return "namesilo.svg"

    @property
    def title(self) -> "str":
        return "NameSilo"

    @property
    def primary_color(self) -> "str":
        return "#031B4E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NameSilo</title>
     <path d="M4.65 0A4.65 4.65 0 0 0 0 4.65v14.7A4.65 4.65 0 0 0 4.65
 24h14.7A4.65 4.65 0 0 0 24 19.35V4.65A4.65 4.65 0 0 0 19.35 0Zm7.21
 4.2 4.64 3.048V8.86h-.006c-.124.4-2.156.718-4.644.718S7.33 9.26 7.206
 8.86H7.2V7.248ZM7.2 9.384c0 .5 2.082.906 4.65.906 2.568 0 4.65-.406
 4.65-.906v2.587c0 .5-2.082.905-4.65.905-2.568
 0-4.65-.405-4.65-.905zm0 3.3c0 .5 2.082.906 4.65.906 2.568 0
 4.65-.405 4.65-.905v2.586c0 .5-2.082.906-4.65.906-2.568
 0-4.65-.406-4.65-.906zm0 3.301c0 .5 2.082.906 4.65.906 2.568 0
 4.65-.406 4.65-.906v2.587c0 .5-2.082.906-4.65.906-2.568
 0-4.65-.406-4.65-.906z" />
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

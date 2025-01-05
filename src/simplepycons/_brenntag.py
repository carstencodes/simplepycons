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


class BrenntagIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "brenntag"

    @property
    def original_file_name(self) -> "str":
        return "brenntag.svg"

    @property
    def title(self) -> "str":
        return "Brenntag"

    @property
    def primary_color(self) -> "str":
        return "#1A0033"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Brenntag</title>
     <path d="M19.7305 12.01c-.768.959-1.899 1.8775-3.2745 2.421.828
 1.02 1.246 2.156.9445 3.337-.2875 1.1275-1.3655 2.228-2.9
 2.228H6.5v-5.999h7c3.86 0 7-3.1395 7-6.9985S17.36 0 13.5
 0h-11v8.998h4V3.999h7c1.655 0 3 1.3445 3 2.9995s-1.345 2.9995-3
 2.9995h-11V24h12c3.86 0 7-3.1395 7-6.9985
 0-1.712-.4815-3.634-1.7695-4.9915" />
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

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


class RssIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rss"

    @property
    def original_file_name(self) -> "str":
        return "rss.svg"

    @property
    def title(self) -> "str":
        return "RSS"

    @property
    def primary_color(self) -> "str":
        return "#FFA500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RSS</title>
     <path d="M19.199 24C19.199 13.467 10.533 4.8 0 4.8V0c13.165 0 24
 10.835 24 24h-4.801zM3.291 17.415c1.814 0 3.293 1.479 3.293 3.295 0
 1.813-1.485 3.29-3.301 3.29C1.47 24 0 22.526 0 20.71s1.475-3.294
 3.291-3.295zM15.909
 24h-4.665c0-6.169-5.075-11.245-11.244-11.245V8.09c8.727 0 15.909
 7.184 15.909 15.91z" />
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

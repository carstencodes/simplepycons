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


class EmberdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "emberdotjs"

    @property
    def original_file_name(self) -> "str":
        return "emberdotjs.svg"

    @property
    def title(self) -> "str":
        return "Ember.js"

    @property
    def primary_color(self) -> "str":
        return "#E04E39"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ember.js</title>
     <path d="M0 0v24h24V0H0zm12.29 4.38c1.66-.03 2.83.42 3.84 1.85
 2.25 5.58-6 8.4-6 8.4s-.23 1.48 2.02 1.42c2.78 0 5.7-2.15
 6.81-3.06a.66.66 0 01.9.05l.84.87a.66.66 0 01.01.9c-.72.8-2.42
 2.46-4.97 3.53 0 0-4.26 1.97-7.13.1a4.95 4.95 0
 01-2.38-3.83s-2.08-.11-3.42-.63c-1.33-.52.01-2.1.01-2.1s.42-.65 1.2 0
 2.24.36 2.24.36c.13-1.03.35-2.38.98-3.81 1.34-3 3.38-4.01
 5.05-4.05zm.33 2.8c-1.1.07-2.8 1.78-2.88 4.93 0 0 .75.23 2.41-.91
 1.67-1.14 2-2.97 1.11-3.81a.82.82 0 00-.64-.21Z" />
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

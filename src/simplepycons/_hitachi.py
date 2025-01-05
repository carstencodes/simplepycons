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


class HitachiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hitachi"

    @property
    def original_file_name(self) -> "str":
        return "hitachi.svg"

    @property
    def title(self) -> "str":
        return "Hitachi"

    @property
    def primary_color(self) -> "str":
        return "#E60027"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hitachi</title>
     <path d="M17.787 11.41h-1.026a.852.852 0 00-.052-.284.714.714 0
 00-.459-.427 1.417 1.417 0 00-.913.019.89.89 0 00-.535.542 2.318
 2.318 0 00-.04 1.425.88.88 0 00.535.584 1.492 1.492 0
 00.977.027.705.705 0 00.428-.384.976.976 0 00.08-.396h1.031a2.198
 2.198 0 01-.049.351c-.09.365-.346.672-.684.814a3.254 3.254 0
 01-2.251.104c-.477-.15-.89-.493-1.054-.96a2.375 2.375 0
 01-.133-.788c0-.388.068-.764.254-1.077.192-.321.486-.569.842-.701a3.062
 3.062 0 012.318.063 1.2 1.2 0
 01.698.853c.017.076.028.156.033.235zm-3.979
 2.436H12.72l-.32-.793h-1.834c-.001.001-.315.794-.319.793h-1.09l1.727-3.693c0
 .002 1.199 0 1.199 0l1.725 3.693zm5.483.001h-.977s.005-3.693
 0-3.693h.977v1.477h1.976c0 .005-.002-1.478 0-1.477h.979s.003 3.686 0
 3.693h-.979v-1.626c0 .005-1.976 0-1.976 0 .002.007 0 1.624 0
 1.626zm-18.312 0H0s.005-3.693 0-3.693h.979s-.002 1.487 0
 1.477h1.976c0 .005-.004-1.478 0-1.477h.978s.004 3.686 0
 3.693h-.978v-1.626c0 .005-1.976 0-1.976 0 0 .007-.002 1.625 0
 1.626zm7.531-.001h-.977v-3.065H6.036s.002-.626 0-.627c.002.001 3.971
 0 3.971
 0v.627H8.51v3.065zm-3.801-3.692h.977v3.692h-.977v-3.692zm18.312
 0H24v3.692h-.979v-3.692zm-11.537.627l-.681 1.68h1.361l-.68-1.68z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Hitac'''

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

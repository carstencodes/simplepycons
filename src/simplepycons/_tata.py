#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class TataIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tata"

    @property
    def original_file_name(self) -> "str":
        return "tata.svg"

    @property
    def title(self) -> "str":
        return "Tata"

    @property
    def primary_color(self) -> "str":
        return "#486AAE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tata</title>
     <path d="M9.774
 11.568c.193-1.322.168-2.013-1.768-1.906-2.223.124-4.476.265-7.849
 1.027A5.63 5.63 0 0 0 0 12c0 1.52.618 2.99 1.787 4.254 1.06 1.144
 2.556 2.095 4.326 2.752a15.48 15.48 0 0 0
 2.014.588c.13-.527.959-3.907
 1.616-7.823l.03-.202m14.07-.88c-3.372-.762-5.624-.902-7.846-1.026-1.937-.107-1.962.584-1.768
 1.906l.046.298c.65 3.848 1.458 7.16 1.598 7.72C20.595 18.508 24
 15.516 24 12c0-.443-.054-.88-.157-1.311m-.491-1.324a7.163 7.163 0 0
 0-1.14-1.618c-1.06-1.144-2.555-2.095-4.325-2.752-1.784-.662-3.82-1.011-5.887-1.011-2.068
 0-4.103.35-5.887 1.01-1.77.658-3.266 1.61-4.326 2.753A7.17 7.17 0 0 0
 .648 9.366c2.304-.557 6.245-1.293
 9.904-1.37.353-.008.596.105.756.307.196.248.18 1.128.175 1.522l-.104
 10.18a18.507 18.507 0 0 0 1.244
 0l-.104-10.18c-.005-.394-.02-1.274.175-1.522.16-.202.403-.315.756-.308
 3.658.078 7.597.813 9.902 1.37z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.tatasteel.com/media/media-kit/log'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.tatasteel.com/media/media-kit/log'''

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
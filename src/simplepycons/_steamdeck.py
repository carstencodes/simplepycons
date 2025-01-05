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


class SteamDeckIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "steamdeck"

    @property
    def original_file_name(self) -> "str":
        return "steamdeck.svg"

    @property
    def title(self) -> "str":
        return "Steam Deck"

    @property
    def primary_color(self) -> "str":
        return "#1A9FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Steam Deck</title>
     <path d="M8.999 0v4.309c4.242 0 7.694 3.45 7.694 7.691s-3.452
 7.691-7.694 7.691V24c6.617 0 12-5.383 12-12s-5.383-12-12-12Zm0
 6.011c-3.313 0-6 2.687-5.998 6a5.999 5.999 0 1 0 5.998-6z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://partner.steamgames.com/doc/marketing/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partner.steamgames.com/doc/marketing/'''

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

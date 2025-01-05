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


class TwitchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "twitch"

    @property
    def original_file_name(self) -> "str":
        return "twitch.svg"

    @property
    def title(self) -> "str":
        return "Twitch"

    @property
    def primary_color(self) -> "str":
        return "#9146FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Twitch</title>
     <path d="M11.571 4.714h1.715v5.143H11.57zm4.715
 0H18v5.143h-1.714zM6 0L1.714
 4.286v15.428h5.143V24l4.286-4.286h3.428L22.286 12V0zm14.571
 11.143l-3.428 3.428h-3.429l-3 3v-3H6.857V1.714h13.714Z" />
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

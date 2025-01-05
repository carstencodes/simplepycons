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


class LastdotfmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lastdotfm"

    @property
    def original_file_name(self) -> "str":
        return "lastdotfm.svg"

    @property
    def title(self) -> "str":
        return "Last.fm"

    @property
    def primary_color(self) -> "str":
        return "#D51007"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Last.fm</title>
     <path d="M10.584 17.21l-.88-2.392s-1.43 1.594-3.573 1.594c-1.897
 0-3.244-1.649-3.244-4.288 0-3.382 1.704-4.591 3.381-4.591 2.42 0
 3.189 1.567 3.849 3.574l.88 2.749c.88 2.666 2.529 4.81 7.285 4.81
 3.409 0 5.718-1.044 5.718-3.793
 0-2.227-1.265-3.381-3.63-3.931l-1.758-.385c-1.21-.275-1.567-.77-1.567-1.595
 0-.934.742-1.484 1.952-1.484 1.32 0 2.034.495 2.144
 1.677l2.749-.33c-.22-2.474-1.924-3.492-4.729-3.492-2.474
 0-4.893.935-4.893 3.932 0 1.87.907 3.051 3.189 3.601l1.87.44c1.402.33
 1.869.907 1.869 1.704 0 1.017-.99 1.43-2.86 1.43-2.776
 0-3.93-1.457-4.59-3.464l-.907-2.75c-1.155-3.573-2.997-4.893-6.653-4.893C2.144
 5.333 0 7.89 0 12.233c0 4.18 2.144 6.434 5.993 6.434 3.106 0
 4.591-1.457 4.591-1.457z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Lastf'''

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

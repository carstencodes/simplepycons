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


class WpRocketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wprocket"

    @property
    def original_file_name(self) -> "str":
        return "wprocket.svg"

    @property
    def title(self) -> "str":
        return "WP Rocket"

    @property
    def primary_color(self) -> "str":
        return "#F56640"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WP Rocket</title>
     <path d="M3.723.666c-.08-.276.08-.47.356-.47h2.283c.16 0
 .31.137.356.274L8.393 7.07h.08L11.491.218A.374.374 0 0111.824
 0h.356c.172 0 .287.092.333.218l3.018 6.85h.08L17.286.47a.397.397 0
 01.356-.275h2.284c.275 0 .424.195.355.47l-3.683 13.082a.369.369 0
 01-.356.275h-.31a.38.38 0 01-.333-.218l-3.568-7.963h-.058l-3.545
 7.963a.403.403 0 01-.333.218h-.31a.379.379 0
 01-.356-.275L3.723.666m8.308 7.917l-2.594 5.818a1.663 1.663 0
 01-.344.448v.004a1.466 1.466 0 01-.688.34l1.4
 8.687c.091.16.263.16.367 0l1.79-2.72 1.64 2.708c.104.16.265.16.368
 0l1.584-8.698a1.5 1.5 0 01-.832-.618l-.02-.03a1.405 1.405 0
 01-.066-.12l-.609-1.366h-.003Z" />
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

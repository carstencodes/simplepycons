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


class LvglIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lvgl"

    @property
    def original_file_name(self) -> "str":
        return "lvgl.svg"

    @property
    def title(self) -> "str":
        return "LVGL"

    @property
    def primary_color(self) -> "str":
        return "#343839"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LVGL</title>
     <path d="M9.23 16.615h5.54c.51 0 .922.412.922.923v5.539a.921.921
 0 0 1-.923.923H9.231a.921.921 0 0
 1-.923-.923v-5.539c0-.511.411-.923.923-.923zM0
 17.538c0-.51.413-.923.923-.923h5.539c.51 0 .923.413.923.923v5.539c0
 .51-.414.923-.923.923H2.769A2.77 2.77 0 0 1 0
 21.23zm.923-9.23h5.539c.511 0 .923.411.923.922v5.539a.921.921 0 0
 1-.923.923H.923A.921.921 0 0 1 0
 14.769V9.23c0-.511.412-.923.923-.923zM2.77 0A2.77 2.77 0 0 0 0
 2.769V6.46c0 .51.413.923.923.923h5.539c1.02 0 1.846.827 1.846
 1.846v5.539c0 .51.413.923.923.923h5.538c1.02 0 1.847.826 1.847
 1.846v5.539c0 .51.413.923.923.923h3.692A2.77 2.77 0 0 0 24
 21.23V2.77a2.77 2.77 0 0 0-2.77-2.77zm18 1.846a1.385 1.385 0 1 1 0
 2.769 1.385 1.385 0 0 1 0-2.77z" />
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
        yield from [
            "Light and Versatile Graphics Library",
        ]

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


class ViteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vite"

    @property
    def original_file_name(self) -> "str":
        return "vite.svg"

    @property
    def title(self) -> "str":
        return "Vite"

    @property
    def primary_color(self) -> "str":
        return "#646CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vite</title>
     <path d="m8.286 10.578.512-8.657a.306.306 0 0 1
 .247-.282L17.377.006a.306.306 0 0 1 .353.385l-1.558 5.403a.306.306 0
 0 0 .352.385l2.388-.46a.306.306 0 0 1 .332.438l-6.79
 13.55-.123.19a.294.294 0 0 1-.252.14c-.177
 0-.35-.152-.305-.369l1.095-5.301a.306.306 0 0
 0-.388-.355l-1.433.435a.306.306 0 0 1-.389-.354l.69-3.375a.306.306 0
 0 0-.37-.36l-2.32.536a.306.306 0 0 1-.374-.316zm14.976-7.926L17.284
 3.74l-.544 1.887 2.077-.4a.8.8 0 0 1 .84.369.8.8 0 0 1 .034.783L12.9
 19.93l-.013.025-.015.023-.122.19a.801.801 0 0 1-.672.37.826.826 0 0
 1-.634-.302.8.8 0 0 1-.16-.67l1.029-4.981-1.12.34a.81.81 0 0
 1-.86-.262.802.802 0 0 1-.165-.67l.63-3.08-2.027.468a.808.808 0 0
 1-.768-.233.81.81 0 0 1-.217-.6l.389-6.57-7.44-1.33a.612.612 0 0
 0-.64.906L11.58 23.691a.612.612 0 0 0
 1.066-.004l11.26-20.135a.612.612 0 0 0-.644-.9z" />
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

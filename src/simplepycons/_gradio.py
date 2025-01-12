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


class GradioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gradio"

    @property
    def original_file_name(self) -> "str":
        return "gradio.svg"

    @property
    def title(self) -> "str":
        return "Gradio"

    @property
    def primary_color(self) -> "str":
        return "#F97316"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gradio</title>
     <path d="M 12 1.527 A 1.532 1.532 0 0 0 11.24 1.73 L 0.7695 7.732
 A 1.532 1.532 0 0 0 0 9.021 L 0 9.109 A 1.532 1.532 0 0 0 0.7695 10.4
 L 3.57 12 L 0.7695 13.61 C 0.256 13.9 0 14.42 0 14.94 C 0 15.45 0.256
 15.97 0.7695 16.26 L 11.24 22.27 C 11.71 22.54 12.29 22.54 12.76
 22.27 L 23.23 16.26 C 23.73 15.98 23.99 15.48 24 14.97 L 24 14.9 C
 23.99 14.4 23.73 13.89 23.23 13.61 L 20.42 12 L 23.23 10.4 A 1.532
 1.532 0 0 0 24 9.223 L 24 8.91 A 1.532 1.532 0 0 0 23.23 7.732 L
 12.76 1.73 A 1.532 1.532 0 0 0 12 1.527 z M 12 4.826 L 19.39 9.061 L
 17.34 10.24 L 12.76 7.602 C 12.53 7.47 12.27 7.398 12 7.398 C 11.73
 7.398 11.47 7.469 11.24 7.602 L 6.652 10.24 L 4.613 9.061 L 12 4.826
 z M 12 10.7 L 14.27 12 L 12 13.3 L 9.734 12 L 12 10.7 z M 6.652 13.77
 L 11.24 16.39 A 1.532 1.532 0 0 0 12.76 16.39 L 17.34 13.77 L 19.39
 14.94 L 12 19.17 L 4.613 14.94 L 6.652 13.77 z" />
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

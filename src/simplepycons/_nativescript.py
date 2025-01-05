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


class NativescriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nativescript"

    @property
    def original_file_name(self) -> "str":
        return "nativescript.svg"

    @property
    def title(self) -> "str":
        return "NativeScript"

    @property
    def primary_color(self) -> "str":
        return "#65ADF1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NativeScript</title>
     <path d="M1.77 1.76A5.68 5.68 0 0 1 5.8 0h12.6c1.37 0 2.65.6 3.83
 1.76A5.43 5.43 0 0 1 24 5.7v12.77c0 1.34-.56 2.58-1.68 3.73A5.77 5.77
 0 0 1 18.25 24H5.87a6.3 6.3 0 0 1-4.1-1.57C.69 21.45.1 20.03 0
 18.13V5.73a5.21 5.21 0 0 1 1.77-3.97zm6.25 8.3l7.93
 10.06h2.12c.49-.06.88-.2
 1.17-.43.3-.23.5-.56.64-1v-4.94c.08-.95.67-1.54
 1.77-1.75-1.1-.4-1.69-1.02-1.77-1.86V5.42c-.12-.44-.33-.8-.64-1.07a1.83
 1.83 0 0 0-1.09-.47H16v10.2L8.02 3.87H5.79c-.56.1-.97.3-1.25.6S4.08
 5.25 4 5.9v4.85c-.35.69-.9 1.1-1.65 1.25.85.16 1.4.61 1.65
 1.36v4.77c.02.55.2 1 .54 1.37.33.36.7.53 1.1.5H8l.02-9.94z" />
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

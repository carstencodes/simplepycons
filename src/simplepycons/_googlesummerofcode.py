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


class GoogleSummerOfCodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlesummerofcode"

    @property
    def original_file_name(self) -> "str":
        return "googlesummerofcode.svg"

    @property
    def title(self) -> "str":
        return "Google Summer of Code"

    @property
    def primary_color(self) -> "str":
        return "#F9AB00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Summer of Code</title>
     <path d="m11.995 0-.954.954L9.24 2.758l-.755.725h-4.97v5.001L0
 12.004l2.758 2.76.755.752v4.973h4.971L11.995
 24l3.523-3.511h4.961v-4.973L24 12.005l-3.52-3.521v-5h-5.01zm0
 5.068a6.928 6.928 0 0 1 6.94 6.918v.019a6.937 6.937 0 1
 1-6.94-6.937Zm.436 3.457-1.709 6.339.94.253 1.709-6.339zm1.97
 1.047-.715.649 1.431 1.594-1.431 1.593.725.649
 2.013-2.242zm-4.8.01-2.014 2.242L9.6 14.075l.725-.648-1.431-1.594
 1.431-1.603z" />
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
            "GSoC",
        ]

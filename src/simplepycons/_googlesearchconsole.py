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


class GoogleSearchConsoleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlesearchconsole"

    @property
    def original_file_name(self) -> "str":
        return "googlesearchconsole.svg"

    @property
    def title(self) -> "str":
        return "Google Search Console"

    @property
    def primary_color(self) -> "str":
        return "#458CF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Search Console</title>
     <path d="M8.548 1.156L6.832 2.872v1.682h1.716zm0
 3.398v.035H6.832v-.035H3.386L0
 7.844v3.577h2.826V8.94c0-.525.429-.954.954-.954h16.476c.525 0
 .954.43.954.954v2.48h2.754V7.844l-3.386-3.29H17.3v.035h-1.717v-.035zm7.035
 0H17.3V2.872l-1.717-1.716zM8.679 1.188V2.84h6.773V1.188zm11.471
 7.07a.834.834 0
 00-.132.01l-.543.002c-5.216.014-10.432-.008-15.648.01-.435-.063-.794.436-.716.883v2.264h17.812c-.016-.888.045-1.782-.034-2.666-.104-.342-.427-.502-.739-.502zm-15.422.634a.689.698
 0 01.689.698.689.698 0 01-.689.697.689.698 0 01-.688-.697.689.698 0
 01.688-.698zm2.134 0a.689.698 0 01.689.698.689.698 0
 01-.689.697.689.698 0 01-.688-.697.689.698 0 01.688-.698zM.036
 11.645v9.156c0 1.05.858 1.908 1.907 1.908h.883V11.645zm21.174
 0v11.064h.882c1.05 0 1.908-.858 1.908-1.908v-9.156zM4.057
 13.133v6.85h6.137v-6.85zm13.243.021v3.777l-1.708.977-1.708-.977v-3.758a4.006
 4.006 0 000 7.23v2.441h3.457v-2.442a4.006 4.006 0
 00-.041-7.248zm-13.243 8.26v1.43h7.925v-1.43z" />
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

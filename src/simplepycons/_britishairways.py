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


class BritishAirwaysIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "britishairways"

    @property
    def original_file_name(self) -> "str":
        return "britishairways.svg"

    @property
    def title(self) -> "str":
        return "British Airways"

    @property
    def primary_color(self) -> "str":
        return "#2E5C99"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>British Airways</title>
     <path d="M23.489
 13.252c-.25.212-.605.444-1.241.767-1.347.72-2.198.983-2.198.983s-1.617-.234-4.207-1.007c0
 0 1.306-.378 1.93-.581a40.11 40.11 0 0 0 1.958-.681c1.055-.396
 1.73-.761 2.18-1.088.03-.022.058-.046.085-.068 0 0
 .32.036.593.113.294.083.604.245.786.386.191.147.28.308.308.358a.681.681
 0 0 1 .071.226s.014.085-.003.177a.579.579 0 0 1-.147.313zM24
 12.196a.662.662 0 0 0-.08-.157 1.348 1.348 0 0 0-.197-.23 1.685 1.685
 0 0
 0-.227-.178c-.354-.232-.81-.362-1.215-.416-.627-.083-1.342-.07-1.411-.07-.23-.005-1.722.007-2.105.015-1.702.034-3.787.039-4.333.038-5.636.027-8.089-.094-10.82-.642C1.289
 10.094 0 9.658 0 9.658c2.05-.073 14.004-.568 16.186-.627 1.427-.04
 2.44-.048 3.253 0 .413.023.802.058 1.287.14a6.2 6.2 0 0 1
 1.064.286c.486.18.893.442 1.096.707 0 0
 .06.06.14.17.093.126.197.282.234.34.294.447.434.73.484.828.052.102.1.209.145.315.044.104.063.166.076.21.02.064.03.125.035.17Z"
 />
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

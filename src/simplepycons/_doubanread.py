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


class DoubanReadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "doubanread"

    @property
    def original_file_name(self) -> "str":
        return "doubanread.svg"

    @property
    def title(self) -> "str":
        return "Douban Read"

    @property
    def primary_color(self) -> "str":
        return "#24D2C8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Douban Read</title>
     <path d="M16.056 3c-4.128 0-5.432 3.97-7.994
 5.966l-.152.115c-.828.607-1.787 1.005-3.012 1.005C2.009 10.083.38
 7.855 0 6.435c0 1.098.177 2.248.499 3.397C2.049 15.403 6.96 21 11.41
 21c5.206 0 8.985-5.428 10.127-9.556.369-1.332 1.204-2.478
 2.368-3.178l.095-.06-.14-.054-.001.004c-1.144-.453-2.082-1.308-2.72-2.384-.983-1.65-2.984-2.77-5.083-2.77m2.705
 3.75c.379.008.702.358.736.822.037.496-.269.933-.683.976-.412.041-.775-.325-.811-.82s.267-.93.68-.976zm-4.609
 2.252a2.46 2.46 0 0 1 1.048.714c1.487 1.825.403 4.62-1.368
 5.858-2.196 1.616-5.202.876-7.382-.379a9.5 9.5 0 0 1-2.775-2.433 10
 10 0 0 1-.672-1.021c-.011-.018.015-.035.027-.019 1.391 1.977 3.554
 3.302 5.904 3.715.947.144 1.903.24 2.794-.036 1.532-.524 2.903-1.736
 3.334-3.329.321-1.088.026-2.33-.938-3.019-.028-.017 0-.064.028-.052"
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

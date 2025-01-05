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


class YoutubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "youtube"

    @property
    def original_file_name(self) -> "str":
        return "youtube.svg"

    @property
    def title(self) -> "str":
        return "YouTube"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YouTube</title>
     <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545
 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0
 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122
 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0
 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545
 15.568V8.432L15.818 12l-6.273 3.568z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.youtube.com/howyoutubeworks/resou'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.youtube.com/howyoutubeworks/resou'''

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

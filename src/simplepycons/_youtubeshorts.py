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


class YoutubeShortsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "youtubeshorts"

    @property
    def original_file_name(self) -> "str":
        return "youtubeshorts.svg"

    @property
    def title(self) -> "str":
        return "YouTube Shorts"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YouTube Shorts</title>
     <path d="m18.931 9.99-1.441-.601 1.717-.913a4.48 4.48 0 0 0
 1.874-6.078 4.506 4.506 0 0 0-6.09-1.874L4.792 5.929a4.504 4.504 0 0
 0-2.402 4.193 4.521 4.521 0 0 0 2.666 3.904c.036.012 1.442.6
 1.442.6l-1.706.901a4.51 4.51 0 0 0-2.369 3.967A4.528 4.528 0 0 0 6.93
 24c.725 0 1.437-.174 2.08-.508l10.21-5.406a4.494 4.494 0 0 0
 2.39-4.192 4.525 4.525 0 0 0-2.678-3.904ZM9.597 15.19V8.824l6.007
 3.184z" />
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

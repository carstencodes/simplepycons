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


class FfmpegIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ffmpeg"

    @property
    def original_file_name(self) -> "str":
        return "ffmpeg.svg"

    @property
    def title(self) -> "str":
        return "FFmpeg"

    @property
    def primary_color(self) -> "str":
        return "#007808"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FFmpeg</title>
     <path d="M21.72 17.91V6.5l-.53-.49L9.05 18.52l-1.29-.06L24
 1.53l-.33-.95-11.93 1-5.75
 6.6v-.23l4.7-5.39-1.38-.77-9.11.77v2.85l1.91.46v.01l.19-.01-.56.66v10.6c.609-.126
 1.22-.241 1.83-.36L14.12 5.22l.83-.04L0 21.44l9.67.82 1.35-.77
 6.82-6.74v2.15l-5.72 5.57
 11.26.95.35-.94v-3.16l-3.29-.18c.434-.403.858-.816 1.28-1.23z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:FFmpe'''

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

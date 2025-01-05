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


class AtariIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "atari"

    @property
    def original_file_name(self) -> "str":
        return "atari.svg"

    @property
    def title(self) -> "str":
        return "Atari"

    @property
    def primary_color(self) -> "str":
        return "#E4202E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Atari</title>
     <path d="M0 21.653s3.154-.355 5.612-2.384c2.339-1.93 3.185-3.592
 3.77-5.476.584-1.885.671-6.419.671-7.764V2.346H8.598v1.365c-.024
 2.041-.2 5.918-1.135 8.444C5.203 18.242 0 18.775 0 18.775zm24
 0s-3.154-.355-5.61-2.384c-2.342-1.93-3.187-3.592-3.772-5.476-.583-1.885-.671-6.419-.671-7.764V2.346H15.4l.001
 1.365c.024 2.041.202 5.918 1.138 8.444 2.258 6.087 7.46 6.62 7.46
 6.62zM10.659 2.348h2.685v19.306H10.66Z" />
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

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


class SmoothcompIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smoothcomp"

    @property
    def original_file_name(self) -> "str":
        return "smoothcomp.svg"

    @property
    def title(self) -> "str":
        return "Smoothcomp"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Smoothcomp</title>
     <path d="M6.3415 0C2.845 0 0 2.8445 0 6.3415v11.3166C0 21.155
 2.8449 24 6.3415 24h11.317C21.155 24 24 21.155 24 17.658V6.3416C24
 2.845 21.155 0 17.6585 0Zm0 2.1493h11.317c2.3117 0 4.1922 1.8805
 4.1922 4.1922v11.3166c0 2.3118-1.8805 4.1923-4.1922
 4.1923H6.3415c-2.3117 0-4.1922-1.8802-4.1922-4.1923V6.3415c0-2.3117
 1.8805-4.1922 4.1922-4.1922zM7.06 5.638c-.7632 0-1.3842.6211-1.3842
 1.3843v10.0035c0 .7629.621 1.384 1.3842 1.384h10.0047c.7628 0
 1.3835-.6208 1.3835-1.3836V7.022c0-.37-.1443-.7174-.4057-.9788a1.3745
 1.3745 0 0 0-.9786-.405Zm.765 2.1493h8.474v8.4735H7.825Z" />
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

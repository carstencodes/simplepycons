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


class TvFourPlayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tv4play"

    @property
    def original_file_name(self) -> "str":
        return "tv4play.svg"

    @property
    def title(self) -> "str":
        return "TV4 Play"

    @property
    def primary_color(self) -> "str":
        return "#E0001C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TV4 Play</title>
     <path d="M10.374 15.93V3.718c0-.209-.279-.307-.402-.12L.037
 18.289a.199.199 0 0 0-.006.223c.036.072.108.12.192.12h7.331v1.656c0
 .113.102.215.222.215h2.376c.12 0 .222-.102.222-.215v-1.656h1.435c.12
 0 .222-.096.222-.222v-2.257a.22.22 0 0
 0-.224-.222zm-2.826.008H4.795l2.753-4.073zm16.313-3.744L16.704
 8.06c-.078-.049-.169.035-.132.12a10.53 10.53 0 0 1 .894 4.26c0
 1.512-.317 2.952-.888
 4.248-.036.083.053.161.131.12l7.152-4.127a.283.283 0 0 0 0-.487z" />
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

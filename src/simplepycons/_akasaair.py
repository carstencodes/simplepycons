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


class AkasaAirIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "akasaair"

    @property
    def original_file_name(self) -> "str":
        return "akasaair.svg"

    @property
    def title(self) -> "str":
        return "Akasa Air"

    @property
    def primary_color(self) -> "str":
        return "#FF6300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Akasa Air</title>
     <path d="M14.7315 1.8005c-2.297 0-3.2705.731-4.165 2.3824l-.6291
 1.1158a3.2264 3.2264 0 0 0-.5293 1.4828c.026.4297.1655.8441.4064
 1.201l5.0022 8.9444c1.789 3.1968 4.0007 4.9858 8.7642 4.9858.4075 0
 .508-.2434.344-.5292L17.4367 9.793C16.14 7.4536 15.69 5.7656 15.69
 4.5483a3.5322 3.5322 0 0 1
 .8143-2.425c.1218-.1376.101-.3228-.1425-.3228ZM7.8123 8.8558c-.1218
 0-.201.084-.3228.285L.0787 21.7113a.3929.3929 0 0 0-.0786.2441c0
 .2435.386.2442.4866.2442 5.335 0 9.041-3.2553 9.041-7.9712a10.0555
 10.0555 0 0 0-1.409-5.107c-.1006-.1589-.1847-.2655-.3064-.2655Z" />
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

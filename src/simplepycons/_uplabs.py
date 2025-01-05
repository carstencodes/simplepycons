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


class UplabsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uplabs"

    @property
    def original_file_name(self) -> "str":
        return "uplabs.svg"

    @property
    def title(self) -> "str":
        return "UpLabs"

    @property
    def primary_color(self) -> "str":
        return "#3930D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UpLabs</title>
     <path d="M9.804
 19.205c-.112-.111-.186-.26-.297-.372-.889-.894-2.259-1.34-4.11-1.34-1.816
 0-3.186.446-4.075
 1.34-.111.112-.185.223-.296.372zm2.88-.044V5.164h2.959V6.9c.406-.702.887-1.219
 1.479-1.588a4.057 4.057 0 0 1 2.034-.517c1.516 0 2.7.517 3.55
 1.514.85.997 1.294 2.4 1.294 4.173 0 1.736-.444 3.102-1.294 4.136-.85
 1.034-1.997 1.551-3.402 1.551-.851
 0-1.554-.147-2.145-.48-.592-.295-1.11-.812-1.516-1.477.037.259.073.554.073.886
 0 .296.037.665.037 1.071v2.955h-3.069zm2.81-8.679c0 .96.222 1.699.703
 2.253.481.517 1.147.812 1.96.812.85 0 1.516-.258
 1.96-.812.48-.517.703-1.293.703-2.253
 0-.96-.222-1.699-.703-2.253-.48-.554-1.146-.812-1.997-.812-.813
 0-1.479.295-1.96.85-.444.48-.665 1.255-.665 2.215zM7.73 5.201v5.577c0
 .923-.185 1.588-.555 1.994-.37.406-.961.628-1.775.628-.813
 0-1.405-.185-1.775-.591-.37-.407-.555-1.071-.555-2.031V5.2H0v5.577c0
 1.661.333 2.88.998 3.767.111.11.185.258.296.369.888.886 2.256 1.33
 4.105 1.33 1.812 0 3.18-.444
 4.068-1.33.11-.111.185-.222.296-.37.665-.886.998-2.142.998-3.766V5.2Z"
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

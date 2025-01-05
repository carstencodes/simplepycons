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


class HiveIcon1(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hive"

    @property
    def original_file_name(self) -> "str":
        return "hive.svg"

    @property
    def title(self) -> "str":
        return "Hive"

    @property
    def primary_color(self) -> "str":
        return "#FF7A00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hive</title>
     <path d="M19.442
 21.355c.55-.19.74-.256.99-.373.342-.152.605-.39.605-.818a.846.846 0
 00-.605-.813c-.318-.092-.703.042-.99.122l-5.42 1.46a7.808 7.808 0
 01-4.057 0l-5.407-1.46c-.287-.08-.672-.214-.99-.122a.847.847 0
 00-.605.813c0 .427.263.666.605.818.25.117.44.184.99.373l5.138
 1.79c1.491.52 3.104.52 4.601 0zm-9.263-3.224a7.622 7.622 0 003.636
 0l8.01-1.967c.507-.122.709-.165.99-.257.354-.116.605-.415.605-.806a.847.847
 0 00-.605-.813c-.281-.08-.697.024-.99.08l-8.664 1.545a6.813 6.813 0
 01-2.334 0l-8.652-1.545c-.293-.056-.708-.16-.99-.08a.847.847 0
 00-.604.813c0
 .39.25.69.604.806.282.092.483.135.99.257zM14.75.621a24.43 24.43 0
 00-5.511
 0L6.495.933c-.294.03-.715.055-.99.14-.28.092-.605.355-.605.807 0
 .39.257.702.605.806.281.08.696.074.99.074h11.01c.293 0
 .709.006.99-.074a.835.835 0
 00.605-.806c0-.452-.324-.715-.605-.807-.275-.085-.697-.11-.99-.14zm6.037
 6.767c.3-.019.709-.037.99-.116a.84.84 0
 000-1.614c-.281-.085-.69-.073-.99-.073H3.214c-.3
 0-.709-.012-.99.073a.84.84 0 000
 1.614c.281.079.69.097.99.116l7.808.556c.642.042 1.308.042 1.943
 0zm1.62
 4.242c.513-.08.708-.104.989-.202.354-.121.605-.409.605-.806a.84.84 0
 00-.605-.806c-.28-.086-.69-.019-.99.012l-9.232.929c-.776.079-1.582.079-2.358
 0l-9.22-.93c-.3-.03-.715-.097-.99-.011a.84.84 0 00-.605.806c0
 .397.25.685.605.806.275.092.476.123.99.202l8.823 1.418c1.038.165
 2.12.165 3.158 0Z" />
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

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


class AntvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "antv"

    @property
    def original_file_name(self) -> "str":
        return "antv.svg"

    @property
    def title(self) -> "str":
        return "AntV"

    @property
    def primary_color(self) -> "str":
        return "#8B5DFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AntV</title>
     <path d="M4.837 1.418c-.363 0-3.064.002-3.545 0-.188
 0-.446.1-.62.2-.538.305-.855 1.123-.558 1.735L10.69
 21.71c.357.617.801.87 1.324.871.63.001 1.038-.454 1.18-.7.635-1.088
 6.214-10.707 6.214-10.707a1.285 1.285 0 0
 0-.497-1.694c-.596-.348-1.397-.197-1.744.388-.307.517-4.58
 7.888-4.886
 8.413-.156.267-.463.2-.585-.017-.216-.383-5.255-9.13-7.833-13.605l.005.004c-.066-.103-.15-.328-.043-.509.09-.155.279-.138.372-.138h9.535a1.3
 1.3 0 0 0 0-2.6zm12.737.029v.003a1.3 1.3 0 0 0 0
 2.593v.003l2.386.002c.309 0 .406.3.28.514L19.053 6.59l.002.002a1.3
 1.3 0 0 0 2.243 1.303l.002.002
 2.425-4.2c.354-.62.349-1.13.086-1.582-.315-.544-.915-.667-1.2-.667Zm-2.839
 5.642-.038.002H9.71a.54.54 0 0 0-.523.55c0 .12.037.23.098.32l2.505
 4.275q.014.028.032.055l.003.005a.47.47 0 0 0 .39.207c.194 0
 .36-.12.435-.294l2.506-4.306a.515.515 0 0 0-.42-.814" />
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

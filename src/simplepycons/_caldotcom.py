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


class CaldotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "caldotcom"

    @property
    def original_file_name(self) -> "str":
        return "caldotcom.svg"

    @property
    def title(self) -> "str":
        return "Cal.com"

    @property
    def primary_color(self) -> "str":
        return "#292929"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cal.com</title>
     <path d="M2.408 14.488C1.035 14.488 0 13.4 0
 12.058c0-1.346.982-2.443 2.408-2.443.758 0 1.282.233
 1.691.765l-.66.55a1.343 1.343 0 0 0-1.03-.442c-.93 0-1.44.711-1.44
 1.57 0 .86.559 1.557 1.44 1.557.413 0 .765-.147
 1.043-.443l.651.573c-.391.51-.929.743-1.695.743zM6.948
 10.913h.89v3.49h-.89v-.51c-.185.362-.493.604-1.083.604-.943
 0-1.695-.82-1.695-1.826 0-1.007.752-1.825 1.695-1.825.585 0 .898.241
 1.083.604zm.026 1.758c0-.546-.374-.998-.964-.998-.568
 0-.938.457-.938.998 0 .528.37.998.938.998.586 0
 .964-.456.964-.998zM8.467 9.503h.89v4.895h-.89zM9.752 13.937a.53.53 0
 0 1 .542-.528c.313 0 .533.242.533.528a.527.527 0 0 1-.533.537.534.534
 0 0 1-.542-.537zM14.23 13.839c-.33.403-.832.658-1.426.658a1.806 1.806
 0 0 1-1.84-1.826c0-1.007.778-1.825 1.84-1.825.572 0 1.07.241
 1.4.622l-.687.577c-.172-.215-.396-.376-.713-.376-.568
 0-.938.456-.938.998 0 .541.37.997.938.997.343 0
 .58-.179.757-.42zM14.305 12.671c0-1.007.78-1.825 1.84-1.825 1.061 0
 1.84.818 1.84 1.825 0 1.007-.779 1.826-1.84
 1.826-1.06-.005-1.84-.82-1.84-1.826zm2.778
 0c0-.546-.37-.998-.938-.998-.568-.004-.937.452-.937.998 0
 .542.37.998.937.998.568 0 .938-.456.938-.998zM24
 12.269v2.13h-.89v-1.911c0-.604-.281-.864-.704-.864-.396
 0-.678.197-.678.864v1.91h-.89v-1.91c0-.604-.285-.864-.704-.864-.396
 0-.744.197-.744.864v1.91h-.89v-3.49h.89v.484c.185-.376.52-.564
 1.035-.564.489 0 .898.241 1.123.649.224-.417.554-.65
 1.153-.65.731.005 1.299.56 1.299 1.442z" />
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

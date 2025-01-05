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


class OpenSourceInitiativeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opensourceinitiative"

    @property
    def original_file_name(self) -> "str":
        return "opensourceinitiative.svg"

    @property
    def title(self) -> "str":
        return "Open Source Initiative"

    @property
    def primary_color(self) -> "str":
        return "#3DA639"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Source Initiative</title>
     <path d="M11.959.447A11.938 11.938 0 000 12.407c0 5.576 3.874
 10.097 7.783 11.114.193.05.392-.05.467-.234l2.771-6.822a.396.396 0
 00-.246-.528C9.365 15.47 8.53 14.32 8.48 12.4c-.024-1.828 1.5-3.45
 3.561-3.447 1.931.003 3.479 1.632 3.479 3.453 0 .966-.203 1.687-.575
 2.238-.371.552-.922.951-1.695 1.239a.396.396 0 00-.23.515l2.685
 6.903a.396.396 0 00.465.24C20.163 22.534 24 18.062 24 12.406 24 5.804
 18.603.447 11.959.447zm0 .791c6.22 0 11.25 4.997 11.25 11.168 0
 5.138-3.423 9.208-6.895 10.272L13.9 16.47c.703-.308 1.302-.79
 1.702-1.384.477-.708.709-1.602.709-2.68
 0-2.266-1.898-4.24-4.27-4.244-2.48-.004-4.382 1.976-4.352 4.25.023
 1.995.934 3.492 2.451 4.13L7.648 22.66C4.251 21.592.791 17.458.791
 12.406A11.13 11.13 0 0111.959 1.238zm10.617 20.149a1.03 1.03 0 000
 2.058 1.03 1.03 0 000-2.058zm0 .162c.48 0 .865.388.865.867a.856.856 0
 01-.271.623l-.172-.342a.847.847 0 00-.111-.178.263.263 0
 00-.114-.084.301.301 0 00.17-.117.356.356 0
 00.061-.21c0-.13-.038-.227-.113-.292-.076-.064-.192-.095-.346-.095h-.41v1.343h.181v-.568h.2c.072
 0 .128.015.17.045a.48.48 0 01.129.18l.171.343.157.001a.878.878 0
 01-.567.216.865.865 0 010-1.732zm-.26.322h.229c.088 0
 .155.018.2.059.044.04.066.099.066.177 0
 .079-.022.14-.067.18-.044.04-.111.06-.2.06h-.228z" />
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

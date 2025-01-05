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


class PeerlistIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "peerlist"

    @property
    def original_file_name(self) -> "str":
        return "peerlist.svg"

    @property
    def title(self) -> "str":
        return "Peerlist"

    @property
    def primary_color(self) -> "str":
        return "#00AA45"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Peerlist</title>
     <path d="M12 0C2.667 0 0 2.667 0 12s2.673 12 12 12 12-2.667
 12-12S21.327 0 12 0zm8.892 20.894c-1.57 1.569-4.247 2.249-8.892
 2.249s-7.322-.68-8.892-2.25C1.735 19.522 1.041 17.3.89 13.654A39.74
 39.74 0 0 1 .857 12c0-1.162.043-2.201.13-3.13.177-1.859.537-3.278
 1.106-4.366.284-.544.62-1.006 1.013-1.398s.854-.729 1.398-1.013C5.592
 1.524 7.01 1.164 8.87.988 9.799.9 10.838.858 12 .858c4.645 0 7.322.68
 8.892 2.248 1.569 1.569 2.25 4.246 2.25 8.894s-.681 7.325-2.25
 8.894zM20.538 3.46C19.064 1.986 16.51 1.357 12 1.357c-4.513
 0-7.067.629-8.54 2.103C1.986 4.933 1.357 7.487 1.357 12c0 4.511.63
 7.065 2.105 8.54C4.936 22.014 7.49 22.643 12 22.643s7.064-.629
 8.538-2.103c1.475-1.475 2.105-4.029
 2.105-8.54s-.63-7.065-2.105-8.54zM14.25 16.49a6.097 6.097 0 0
 1-2.442.59v2.706H10.45v.357H6.429V5.57h.357V4.214h5.676c3.565 0 6.467
 2.81 6.467 6.262 0 2.852-1.981 5.26-4.68
 6.013zm-1.788-8.728H10.45v5.428h2.011c1.532 0 2.802-1.2
 2.802-2.714s-1.27-2.714-2.802-2.714zm.901
 4.351c.117-.239.186-.502.186-.78
 0-1.01-.855-1.857-1.945-1.857h-.296V8.62h1.154c1.09 0 1.945.847 1.945
 1.857 0 .705-.422 1.323-1.044 1.637zm4.104
 1.493c.043-.063.083-.129.123-.194a5.653 5.653 0 0 0 .526-1.103 5.56
 5.56 0 0 0 .11-.362c.02-.076.042-.15.06-.227a5.58 5.58 0 0 0
 .073-.41c.01-.068.025-.134.032-.203.024-.207.038-.417.038-.63
 0-3.198-2.687-5.763-5.967-5.763H7.286v14.572h4.022v-3.048h1.154c1.43
 0 2.747-.488 3.778-1.303a5.92 5.92 0 0 0
 .46-.406c.035-.034.066-.07.1-.105.107-.11.21-.22.308-.337.044-.053.084-.108.126-.162.081-.104.16-.21.233-.319zm-5.005
 1.775H10.45v3.048H8.143V5.57h4.319c2.837 0 5.11 2.211 5.11
 4.905s-2.273 4.905-5.11 4.905z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://peerlist.io/legal/peerlist-terms-cond'''
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

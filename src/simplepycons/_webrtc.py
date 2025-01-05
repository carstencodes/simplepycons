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


class WebrtcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webrtc"

    @property
    def original_file_name(self) -> "str":
        return "webrtc.svg"

    @property
    def title(self) -> "str":
        return "WebRTC"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WebRTC</title>
     <path d="M11.9998.3598c-2.8272 0-5.1456 2.1733-5.3793 4.94a5.4117
 5.4117 0 00-1.2207-.1401C2.418 5.1597 0 7.5779 0 10.5603c0 2.2203
 1.341 4.1274 3.2568 4.957a5.3734 5.3734 0 00-.7372 2.7227c0 2.9823
 2.4175 5.4002 5.4002 5.4002 1.6627 0 3.1492-.7522 4.1397-1.934.9906
 1.1818 2.4773 1.934 4.1398 1.934 2.983 0 5.4004-2.418 5.4004-5.4002
 0-.9719-.258-1.883-.7073-2.6708C22.7283 14.7068 24 12.8418 24
 10.6795c0-2.9823-2.4175-5.4006-5.3998-5.4006-.417
 0-.8223.049-1.2121.1384C17.2112 2.5949 14.867.3598
 11.9998.3598zm-5.717 6.8683h10.5924c.7458 0 1.352.605 1.352
 1.3487v7.6463c0 .7438-.6062 1.3482-1.352 1.3482h-3.6085l-7.24 3.5491
 1.1008-3.5491h-.8447c-.7458
 0-1.3522-.6044-1.3522-1.3482V8.5768c0-.7438.6064-1.3487
 1.3522-1.3487Z" />
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

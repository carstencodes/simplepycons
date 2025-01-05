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


class XmppIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xmpp"

    @property
    def original_file_name(self) -> "str":
        return "xmpp.svg"

    @property
    def title(self) -> "str":
        return "XMPP"

    @property
    def primary_color(self) -> "str":
        return "#002B5C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>XMPP</title>
     <path d="m3.401 4.594 1.025.366
 3.08.912c-.01.18-.016.361-.016.543 0 3.353 1.693 7.444 4.51 10.387
 2.817-2.943 4.51-7.034 4.51-10.387
 0-.182-.006-.363-.016-.543l3.08-.912 1.025-.366L24 3.276C23.854 8.978
 19.146 14.9 13.502 18.17c1.302 1.028 2.778 1.81 4.388
 2.215v.114l.004.001v.224a14.55 14.55 0 0 1-4.829-1.281A20.909 20.909
 0 0 1 12 18.966c-.353.17-.708.329-1.065.477a14.55 14.55 0 0 1-4.829
 1.281V20.5l.004-.001v-.113c1.61-.406 3.086-1.188 4.389-2.216C4.854
 14.9.146 8.978 0 3.276l3.401 1.318Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/xsf/xmpp.org/blob/82856a2c'''

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

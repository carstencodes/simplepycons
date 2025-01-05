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


class RustdeskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rustdesk"

    @property
    def original_file_name(self) -> "str":
        return "rustdesk.svg"

    @property
    def title(self) -> "str":
        return "RustDesk"

    @property
    def primary_color(self) -> "str":
        return "#024EFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RustDesk</title>
     <path d="m20.6081 5.6014-1.9708 1.9588c-.347.3111-.515.8114-.3203
 1.2342 1.3127 2.7471.8142 6.0223-1.3403 8.175-2.1554 2.1516-5.4343
 2.6492-8.1842 1.3375-.4052-.1819-.8806-.0277-1.1926.288l-2.0031
 2.0003a1.0652 1.0652 0 0 0 .192 1.6708 12.0048 12.0048 0 0 0
 14.6864-1.765A11.9725 11.9725 0 0 0 22.2808 5.836a1.0652 1.0652 0 0
 0-1.6727-.2345zM3.5614 3.4737A11.9716 11.9716 0 0 0 1.6967
 18.137a1.0652 1.0652 0 0 0 1.6727.2345L5.33
 16.4238c.3554-.3102.528-.816.3314-1.2444-1.3136-2.747-.816-6.0222
 1.3394-8.1749C9.1553 4.852 12.4351 4.3543 15.185
 5.666c.4006.1791.8695.0305 1.1824-.2769l2.0142-2.0123a1.0634 1.0634 0
 0 0-.192-1.6708A12.0085 12.0085 0 0 0 3.519 3.5272z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rustdesk/rustdesk/blob/808'''

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

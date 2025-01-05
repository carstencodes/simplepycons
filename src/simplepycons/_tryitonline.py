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


class TryItOnlineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tryitonline"

    @property
    def original_file_name(self) -> "str":
        return "tryitonline.svg"

    @property
    def title(self) -> "str":
        return "Try It Online"

    @property
    def primary_color(self) -> "str":
        return "#303030"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Try It Online</title>
     <path d="M.75 6a.75.75 0 100 1.5H4.5v9.75a.75.75 0 101.5
 0V7.5h17.25a.75.75 0 100-1.5zm10.5 3a.75.75 0 00-.75.75v7.5a.75.75 0
 101.5 0v-7.5a.75.75 0 00-.75-.75zm8.25 0a4.51 4.51 0 00-4.5 4.5c0
 2.48 2.02 4.5 4.5 4.5s4.5-2.02 4.5-4.5S21.98 9 19.5 9zm0 1.5c1.67 0 3
 1.33 3 3s-1.33 3-3 3-3-1.33-3-3 1.33-3 3-3Z" />
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

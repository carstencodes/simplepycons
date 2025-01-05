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


class BigCartelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bigcartel"

    @property
    def original_file_name(self) -> "str":
        return "bigcartel.svg"

    @property
    def title(self) -> "str":
        return "Big Cartel"

    @property
    def primary_color(self) -> "str":
        return "#222222"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Big Cartel</title>
     <path d="M12
 13.068v-1.006c0-.63.252-1.256.88-1.508l7.79-4.9c.503-.252.755-.88.755-1.51V0L12
 6.03 2.575 0v12.69c0 3.394 1.51 6.284 4.02 7.917L11.875
 24l5.28-3.393c2.513-1.51 4.02-4.398 4.02-7.916V7.036L12 13.068z" />
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

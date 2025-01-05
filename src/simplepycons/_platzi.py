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


class PlatziIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "platzi"

    @property
    def original_file_name(self) -> "str":
        return "platzi.svg"

    @property
    def title(self) -> "str":
        return "Platzi"

    @property
    def primary_color(self) -> "str":
        return "#98CA3F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Platzi</title>
     <path d="M10.6392 1.127L2.486 9.282a3.842 3.842 0 000
 5.4361l8.1552 8.1552a3.842 3.842 0 005.4361
 0l2.719-2.718-2.719-2.7181-2.718 2.718-8.1562-8.1551 8.1552-8.1552
 5.437 5.4371-5.437 5.4361 2.718 2.719 5.4371-5.437a3.842 3.842 0
 000-5.4372l-5.448-5.436a3.828 3.828 0 00-5.4252 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/PlatziDev/oss/blob/932bd83'''

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

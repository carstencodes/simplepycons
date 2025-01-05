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


class DiscourseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "discourse"

    @property
    def original_file_name(self) -> "str":
        return "discourse.svg"

    @property
    def title(self) -> "str":
        return "Discourse"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Discourse</title>
     <path d="M12.103 0C18.666 0 24 5.485 24 11.997c0 6.51-5.33
 11.99-11.9 11.99L0 24V11.79C0 5.28 5.532 0 12.103 0zm.116
 4.563c-2.593-.003-4.996 1.352-6.337 3.57-1.33 2.208-1.387 4.957-.148
 7.22L4.4 19.61l4.794-1.074c2.745 1.225 5.965.676 8.136-1.39
 2.17-2.054 2.86-5.228
 1.737-7.997-1.135-2.778-3.84-4.59-6.84-4.585h-.008z" />
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

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


class ReebokIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reebok"

    @property
    def original_file_name(self) -> "str":
        return "reebok.svg"

    @property
    def title(self) -> "str":
        return "Reebok"

    @property
    def primary_color(self) -> "str":
        return "#E41D1B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reebok</title>
     <path d="M14.991 11.48C17.744 10.38 19.458 9.748 24
 8.64c-2.467.163-7.922.537-11.682 1.271l2.673 1.57m-8.56
 3.651h3.6c.713-1.08 1.422-1.606 2.248-2.191a71.382 71.382 0
 00-1.892-.701c-2.297 1.014-3.575 2.375-3.953 2.892m.709-3.928c-3.21
 1.147-4.994 2.393-6.199 3.928h3.975c.387-.539 1.862-2.093
 4.633-3.174a57.092 57.092 0 00-2.41-.754M8.79 8.788H0c8.862 1.6
 13.133 3.66 20 6.572-.587-.439-10.051-6.013-11.209-6.572" />
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

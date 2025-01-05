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


class FandangoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fandango"

    @property
    def original_file_name(self) -> "str":
        return "fandango.svg"

    @property
    def title(self) -> "str":
        return "Fandango"

    @property
    def primary_color(self) -> "str":
        return "#FF7300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fandango</title>
     <path d="M13.664 6.956L8.05 8.496 9.19 12.72l5.615-1.54L15.95
 15.4l-5.615 1.49 1.093 4.224-5.615 1.49L4.42 17.54c.846-.995
 1.194-2.386.846-3.728-.398-1.342-1.392-2.385-2.584-2.832L1.29 5.763
 12.57 2.78zm7.106-.198L18.932.05 0 5.068l1.838 6.758c1.093.2 2.087
 1.043 2.385 2.236.348 1.193-.1 2.385-.944 3.18l1.788 6.708L24
 18.882l-1.79-6.708c-1.142-.2-2.086-1.043-2.434-2.236-.298-1.193.1-2.435.994-3.18z"
 />
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

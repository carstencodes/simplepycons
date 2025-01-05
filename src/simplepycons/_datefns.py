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


class DatefnsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datefns"

    @property
    def original_file_name(self) -> "str":
        return "datefns.svg"

    @property
    def title(self) -> "str":
        return "date-fns"

    @property
    def primary_color(self) -> "str":
        return "#770C56"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>date-fns</title>
     <path d="M1.065 6.534C.355 8.246 0 10.068 0 11.999c0 1.932.355
 3.754 1.065 5.466a13.768 13.768 0 0 0 3.068
 4.549h2.685c-2.784-2.756-4.176-6.094-4.176-10.015 0-3.92 1.392-7.258
 4.176-10.014H4.133a13.768 13.768 0 0 0-3.068 4.549Zm21.869
 10.931c.71-1.712 1.066-3.534 1.066-5.466
 0-1.931-.356-3.753-1.066-5.465a13.768 13.768 0 0
 0-3.068-4.549h-2.685c2.784 2.756 4.176 6.094 4.176 10.014 0
 3.921-1.392 7.259-4.176 10.015h2.685a13.768 13.768 0 0 0
 3.068-4.549ZM11.63
 3.299H9.854v10.21h1.776v-.033l7.218-7.218-1.151-1.151-6.067
 6.067V3.299Z" />
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

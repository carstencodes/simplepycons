#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AftershipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aftership"

    @property
    def original_file_name(self) -> "str":
        return "aftership.svg"

    @property
    def title(self) -> "str":
        return "AfterShip"

    @property
    def primary_color(self) -> "str":
        return "#FF6B2B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AfterShip</title>
     <path d="M22.549 9.604a10.462 10.462 0 0 0-3.388-6.838A10.632
 10.632 0 0 0 12 0a10.64 10.64 0 0 0-7.16 2.764 10.465 10.465 0 0
 0-3.428 7.74c0 2.371.81 4.672 2.298 6.529a10.617 10.617 0 0 0 5.895
 3.698L12 24l2.395-3.27a10.593 10.593 0 0 0 5.895-3.697 10.442 10.442
 0 0 0 2.26-7.43zm-11.306 6.28a.26.26 0 0 1-.034.125.254.254 0 0
 1-.347.092l-3.906-2.237a1.005 1.005 0 0 1-.505-.865V8.624a.26.26 0 0
 1 .033-.126.254.254 0 0 1 .347-.092l3.907
 2.237c.152.089.281.214.368.366.09.151.135.324.135.5v4.372zM12
 9.48c-.176 0-.35-.047-.503-.133L7.5 7.057a.241.241 0 0
 1-.09-.092.249.249 0 0 1 .09-.342l3.997-2.289a1.025 1.025 0 0 1 1.007
 0l3.996 2.29a.24.24 0 0 1 .09.092.247.247 0 0 1 0 .25.271.271 0 0
 1-.09.092l-3.997 2.289A1.005 1.005 0 0 1 12 9.48ZM17.546 13a.996.996
 0 0 1-.503.866l-3.908 2.237a.254.254 0 0
 1-.38-.218V11.51c0-.175.047-.348.135-.501.089-.152.216-.28.368-.366l3.907-2.238a.254.254
 0 0 1 .38.219z" />
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
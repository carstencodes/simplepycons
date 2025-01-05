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


class CarThrottleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "carthrottle"

    @property
    def original_file_name(self) -> "str":
        return "carthrottle.svg"

    @property
    def title(self) -> "str":
        return "Car Throttle"

    @property
    def primary_color(self) -> "str":
        return "#FF9C42"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Car Throttle</title>
     <path d="M0 19.99h5.31l1-5.76h2.673L7.97
 19.99h5.272l1.037-5.76h2.824l-1 5.76h7.584L21.9 17.029 24
 4.01h-5.16l-.987 5.647h-2.86l.936-5.647H8.483l1.724 2.749-.487
 2.898H6.996l.9-5.647H.35l1.76 2.774Z" />
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

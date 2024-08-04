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


class VEightIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "v8"

    @property
    def original_file_name(self) -> "str":
        return "v8.svg"

    @property
    def title(self) -> "str":
        return "V8"

    @property
    def primary_color(self) -> "str":
        return "#4B8BF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>V8</title>
     <path d="M6.832
 6c0-.161.008-.322.023-.479.019-.207.07-.401.112-.599l-.694-1.377H0l2.182
 3.818h1.527l2.097 3.98a6.534 6.534 0 0 1 1.727-2.745A5.123 5.123 0 0
 1 6.832 6zM10.365 19.663L12
 22.637l1.637-2.975c-.535.138-1.079.234-1.637.234s-1.101-.096-1.635-.233zM17.728
 3.545l-.717 1.258c.056.238.112.476.134.726a5.148 5.148 0 0 1-.677
 3.07 6.565 6.565 0 0 1 1.727 2.746l2.097-3.981h1.527L24 3.545h-6.272z
 M17.846 12.007a6 6 0 0 0-2.073-3.31A4.64 4.64 0 0 0 12 1.363 4.635
 4.635 0 0 0 7.363 6a4.62 4.62 0 0 0 .865 2.697A5.988 5.988 0 0 0 6
 13.363a6.01 6.01 0 0 0 3.814 5.592 6.02 6.02 0 0 0 4.375-.003 6.006
 6.006 0 0 0 3.657-6.945zM12 4.227c1.129 0 2.046.917 2.046 2.045a2.046
 2.046 0 0 1-4.092 0c0-1.128.918-2.045 2.046-2.045zm0 11.456a2.32 2.32
 0 0 1 0-4.637c1.282 0 2.318 1.037 2.318 2.318S13.282 15.683 12
 15.683z" />
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
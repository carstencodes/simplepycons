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


class IrobotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "irobot"

    @property
    def original_file_name(self) -> "str":
        return "irobot.svg"

    @property
    def title(self) -> "str":
        return "iRobot"

    @property
    def primary_color(self) -> "str":
        return "#6CB86A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iRobot</title>
     <path d="M23.848
 8.166c.75-3.536-1.287-7.264-5.747-7.264h-6.955l-1.152 5.4h5.246c1.076
 0 1.748.884 1.517 1.941-.23 1.076-1.267 1.903-2.344 1.903H9.11l7.111
 13.143h7.437l-4.806-8.82c1.288-.692 4.21-2.632 4.997-6.303zM1.23
 17.505 0 23.31h6.342l2.767-13.145c-3.863.135-6.9 2.71-7.88 7.34zM5.4
 6.648a2.985 2.985 0 0 0 2.997-2.98A2.986 2.986 0 0 0 5.4.69a2.986
 2.986 0 0 0-2.998 2.98c0 1.633 1.346 2.978 2.998 2.978z" />
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

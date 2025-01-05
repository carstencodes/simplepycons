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


class ScalaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scala"

    @property
    def original_file_name(self) -> "str":
        return "scala.svg"

    @property
    def title(self) -> "str":
        return "Scala"

    @property
    def primary_color(self) -> "str":
        return "#DC322F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scala</title>
     <path d="M4.589 24c4.537 0 13.81-1.516 14.821-3v-5.729c-.957
 1.408-10.284 2.912-14.821 2.912V24zM4.589 16.365c4.537 0 13.81-1.516
 14.821-3V7.636c-.957 1.408-10.284 2.912-14.821 2.912v5.817zM4.589
 8.729c4.537 0 13.81-1.516 14.821-3V0C18.453 1.408 9.126 2.912 4.589
 2.912v5.817z" />
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

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


class SparkArIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sparkar"

    @property
    def original_file_name(self) -> "str":
        return "sparkar.svg"

    @property
    def title(self) -> "str":
        return "Spark AR"

    @property
    def primary_color(self) -> "str":
        return "#FF5C83"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spark AR</title>
     <path d="M3.199 20.001L20.801 12v8.001L11.999 24l-8.8-3.999zm8.8
 3.999zm-.001-24L3.199 3.999V12l17.602-8.001L11.998 0zM3.803
 12.275l7.592 3.453 8.803-4.002-7.594-3.45-8.801 3.999z" />
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

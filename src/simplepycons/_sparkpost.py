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


class SparkpostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sparkpost"

    @property
    def original_file_name(self) -> "str":
        return "sparkpost.svg"

    @property
    def title(self) -> "str":
        return "SparkPost"

    @property
    def primary_color(self) -> "str":
        return "#FA6423"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SparkPost</title>
     <path d="M16.2 9c-1.351.9-1.8 2.7-1.65 3.9-2.25-2.25
 3.45-8.55-3-12.9C15.15 5.4 6 9.75 6 17.4c0 3 1.95 5.701 6 6.6
 4.05-.898 6-3.6 6-6.6 0-4.5-2.7-6-1.8-8.4zM12 20.852c-1.8
 0-3.45-1.5-3.45-3.451 0-1.801 1.5-3.45 3.45-3.45 1.8 0 3.45 1.5 3.45
 3.45-.15 1.951-1.65 3.451-3.45 3.451z" />
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

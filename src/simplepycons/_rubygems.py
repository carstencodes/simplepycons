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


class RubygemsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rubygems"

    @property
    def original_file_name(self) -> "str":
        return "rubygems.svg"

    @property
    def title(self) -> "str":
        return "RubyGems"

    @property
    def primary_color(self) -> "str":
        return "#E9573F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RubyGems</title>
     <path d="M7.81 7.9l-2.97 2.95 7.19 7.18 2.96-2.95
 4.22-4.23-2.96-2.96v-.01H7.8zM12 0L1.53 6v12L12 24l10.47-6V6L12
 0zm8.47 16.85L12 21.73l-8.47-4.88V7.12L12 2.24l8.47 4.88v9.73z" />
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

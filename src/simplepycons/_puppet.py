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


class PuppetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "puppet"

    @property
    def original_file_name(self) -> "str":
        return "puppet.svg"

    @property
    def title(self) -> "str":
        return "Puppet"

    @property
    def primary_color(self) -> "str":
        return "#FFAE1A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Puppet</title>
     <path d="M8.984 21.611H6.595v-2.388h2.39zM6.595
 2.39h2.39v2.388h-2.39zm13.198
 6.028h-5.48l.001-.002-2.941-2.941V0H4.207v7.166h5.48l2.938
 2.938.002-.001v3.794l-.003-.003-2.94
 2.94H4.207V24h7.166v-5.477l2.94-2.94h5.48V8.417" />
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

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


class GoogleKeepIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlekeep"

    @property
    def original_file_name(self) -> "str":
        return "googlekeep.svg"

    @property
    def title(self) -> "str":
        return "Google Keep"

    @property
    def primary_color(self) -> "str":
        return "#FFBB00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Keep</title>
     <path d="M4.908 0c-.904 0-1.635.733-1.635 1.637v20.726c0 .904.732
 1.637 1.635 1.637H19.09c.904 0 1.637-.733
 1.637-1.637V6.5h-6.5V0H4.908zm9.819 0v6h6l-6-6zM11.97 8.229c.224 0
 .571.031.765.072.2.04.576.185.842.312.828.414 1.467 1.164 1.774
 2.088.168.511.188 1.34.05 1.865a3.752 3.752 0 0 1-1.277
 1.952l-.25.193h-1.87c-2.134 0-1.931.042-2.478-.494a3.349 3.349 0 0
 1-.984-1.844c-.148-.766-.053-1.437.32-2.203.19-.399.303-.556.65-.899.68-.679
 1.513-1.037 2.458-1.042zm-1.866 7.863h3.781v1.328h-3.779v-1.328z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://about.google/brand-resource-center/lo'''

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

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


class UnrealEngineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unrealengine"

    @property
    def original_file_name(self) -> "str":
        return "unrealengine.svg"

    @property
    def title(self) -> "str":
        return "Unreal Engine"

    @property
    def primary_color(self) -> "str":
        return "#0E1128"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unreal Engine</title>
     <path d="M12 0a12 12 0 1012 12A12 12 0 0012 0zm0 23.52A11.52
 11.52 0 1123.52 12 11.52 11.52 0 0112
 23.52zm7.13-9.791c-.206.997-1.126 3.557-4.06 4.942l-1.179-1.325-1.988
 2a7.338 7.338 0 01-5.804-2.978 2.859 2.859 0
 00.65.123c.326.006.678-.114.678-.66v-5.394a.89.89 0
 00-1.116-.89c-.92.212-1.656 2.509-1.656 2.509a7.304 7.304 0
 012.528-5.597 7.408 7.408 0 013.73-1.721c-1.006.573-1.57 1.507-1.57
 2.29 0 1.262.76 1.109.984.923v7.28a1.157 1.157 0 00.148.256 1.075
 1.075 0 00.88.445c.76 0 1.747-.868
 1.747-.868V9.172c0-.6-.452-1.324-.905-1.572 0 0 .838-.149
 1.484.346a5.537 5.537 0 01.387-.425c1.508-1.48 2.929-1.902
 4.112-2.112 0 0-2.151 1.69-2.151 3.96 0 1.687.043 5.801.043
 5.801.799.771 1.986-.342 3.059-1.441Z" />
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

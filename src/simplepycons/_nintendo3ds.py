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


class NintendoThreeDsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nintendo3ds"

    @property
    def original_file_name(self) -> "str":
        return "nintendo3ds.svg"

    @property
    def title(self) -> "str":
        return "Nintendo 3DS"

    @property
    def primary_color(self) -> "str":
        return "#D12228"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nintendo 3DS</title>
     <path d="M17.653 16.63a.712.712 0 1 0 1.424 0 .712.712 0 1
 0-1.424 0m-9.45 4.238h7.575c.3 0
 .524-.225.544-.524v-5.175c-.02-.282-.263-.525-.544-.507H8.203a.54.54
 0 0 0-.544.525v5.156c0 .301.244.525.544.525zm13.051-3.525a.729.729 0
 0 0 .73-.729.73.73 0 1 0-.73.729zm-1.443-.019a.714.714 0 1 0 .001
 1.427.714.714 0 0 0-.001-1.427zm-.713-2.137a.712.712 0 1 0 1.424 0
 .712.712 0 1 0-1.424 0M2.54 16.612a1.65 1.65 0 1 0 3.3 0 1.65 1.65 0
 1 0-3.3 0M21.272 0H2.728A2.73 2.73 0 0 0-.01 2.72v18.542C.009 22.781
 1.228 24 2.728 24h18.526a2.753 2.753 0 0 0 2.756-2.719V2.737C23.991
 1.219 22.772 0 21.272 0zm1.913 21.281a1.92 1.92 0 0 1-1.912
 1.912H2.728a1.92 1.92 0 0
 1-1.913-1.912v-8.456h22.369v8.456zm0-9.694H.815v-8.85A1.92 1.92 0 0 1
 2.728.824h18.544c1.049 0 1.912.863 1.912 1.913v8.85 M17.409
 3.112H6.534c-.3 0-.544.263-.544.563V9.15c0
 .3.226.563.544.563h10.875a.548.548 0 0 0 .544-.563V3.656a.543.543 0 0
 0-.544-.544z" />
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

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


class RaylibIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "raylib"

    @property
    def original_file_name(self) -> "str":
        return "raylib.svg"

    @property
    def title(self) -> "str":
        return "Raylib"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Raylib</title>
     <path d="M0 0v24h24V0H0Zm1.5 1.5h21v21h-21v-21Zm14.813
 15.469v3.281h.937v-.469h-.469V16.97h-.468Zm1.406
 0v.468h.468v-.468h-.468Zm.937
 0v3.281H21v-2.344h-1.875v-.937h-.469Zm-10.781.937v2.344h.469v-1.875h1.875v-.469H7.875Zm2.813
 0v.469h1.874v.469h-1.874v1.406h2.343v-2.344h-2.344Zm2.812
 0v2.344h1.875v.469H13.5v.468h2.344v-3.28h-.469v1.874h-1.406v-1.875H13.5Zm4.219
 0v2.344h.468v-2.344h-.468Zm1.406.469h1.406v1.406h-1.406v-1.406Zm-7.969.938h1.406v.468h-1.406v-.468Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/raysan5/raylib/blob/e7a486'''

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

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


class TileIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tile"

    @property
    def original_file_name(self) -> "str":
        return "tile.svg"

    @property
    def title(self) -> "str":
        return "Tile"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tile</title>
     <path d="M7.486 8.483h1.617a.16.16 0 0 1 .15.15v9.706a.16.16 0 0
 1-.15.15H7.486a.162.162 0 0
 1-.15-.15V8.633c0-.075.075-.15.15-.15zm3.536-2.972h1.617c.076 0
 .151.075.151.15v12.64c0 .075-.075.15-.15.15h-1.618a.162.162 0 0
 1-.15-.15V5.66c0-.075.075-.15.15-.15zM5.68 8.483H1.918V5.66a.162.162
 0 0 0-.15-.15H.15a.162.162 0 0 0-.15.15v7.787c0 2.746 2.257 5.003
 5.003 5.003h.677c.075 0 .15-.075.15-.15v-1.618a.162.162 0 0
 0-.15-.15h-.677a3.099 3.099 0 0 1-3.085-3.085v-3.084H5.68c.075 0
 .15-.076.15-.15V8.595c0-.076-.075-.113-.15-.113zM22.533 9.95a5.018
 5.018 0 0 0-7.035 0c-1.956 1.918-1.918 5.078 0 7.034 1.919 1.956
 5.079 1.919 7.035 0a4.48 4.48 0 0 0 .865-1.166.08.08 0 0
 0-.075-.075h-2.07l-.225.075c-1.279
 1.129-3.235.978-4.363-.338-.339-.414-.602-.903-.678-1.43
 0-.075.038-.113.113-.113h7.75c.075 0 .15-.075.15-.15v-.301a5.013
 5.013 0 0 0-1.467-3.536zm-.903 2.257h-5.266c-.076
 0-.113-.038-.113-.113a3.066 3.066 0 0 1 2.708-1.655c1.129 0 2.182.64
 2.709 1.655 0 .038 0 .075-.038.113zM9.404 6.602a1.09 1.09 0 0 1-1.09
 1.09 1.09 1.09 0 0 1-1.091-1.09 1.09 1.09 0 0 1 1.09-1.091 1.09 1.09
 0 0 1 1.091 1.09Z" />
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

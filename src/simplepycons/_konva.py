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


class KonvaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "konva"

    @property
    def original_file_name(self) -> "str":
        return "konva.svg"

    @property
    def title(self) -> "str":
        return "Konva"

    @property
    def primary_color(self) -> "str":
        return "#0D83CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Konva</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm1.391 18.541-.239-3.76-2.391-1.608.152
 5.129-4.325.152-.173-13.409L10.5 4.98l.087 5.346
 2.217-1.608.109-3.781 4.412.283-.348 4.586-2.608 1.608 2.673
 1.174.913 5.694-4.564.259z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/konvajs/konvajs.github.io/'''

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

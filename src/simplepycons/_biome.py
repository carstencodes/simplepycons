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


class BiomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "biome"

    @property
    def original_file_name(self) -> "str":
        return "biome.svg"

    @property
    def title(self) -> "str":
        return "Biome"

    @property
    def primary_color(self) -> "str":
        return "#60A5FA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Biome</title>
     <path d="m12 1.608-5.346 9.259a12.069 12.069 0 0 1
 6.326-.219l1.807.426-1.7 7.208-1.809-.427c-2.224-.524-4.361.644-5.264
 2.507l-1.672-.809c1.276-2.636 4.284-4.232
 7.364-3.505l.847-3.592A10.211 10.211 0 0 0 0 22.392h24L12 1.608Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/biomejs/resources/blob/551'''

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

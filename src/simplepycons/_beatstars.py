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


class BeatstarsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "beatstars"

    @property
    def original_file_name(self) -> "str":
        return "beatstars.svg"

    @property
    def title(self) -> "str":
        return "BeatStars"

    @property
    def primary_color(self) -> "str":
        return "#EB0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BeatStars</title>
     <path d="m17.217 11.996-3.308 1.079v3.478l-2.052-2.818-3.309
 1.079 2.043-2.818-2.043-2.819 3.31 1.08 2.05-2.819v3.487zm0
 0v7.277H6.854V4.584h10.363v7.412l4.585-1.49v-7.67L19.135
 0H2.198v24h16.92l2.684-2.685v-7.83z" />
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

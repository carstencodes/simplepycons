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


class LevelsdotfyiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "levelsdotfyi"

    @property
    def original_file_name(self) -> "str":
        return "levelsdotfyi.svg"

    @property
    def title(self) -> "str":
        return "levels.fyi"

    @property
    def primary_color(self) -> "str":
        return "#788B95"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>levels.fyi</title>
     <path d="M2.494
 18.913h3.52v-3.52c0-.43.35-.78.781-.78h3.52v-3.52c0-.432.35-.783.781-.783h3.52V6.791c0-.432.35-.782.782-.782h3.519V2.49c0-.432.35-.782.782-.782h3.52c.43
 0 .781.35.781.782v20.724c0 .432-.35.782-.782.782H2.494a.782.782 0 0
 1-.782-.782v-3.52c0-.43.35-.78.782-.78ZM.172 15.928a.587.587 0 0 1
 0-.83L15.102.168a.587.587 0 0 1 .83.83l-14.93 14.93c-.23.23-.6.23-.83
 0Z" />
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

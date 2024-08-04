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


class NintendoGamecubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nintendogamecube"

    @property
    def original_file_name(self) -> "str":
        return "nintendogamecube.svg"

    @property
    def title(self) -> "str":
        return "Nintendo GameCube"

    @property
    def primary_color(self) -> "str":
        return "#6A5FBB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nintendo GameCube</title>
     <path d="M6.816 15.126l4.703 2.715v-5.433L6.814
 9.695v5.432zm-2.025 1.168l6.73 3.882v3.82L1.481 18.206V6.616l3.31
 1.91v7.769zM12 6.145L7.298 8.863 12 11.579l4.704-2.717L12
 6.146zm0-2.332l5.659 3.274 3.31-1.91L12 0 1.975 5.79 5.28
 7.695zm7.207 12.48v-3.947l-2.023 1.167v1.614l-4.703
 2.715v.005-5.436L22.518 6.62v11.587L12.48 24v-3.817l6.727-3.887z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.nintendo.com/consumer/systems/nin'''

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

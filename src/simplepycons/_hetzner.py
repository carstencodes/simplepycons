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


class HetznerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hetzner"

    @property
    def original_file_name(self) -> "str":
        return "hetzner.svg"

    @property
    def title(self) -> "str":
        return "Hetzner"

    @property
    def primary_color(self) -> "str":
        return "#D50C2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hetzner</title>
     <path d="M0 0v24h24V0H0zm4.602 4.025h2.244c.509 0
 .716.215.716.717v5.64h8.883v-5.64c0-.509.215-.717.717-.717h2.229c.5 0
 .71.23.724.717v14.516c0 .509-.215.717-.717.717h-2.23c-.51
 0-.717-.215-.717-.717v-5.735H7.562v5.735c0
 .516-.215.717-.716.717H4.602c-.51
 0-.717-.208-.717-.717V4.742c0-.509.207-.717.717-.717z" />
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

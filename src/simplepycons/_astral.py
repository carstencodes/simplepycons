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


class AstralIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "astral"

    @property
    def original_file_name(self) -> "str":
        return "astral.svg"

    @property
    def title(self) -> "str":
        return "Astral"

    @property
    def primary_color(self) -> "str":
        return "#261230"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Astral</title>
     <path d="M1.44 0C.6422 0 0 .6422 0 1.44v21.12C0 23.3578.6422 24
 1.44 24h21.12c.7978 0 1.44-.6422 1.44-1.44V1.44C24 .6422 23.3578 0
 22.56 0Zm4.7998 4.8h11.5199c.7953 0 1.44.6447 1.44
 1.44V19.2h-6.624v-4.32h-1.152v4.32H4.8V6.24c0-.7953.6446-1.44
 1.4398-1.44m4.032 5.472v1.152h3.456v-1.152z" />
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

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


class FonomaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fonoma"

    @property
    def original_file_name(self) -> "str":
        return "fonoma.svg"

    @property
    def title(self) -> "str":
        return "Fonoma"

    @property
    def primary_color(self) -> "str":
        return "#02B78F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fonoma</title>
     <path d="M19.706 21.919a4.295 4.295 0 0 0 4.293-4.296 4.295 4.295
 0 1 0-4.293 4.296zM4.296 10.672a4.295 4.295 0 0 0 4.293-4.295 4.295
 4.295 0 1 0-4.294 4.295zm10.412 0h4.975a4.277 4.277 0 0 0 4.293-4.295
 4.277 4.277 0 0 0-4.293-4.296h-4.975a4.277 4.277 0 0 0-4.294 4.296
 4.277 4.277 0 0 0 4.294 4.295zM4.295 21.92h4.976a4.277 4.277 0 0 0
 4.293-4.296 4.277 4.277 0 0 0-4.293-4.295H4.295a4.277 4.277 0 0
 0-4.293 4.295c.068 2.318 1.976 4.296 4.293 4.296z" />
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

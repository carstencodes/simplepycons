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


class TyperIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "typer"

    @property
    def original_file_name(self) -> "str":
        return "typer.svg"

    @property
    def title(self) -> "str":
        return "Typer"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Typer</title>
     <path d="M21.818 3.646H2.182C.982 3.646 0 4.483 0
 5.505v3.707h2.182V5.486h19.636v13.036H2.182v-3.735H0v3.726c0
 1.022.982 1.84 2.182 1.84h19.636c1.2 0 2.182-.818
 2.182-1.84V5.505c0-1.032-.982-1.859-2.182-1.859Zm-10.909 12.07L15.273
 12l-4.364-3.717v2.787H0v1.859h10.909v2.787Z" />
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

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


class QuartoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quarto"

    @property
    def original_file_name(self) -> "str":
        return "quarto.svg"

    @property
    def title(self) -> "str":
        return "Quarto"

    @property
    def primary_color(self) -> "str":
        return "#39729E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quarto</title>
     <path d="M12.65 12.854V24c6.042-.325 10.923-5.105
 11.33-11.125H12.65Zm-1.504 0H.02c.427 5.94 5.166 10.699 11.105
 11.105V12.854Zm1.505-1.505H24C23.675 5.247 18.753.325 12.65 0Zm-1.505
 0V0C5.106.427.326 5.308 0 11.35Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/quarto-dev/quarto-web/blob'''

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

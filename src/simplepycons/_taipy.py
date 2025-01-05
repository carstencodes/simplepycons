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


class TaipyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "taipy"

    @property
    def original_file_name(self) -> "str":
        return "taipy.svg"

    @property
    def title(self) -> "str":
        return "Taipy"

    @property
    def primary_color(self) -> "str":
        return "#FF371A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Taipy</title>
     <path d="M1.273 4.153a.971.971 0 0 1 .917-.65h21.325a.486.486 0 0
 1 .458.646l-1.245 3.56a.971.971 0 0 1-.917.65H.486a.486.486 0 0
 1-.459-.646Zm4.855 6.07a.971.971 0 0 1 .917-.65h8.337a.486.486 0 0 1
 .458.645l-1.245 3.56a.971.971 0 0 1-.917.65H5.341a.486.486 0 0
 1-.458-.646Zm2.698 6.068a.971.971 0 0 1 .917-.65h3.482a.486.486 0 0 1
 .458.646l-1.246 3.56a.971.971 0 0 1-.916.65H8.039a.486.486 0 0
 1-.458-.646Z" />
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

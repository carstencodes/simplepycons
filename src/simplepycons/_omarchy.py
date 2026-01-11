#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class OmarchyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "omarchy"

    @property
    def original_file_name(self) -> "str":
        return "omarchy.svg"

    @property
    def title(self) -> "str":
        return "Omarchy"

    @property
    def primary_color(self) -> "str":
        return "#9ECE6A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Omarchy</title>
     <path d="M0
 0v24h12.8v-3.2h8V3.2h-3.2v1.6h1.6v14.4H4.8V4.8h8V1.6h9.6v20.8h-8V24H24V0Zm1.6
 1.6h9.6v1.6h-8v8H1.6Zm0 11.2h1.6v8h8v1.6H1.6Z" />
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

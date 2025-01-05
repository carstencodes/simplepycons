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


class NamebaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "namebase"

    @property
    def original_file_name(self) -> "str":
        return "namebase.svg"

    @property
    def title(self) -> "str":
        return "Namebase"

    @property
    def primary_color(self) -> "str":
        return "#0068FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Namebase</title>
     <path d="M23.0978 2.406c0 1.3288-1.0516 2.406-2.3488
 2.406s-2.3487-1.0772-2.3487-2.406S19.4519 0 20.7491 0s2.3487 1.0772
 2.3487 2.406zm-11.5089.5415C5.6868 2.9475.9022 7.8488.9022
 13.8948V24h6.5764V13.8948c0-2.3254 1.8403-4.2105 4.1103-4.2105s4.1103
 1.8851 4.1103
 4.2105V24h6.5764V13.8948c0-6.046-4.7846-10.9473-10.6867-10.9473z" />
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

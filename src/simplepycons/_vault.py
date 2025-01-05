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


class VaultIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vault"

    @property
    def original_file_name(self) -> "str":
        return "vault.svg"

    @property
    def title(self) -> "str":
        return "Vault"

    @property
    def primary_color(self) -> "str":
        return "#FFEC6E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vault</title>
     <path d="M0 0l11.955 24L24 0zm13.366
 4.827h1.393v1.38h-1.393zm-2.77
 5.569H9.22V8.993h1.389zm0-2.087H9.22V6.906h1.389zm0-2.086H9.22V4.819h1.389zm2.087
 6.263h-1.377V11.08h1.388zm0-2.09h-1.377V8.993h1.388zm0-2.087h-1.377V6.906h1.388zm0-2.086h-1.377V4.819h1.388zm.683.683h1.393v1.389h-1.393zm0
 3.475V8.993h1.389v1.388Z" />
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

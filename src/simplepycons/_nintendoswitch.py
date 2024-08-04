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


class NintendoSwitchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nintendoswitch"

    @property
    def original_file_name(self) -> "str":
        return "nintendoswitch.svg"

    @property
    def title(self) -> "str":
        return "Nintendo Switch"

    @property
    def primary_color(self) -> "str":
        return "#E60012"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nintendo Switch</title>
     <path d="M14.176 24h3.674c3.376 0 6.15-2.774 6.15-6.15V6.15C24
 2.775 21.226 0 17.85 0H14.1c-.074
 0-.15.074-.15.15v23.7c-.001.076.075.15.226.15zm4.574-13.199c1.351 0
 2.399 1.125 2.399 2.398 0 1.352-1.125 2.4-2.399 2.4-1.35
 0-2.4-1.049-2.4-2.4-.075-1.349 1.05-2.398 2.4-2.398zM11.4
 0H6.15C2.775 0 0 2.775 0 6.15v11.7C0 21.226 2.775 24 6.15
 24h5.25c.074 0 .15-.074.15-.149V.15c.001-.076-.075-.15-.15-.15zM9.676
 22.051H6.15c-2.326 0-4.201-1.875-4.201-4.201V6.15c0-2.326 1.875-4.201
 4.201-4.201H9.6l.076 20.102zM3.75 7.199c0 1.275.975 2.25 2.25
 2.25s2.25-.975 2.25-2.25c0-1.273-.975-2.25-2.25-2.25s-2.25.977-2.25
 2.25z" />
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

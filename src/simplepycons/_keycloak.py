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


class KeycloakIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keycloak"

    @property
    def original_file_name(self) -> "str":
        return "keycloak.svg"

    @property
    def title(self) -> "str":
        return "Keycloak"

    @property
    def primary_color(self) -> "str":
        return "#4D4D4D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keycloak</title>
     <path d="m18.742 1.182-12.493.002C4.155 4.784 2.079 8.393 0
 12.002c2.071 3.612 4.162 7.214 6.252 10.816l12.49-.004
 3.089-5.404h2.158v-.002H24L23.996 6.59h-2.168zM8.327 4.792h2.081l1.04
 1.8-3.12 5.413 3.117 5.403-1.035 1.81H8.327a2047.566 2047.566 0 0
 0-4.168-7.204C5.547 9.606 6.937 7.2 8.327 4.792Zm6.241 0
 2.086.003c1.393 2.405 2.78 4.813 4.166 7.222l-4.167
 7.2h-2.08c-.382-.562-1.038-1.808-1.038-1.808l3.123-5.405-3.124-5.413z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/keycloak/keycloak-misc/blo'''

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

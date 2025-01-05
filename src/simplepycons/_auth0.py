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


class AuthZeroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "auth0"

    @property
    def original_file_name(self) -> "str":
        return "auth0.svg"

    @property
    def title(self) -> "str":
        return "Auth0"

    @property
    def primary_color(self) -> "str":
        return "#EB5424"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Auth0</title>
     <path d="M21.98 7.448L19.62 0H4.347L2.02 7.448c-1.352 4.312.03
 9.206 3.815 12.015L12.007 24l6.157-4.552c3.755-2.81 5.182-7.688
 3.815-12.015l-6.16 4.58 2.343 7.45-6.157-4.597-6.158 4.58
 2.358-7.433-6.188-4.55 7.63-.045L12.008 0l2.356 7.404 7.615.044z" />
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

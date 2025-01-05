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


class FaceitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "faceit"

    @property
    def original_file_name(self) -> "str":
        return "faceit.svg"

    @property
    def title(self) -> "str":
        return "FACEIT"

    @property
    def primary_color(self) -> "str":
        return "#FF5500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FACEIT</title>
     <path d="M23.999 2.705a.167.167 0 00-.312-.1 1141.27 1141.27 0
 00-6.053 9.375H.218c-.221 0-.301.282-.11.352 7.227 2.73 17.667 6.836
 23.5 9.134.15.06.39-.08.39-.18z" />
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

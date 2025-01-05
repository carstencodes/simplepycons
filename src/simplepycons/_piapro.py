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


class PiaproIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "piapro"

    @property
    def original_file_name(self) -> "str":
        return "piapro.svg"

    @property
    def title(self) -> "str":
        return "Piapro"

    @property
    def primary_color(self) -> "str":
        return "#E4007B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Piapro</title>
     <path d="M11.988 0c-4.705 0-8.7 3.492-9.351
 8.168-.06.207-.09.444-.09.68V24l5.21-3.403V9.44c0-2.338 1.893-4.261
 4.231-4.261s4.261 1.894 4.261 4.232c0 2.337-1.894 4.261-4.231
 4.261-.77 0-1.54-.207-2.22-.621v5.563A9.45 9.45 0 0 0 21.191
 11.6C22.405 6.51 19.268 1.45 14.207.266A9.48 9.48 0 0 0 11.988 0Z" />
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

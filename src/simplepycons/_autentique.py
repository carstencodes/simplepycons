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


class AutentiqueIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autentique"

    @property
    def original_file_name(self) -> "str":
        return "autentique.svg"

    @property
    def title(self) -> "str":
        return "Autentique"

    @property
    def primary_color(self) -> "str":
        return "#3379F2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Autentique</title>
     <path d="m18.54 1.225-.27 1.66a10.57 10.57 0 0 0-6.114-2.32L0
 11.99h12.156V6.062c3.199 0 5.74 2.434 5.74 5.917 0 3.687-2.614
 5.98-5.73 5.98-2.594 0-4.648-1.557-5.429-3.898L0 11.984c0 6.43 4.591
 11.45 11.543 11.45 1.666 0 4.259-.383 6.706-2.325l.29 1.64H24V1.225Z"
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

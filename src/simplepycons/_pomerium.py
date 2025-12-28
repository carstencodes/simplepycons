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


class PomeriumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pomerium"

    @property
    def original_file_name(self) -> "str":
        return "pomerium.svg"

    @property
    def title(self) -> "str":
        return "Pomerium"

    @property
    def primary_color(self) -> "str":
        return "#6F43E7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pomerium</title>
     <path d="M0 6.768v2.338l.038-.005A2.832 2.832 0 0 1 3.2
 11.913v7.998h2.318v-9.023A2.687 2.687 0 0 1 7.95 8.213c1.288-.123
 2.345.873 2.345 2.167v9.53h2.317v-9.265c0-1.685 1.271-3.1 2.948-3.281
 1.565-.169 2.922 1.085 2.922 2.66v9.886H20.8v-9.875A3.635 3.635 0 0 1
 24 6.422V4.089z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.pomerium.com/static-img/logo-ligh'''

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

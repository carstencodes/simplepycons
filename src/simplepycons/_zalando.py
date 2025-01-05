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


class ZalandoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zalando"

    @property
    def original_file_name(self) -> "str":
        return "zalando.svg"

    @property
    def title(self) -> "str":
        return "Zalando"

    @property
    def primary_color(self) -> "str":
        return "#FF6900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zalando</title>
     <path d="M5.27 24c-.88
 0-1.36-.2-1.62-.36-.36-.21-1.02-.75-1.62-2.33A27.06 27.06 0 01.49
 12c.02-3.66.59-6.76 1.54-9.3C2.63 1.1 3.29.56 3.65.35 3.91.21 4.39 0
 5.27 0c.33 0 .72.03 1.18.1a26.1 26.1 0 018.7 3.3h.01a26.4 26.4 0
 017.16 6.01c1.06 1.32 1.19 2.17 1.19 2.59 0 .42-.13 1.27-1.19
 2.59a26.4 26.4 0 01-7.16 6h-.01a26.03 26.03 0 01-8.7
 3.3c-.46.08-.85.11-1.18.11z" />
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

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


class TruenasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "truenas"

    @property
    def original_file_name(self) -> "str":
        return "truenas.svg"

    @property
    def title(self) -> "str":
        return "TrueNAS"

    @property
    def primary_color(self) -> "str":
        return "#0095D5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TrueNAS</title>
     <path d="M24 10.049v5.114l-10.949 6.324v-5.114L24 10.049zm-24
 0v5.114l10.956 6.324v-5.114L0 10.049zm12.004-.605l-4.433 2.559 4.433
 2.559 4.429-2.559-4.429-2.559zm10.952-1.207l-9.905-5.723v5.118l5.473
 3.164 4.432-2.559zm-12-.605V2.513L1.044 8.236l4.432 2.555
 5.48-3.159z" />
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

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


class RaribleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rarible"

    @property
    def original_file_name(self) -> "str":
        return "rarible.svg"

    @property
    def title(self) -> "str":
        return "Rarible"

    @property
    def primary_color(self) -> "str":
        return "#FEDA03"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rarible</title>
     <path d="M4.8 0A4.79 4.79 0 000 4.8v14.4A4.79 4.79 0 004.8
 24h14.4a4.79 4.79 0 004.8-4.8V4.8A4.79 4.79 0 0019.2 0zm1.32
 7.68h8.202c2.06 0 3.666.44 3.666 2.334 0 1.137-.671 1.702-1.427
 1.898.904.268 1.558 1 1.558
 2.16v2.131h-3.451V14.18c0-.62-.37-.87-1-.87H9.572v2.893H6.12zm3.452
 2.5v.834h4.155c.452 0 .726-.06.726-.416 0-.358-.274-.418-.726-.418z"
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

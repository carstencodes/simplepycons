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


class RatatuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ratatui"

    @property
    def original_file_name(self) -> "str":
        return "ratatui.svg"

    @property
    def title(self) -> "str":
        return "Ratatui"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ratatui</title>
     <path d="M8.16
 13.92h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48H12v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48v.48h.48V24H2.4v-.48h-.48v-.48h-.48v-.48H.96v-.48H.48v-.48H0v-.96h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.96Zm-.96
 6.72h.48v.48h.48v.48h.48v-.96h-.48v-.48h-.48v-.48H7.2Zm0-2.88H5.76v.48h.48v.48h1.92V16.8h-.48v-.48H7.2ZM24
 7.68h-.48V9.6h-.48v.48h-.48v.48h-.48v.48h-.96v.48h-.48V12h-.48v.48h-.48v.48h-.96v4.32h2.4v.48h.48v4.32h-.48v.48h-.48v.96h-.48V24h-.48v-.48h-.48v-.48h-.48v-.48h.48v-.48h.48v-.48h.48v-2.4h-.48v.48h-1.44v.48h-.48v1.44h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48h-.48v-.48H12v-.48h-.48v-.96H12v-.96h.48v-.48h-.96v.48H9.6v-.48h-.48v-.48h-.48v-.48h-.48v-.96h.48v-.48h.48v-.48h.96v-.48h3.36V9.6h.48v-.48h.48v-.48h.48v-.48h.48v-.48h.48V7.2h1.92v-.48h1.44v-.48H24Zm-8.16.96h-.48v.96h.48v.48h.96V9.6h.48v-.96h-.48v-.48h-.96ZM13.92.48h.48V4.8h.48v.48h.48v.96h.48v.96h-.48v.48h-.48v.48h-.48v.48h-.48v.48h-.48v.48H12v-.48h-.48v-.48h-.96v-.48h-.48v-.48H9.6V7.2H6.72v-.48h-.48v-2.4h.48v-.48h.48v-.48h.48v-.48h.48V2.4h.48v-.48h.48v-.48h.48V.96h.48V.48h.96V0h2.88z"
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
        return '''https://github.com/ratatui/ratatui/blob/8e3bd'''

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

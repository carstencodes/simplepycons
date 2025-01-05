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


class KuulaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kuula"

    @property
    def original_file_name(self) -> "str":
        return "kuula.svg"

    @property
    def title(self) -> "str":
        return "Kuula"

    @property
    def primary_color(self) -> "str":
        return "#4092B4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kuula</title>
     <path d="M12 0C5.388 0 0 5.388 0 12s5.388 12 12 12 12-5.388
 12-12S18.612 0 12 0Zm0 2.547A9.433 9.433 0 0 1 21.453 12 9.433 9.433
 0 0 1 12 21.453 9.433 9.433 0 0 1 2.547 12 9.433 9.433 0 0 1 12
 2.547Zm-.606 5.366 4.372-.693 2.01 3.944-3.13 3.13-3.944-2.01z" />
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

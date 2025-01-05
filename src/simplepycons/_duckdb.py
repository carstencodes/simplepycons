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


class DuckdbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "duckdb"

    @property
    def original_file_name(self) -> "str":
        return "duckdb.svg"

    @property
    def title(self) -> "str":
        return "DuckDB"

    @property
    def primary_color(self) -> "str":
        return "#FFF000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DuckDB</title>
     <path d="M12 0C5.363 0 0 5.363 0 12s5.363 12 12 12 12-5.363
 12-12S18.637 0 12 0zM9.502 7.03a4.974 4.974 0 0 1 4.97 4.97 4.974
 4.974 0 0 1-4.97 4.97A4.974 4.974 0 0 1 4.532 12a4.974 4.974 0 0 1
 4.97-4.97zm6.563 3.183h2.351c.98 0 1.787.782 1.787 1.762s-.807
 1.789-1.787 1.789h-2.351v-3.551z" />
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

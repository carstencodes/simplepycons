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


class CratedbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cratedb"

    @property
    def original_file_name(self) -> "str":
        return "cratedb.svg"

    @property
    def title(self) -> "str":
        return "CrateDB"

    @property
    def primary_color(self) -> "str":
        return "#009DC7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CrateDB</title>
    <path d="M18 9V3h-6v6H0v6h6v6h6v-6h12V9h-6z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/crate/crate-docs-theme/blo
b/cbd734b3617489ca937f35e30f37f3f6c1870e1f/src/crate/theme/rtd/crate/s'''

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

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


class WiseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wise"

    @property
    def original_file_name(self) -> "str":
        return "wise.svg"

    @property
    def title(self) -> "str":
        return "Wise"

    @property
    def primary_color(self) -> "str":
        return "#9FE870"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wise</title>
     <path d="M6.488 7.469 0
 15.05h11.585l1.301-3.576H7.922l3.033-3.507.01-.092L8.993
 4.48h8.873l-6.878 18.925h4.706L24 .595H2.543l3.945 6.874Z" />
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

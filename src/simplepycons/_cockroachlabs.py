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


class CockroachLabsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cockroachlabs"

    @property
    def original_file_name(self) -> "str":
        return "cockroachlabs.svg"

    @property
    def title(self) -> "str":
        return "Cockroach Labs"

    @property
    def primary_color(self) -> "str":
        return "#6933FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cockroach Labs</title>
     <path d="M17.645 16.155a13.013 13.013 0 0 0-4.479-13.287 11.617
 11.617 0 0 1 5.815-1.546c.774 0 1.545.075 2.304.226l.32-1.282A13.092
 13.092 0 0 0 18.98 0 12.93 12.93 0 0 0 12 2.03 12.933 12.933 0 0 0
 5.021 0C4.139 0 3.26.089 2.396.266l.319 1.282a11.83 11.83 0 0 1
 2.306-.226 11.64 11.64 0 0 1 5.817 1.544 13.01 13.01 0 0 0 .792
 20.877l.375.257.373-.257c2.624-1.801 4.5-4.5 5.27-7.588zm-6.305
 5.7A11.687 11.687 0 0 1 7.825 9.519a13.08 13.08 0 0 0 2.457 2.977
 3.202 3.202 0 0 1 1.058 2.383zm.661-9.657a11.717 11.717 0 0
 1-2.343-2.315 3.23 3.23 0 0 1 0-3.912 11.67 11.67 0 0 1
 2.347-2.333c.9.671 1.697 1.468 2.37 2.366a3.197 3.197 0 0 1 0 3.832
 11.816 11.816 0 0 1-2.374 2.362zm.659 9.657v-6.976a3.202 3.202 0 0 1
 1.06-2.383 13.026 13.026 0 0 0 2.455-2.977 11.694 11.694 0 0 1-3.515
 12.336Z" />
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

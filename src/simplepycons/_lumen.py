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


class LumenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lumen"

    @property
    def original_file_name(self) -> "str":
        return "lumen.svg"

    @property
    def title(self) -> "str":
        return "Lumen"

    @property
    def primary_color(self) -> "str":
        return "#E74430"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lumen</title>
     <path d="M11.649 0a.75.75 0 00-.342.072l-4.878 2.23a.75.751 0
 10.624 1.366l4.878-2.23A.75.75 0 0011.649 0zm5.624.354a.75.75 0
 00-.341.074L6.425 5.306a.75.75 0 00.632 1.362L17.563 1.79a.75.75 0
 00-.29-1.436zm0 3.002a.75.75 0 00-.341.074L6.425 8.31a.75.75 0 00.632
 1.362l10.506-4.88a.75.75 0 00-.29-1.436zm0 3.002a.75.75 0
 00-.341.074L6.425 11.311a.75.75 0 00.632 1.361l10.506-4.878a.75.75 0
 00-.29-1.436zm.009 3.003a.75.75 0 00-.342.07l-3.753 1.688a.75.75 0
 00-.442.685v3.518a.75.75 0 00.001.047h-1.503a.75.75 0
 000-.047v-2.58a.75.75 0 00-.761-.761.75.75 0 00-.74.761v2.58a.75.75 0
 00.002.047h-.94a.461.461 0 00-.47.555l.19 1.14a.687.687 0
 00.656.557h2.28l-2.537.476a.375.375 0 10.139.737l6.003-1.126a.375.375
 0 00.307-.41.625.625 0 00.092-.232l.19-1.142a.461.461 0
 00-.47-.555h-.94a.75.75 0 00.002-.047V12.29l3.31-1.49a.75.75 0
 00-.274-1.438zm-2.292 9.385a.375.375 0 00-.063.007l-6.004
 1.126a.375.375 0 10.139.737l6.003-1.125a.375.375 0 00-.075-.745zm0
 1.876a.375.375 0 00-.063.008l-6.004 1.125a.375.375 0
 10.139.737l6.003-1.125a.375.375 0 00-.075-.745zm-.743 1.876a.375.375
 0 00-.064.006l-4.471.751a.375.375 0 10.124.74l4.472-.75a.375.375 0
 00-.061-.747z" />
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

#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class VitestIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vitest"

    @property
    def original_file_name(self) -> "str":
        return "vitest.svg"

    @property
    def title(self) -> "str":
        return "Vitest"

    @property
    def primary_color(self) -> "str":
        return "#00FF74"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vitest</title>
     <path d="M11.545 23.3a.613.613 0 0 1-.895.197L.252 15.936A.61.61
 0 0 1 0 15.439V6.325c0-.502.569-.792.975-.497l6.358 4.624c.594.433
 1.432.25 1.793-.39L14.393.7a.62.62 0 0 1 .535-.314h8.455a.613.613 0 0
 1 .537.916z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/voidzero-dev/community-des
ign-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-asse'''

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

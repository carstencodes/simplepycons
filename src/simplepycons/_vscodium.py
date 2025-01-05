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


class VscodiumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vscodium"

    @property
    def original_file_name(self) -> "str":
        return "vscodium.svg"

    @property
    def title(self) -> "str":
        return "VSCodium"

    @property
    def primary_color(self) -> "str":
        return "#2F80ED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VSCodium</title>
     <path d="M11.583.54a1.467 1.467 0 0 0-.441 2.032c2.426 3.758
 2.999 6.592 2.75 9.075-1.004 4.756-3.187 5.721-5.094 5.721-1.863
 0-1.364-3.065.036-3.962.836-.522 1.906-.861 2.728-.861.814 0
 1.474-.658 1.474-1.47 0-.812-.66-1.47-1.474-1.47-.96
 0-1.901.202-2.78.545.18-.847.246-1.762.014-2.735-.352-1.477-1.367-2.889-3.128-4.257a1.476
 1.476 0 0 0-2.069.256c-.5.64-.384 1.564.259 2.063 1.435 1.114 1.908
 1.939 2.07 2.618.162.679.032 1.407-.293 2.408-.416 1.349-.9
 2.553-1.11 3.708-.105.568-.114 1.187-.14
 1.68-1.034-1.006-1.438-2.336-1.438-4.279
 0-.811-.66-1.47-1.474-1.47-.814.001-1.473.659-1.473 1.47 0 2.654.776
 5.179 2.855 6.863 1.883 1.793 6.67 1.13 6.67 4.01 0 .812 1.19 1.208
 2.004 1.208.834 0 1.885-.558 1.885-1.208 0-3.267 3.443-5.253
 9.11-5.244A1.472 1.472 0 0 0 24 15.773 1.472 1.472 0 0 0 22.53
 14.3c-.388 0-.765.013-1.138.035.634-1.49.915-3.13.857-4.903a1.473
 1.473 0 0 0-1.522-1.42 1.472 1.472 0 0 0-1.425 1.517c.076 2.32-.01
 4.393-1.74
 5.485-.49.31-1.062.58-1.604.58.42-1.145.738-2.353.869-3.655.083-.83.091-1.818-.003-2.585-.148-1.188-.325-2.535.126-3.55.405-.874
 1.313-1.24 2.645-1.24.814 0 1.473-.659 1.473-1.47
 0-.811-.659-1.47-1.473-1.47-1.98 0-3.481 1.042-4.332
 2.3-.445-.95-.987-1.929-1.642-2.943a1.474 1.474 0 0 0-2.037-.44z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/VSCodium/vscodium.github.i'''

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

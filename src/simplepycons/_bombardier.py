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


class BombardierIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bombardier"

    @property
    def original_file_name(self) -> "str":
        return "bombardier.svg"

    @property
    def title(self) -> "str":
        return "Bombardier"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bombardier</title>
     <path d="m0 23.24 1.823-1.822c1.823-1.823 3.645-2.127
 6.076-2.127h5.012c2.43 0 3.707-.152 5.681-1.519h.244l-3.342
 3.342c-1.823 1.823-3.646 2.127-6.076 2.127H0ZM5.165 6.533l1.822
 1.822c1.823 1.823 3.646 2.127 6.076 2.127h5.013c2.43 0 3.706.152
 5.681 1.519-1.975 1.367-3.25 1.519-5.681 1.519h-5.013c-2.43
 0-4.253.304-6.076 2.127l-1.822 1.822h9.417c2.43 0 4.254-.303
 6.076-2.126L24
 12l-3.342-3.342c-1.822-1.823-3.645-2.126-6.076-2.126H5.165ZM0
 .759l1.823 1.823C3.646 4.405 5.468 4.71 7.899 4.71h5.012c2.43 0
 3.707.152 5.681 1.519h.244l-3.342-3.342C13.67 1.063 11.848.76
 9.418.76H0Z" />
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

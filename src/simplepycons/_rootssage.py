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


class RootsSageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rootssage"

    @property
    def original_file_name(self) -> "str":
        return "rootssage.svg"

    @property
    def title(self) -> "str":
        return "Roots Sage"

    @property
    def primary_color(self) -> "str":
        return "#525DDC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Roots Sage</title>
     <path d="M7.384 4.232l1.71 5.075-4.478-3.136L0 9.403l1.753
 5.2.01.03H7.3L2.82 17.77l1.754 5.2.01.03h5.705L12 17.925l1.7
 5.045.01.03h5.707l1.763-5.23-4.48-3.137h5.537L24
 9.403l-4.616-3.232-4.479 3.136 1.711-5.075L12 1zm.105
 10.342l1.723-5.111h5.576l1.723 5.111-4.51 3.16z" />
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

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


class CockpitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cockpit"

    @property
    def original_file_name(self) -> "str":
        return "cockpit.svg"

    @property
    def title(self) -> "str":
        return "Cockpit"

    @property
    def primary_color(self) -> "str":
        return "#0066CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cockpit</title>
     <path d="M12 0C5.383 0 0 5.382 0 12s5.383 12 12 12 12-5.383
 12-12S18.617 0 12 0zm0 1.799A10.19 10.19 0 0 1 22.207 12 10.19 10.19
 0 0 1 12 22.201 10.186 10.186 0 0 1 1.799 12 10.186 10.186 0 0 1 12
 1.799zm4.016 5.285c-.49-.018-1.232.368-1.899 1.031l-1.44
 1.43-4.31-1.447-.842.867 3.252 2.47-.728.723a4.747 4.747 0 0
 0-.639.787L7.451 12.8l-.476.484 1.947 1.444 1.424
 1.943.48-.48-.144-1.98c.246-.16.497-.361.74-.603l.765-.76 2.495
 3.274.869-.84-1.455-4.332 1.394-1.385c.89-.885
 1.298-1.92.918-2.322a.547.547 0 0 0-.392-.158z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cockpit-project/cockpit-pr
oject.github.io/blob/b851b3477d90017961ac9b252401c9a6cb6239f1/images/s'''

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

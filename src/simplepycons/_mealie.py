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


class MealieIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mealie"

    @property
    def original_file_name(self) -> "str":
        return "mealie.svg"

    @property
    def title(self) -> "str":
        return "Mealie"

    @property
    def primary_color(self) -> "str":
        return "#E58325"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mealie</title>
     <path d="M6.619 13.59 1.444 8.427c-1.925-1.939-1.925-5.063
 0-6.989l8.666 8.642-3.491 3.51m6.551-.42 8.51 8.49-1.76
 1.74-8.48-8.48-8.502 8.48-1.741-1.74L13.12 9.739l-.25-.272a2.448
 2.448 0 0 1 0-3.472L18.23.6l1.14 1.135-3.99 4.024 1.18 1.161
 3.99-4.012 1.15 1.136-4.01 4 1.15 1.189 4.03-4.017L24 6.377l-5.4
 5.353c-.95.96-2.51.96-3.46 0l-.27-.25z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mealie-recipes/mealie.io/b
lob/5519cac801c116a5688c63d8126c3bf1ce568c58/components/App/Toolbar.vu'''

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

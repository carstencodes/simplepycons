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


class LeafletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leaflet"

    @property
    def original_file_name(self) -> "str":
        return "leaflet.svg"

    @property
    def title(self) -> "str":
        return "Leaflet"

    @property
    def primary_color(self) -> "str":
        return "#199900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Leaflet</title>
     <path d="M17.69 0c-.355.574-8.432 4.74-10.856 8.649-2.424
 3.91-3.116 6.988-2.237 9.882.879 2.893 2.559 2.763 3.516
 3.717.958.954 2.257 2.113 4.332 1.645 2.717-.613 5.335-2.426
 6.638-7.508 1.302-5.082.448-9.533-.103-11.99A35.395 35.395 0 0 0
 17.69 0zm-.138.858l-9.22 21.585-.574-.577Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Leaflet/Leaflet/blob/d843c'''

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

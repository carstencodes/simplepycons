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


class DigikeyElectronicsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "digikeyelectronics"

    @property
    def original_file_name(self) -> "str":
        return "digikeyelectronics.svg"

    @property
    def title(self) -> "str":
        return "Digi-Key Electronics"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Digi-Key Electronics</title>
     <path d="M12.246.221A11.786 11.786 0 0 1 23.89 10.418c.912
 6.593-3.944 12.711-10.558
 13.297-.454.04-.912.063-1.369.064l-10.705.003v-3.749H0V3.987h1.222V.218l11.024.003zM17.9
 19.423l-8.26-7.422 8.25-7.422h-6.938L5.615
 9.361V4.598H.56v14.803h5.105v-4.724l5.289 4.746H17.9z" />
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

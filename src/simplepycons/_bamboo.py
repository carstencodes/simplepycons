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


class BambooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bamboo"

    @property
    def original_file_name(self) -> "str":
        return "bamboo.svg"

    @property
    def title(self) -> "str":
        return "Bamboo"

    @property
    def primary_color(self) -> "str":
        return "#0052CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bamboo</title>
     <path d="M21.7142 13.6433h-4.9888a.651.651 0 00-.655.555 4.1139
 4.1139 0 01-4.0619 3.5299l1.35 6.1728a10.3737 10.3737 0
 009.0077-9.5447.651.651 0
 00-.652-.713zm-8.6327-.158l7.1998-6.1718a.645.645 0
 000-.984L13.0815.1597a.648.648 0 00-1.074.483v12.3426a.651.651 0
 001.073.5zm-11.3547 1.505A10.3847 10.3847 0 0012.0115
 24v-6.2698a4.0929 4.0929 0
 01-4.0999-4.0869zm-.096-1.447v.1h6.2798a4.0929 4.0929 0
 014.098-4.0879l-1.348-6.1698a10.3697 10.3697 0 00-9.0298 10.1577" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.atlassian.design/guidelines/marke'''

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

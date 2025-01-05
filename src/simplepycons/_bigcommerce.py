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


class BigcommerceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bigcommerce"

    @property
    def original_file_name(self) -> "str":
        return "bigcommerce.svg"

    @property
    def title(self) -> "str":
        return "BigCommerce"

    @property
    def primary_color(self) -> "str":
        return "#121118"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BigCommerce</title>
     <path d="M12.645 13.663h3.027c.861 0 1.406-.474 1.406-1.235
 0-.717-.545-1.234-1.406-1.234h-3.027c-.1
 0-.187.086-.187.172v2.125c.015.1.086.172.187.172zm0 4.896h3.128c.961
 0 1.535-.488 1.535-1.35 0-.746-.545-1.35-1.535-1.35h-3.128c-.1
 0-.187.087-.187.173v2.34c.015.115.086.187.187.187zM23.72.053l-8.953
 8.93h1.464c2.281 0 3.63 1.435 3.63 3 0 1.235-.832 2.14-1.722
 2.541-.143.058-.143.259.014.316 1.033.402 1.765 1.48 1.765 2.742 0
 1.78-1.19 3.202-3.5 3.202h-6.342c-.1 0-.187-.086-.187-.172V13.85L.062
 23.64c-.13.13-.043.359.143.359h23.631a.16.16 0 0 0
 .158-.158V.182c.043-.158-.158-.244-.273-.13z" />
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

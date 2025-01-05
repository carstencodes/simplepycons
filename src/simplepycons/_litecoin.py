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


class LitecoinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "litecoin"

    @property
    def original_file_name(self) -> "str":
        return "litecoin.svg"

    @property
    def title(self) -> "str":
        return "Litecoin"

    @property
    def primary_color(self) -> "str":
        return "#A6A9AA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Litecoin</title>
     <path d="M12 0a12 12 0 1012 12A12 12 0 0012 0zm-.2617
 3.6777h2.584a.3425.3425 0 01.33.4356l-2.0312 6.918 1.9062-.582-.4082
 1.3847-1.9238.5605-1.248 4.213h6.6757a.3425.3425 0 01.3282.4374l-.582
 2a.4586.4586 0
 01-.4395.3301H6.7324l1.7227-5.8223-1.9063.5801.42-1.3613 1.9101-.58
 2.4219-8.1798a.4557.4557 0 01.4375-.334Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://litecoin-foundation.org/litecoin-bran'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://litecoin-foundation.org/litecoin-bran'''

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

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


class ValaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vala"

    @property
    def original_file_name(self) -> "str":
        return "vala.svg"

    @property
    def title(self) -> "str":
        return "Vala"

    @property
    def primary_color(self) -> "str":
        return "#7239B3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vala</title>
     <path d="m9.3836 23.9993-.5152-21.859q-2.2504.8435-3.5153
 2.64-1.2509 1.7971-1.2509 4.4689 0 .6092.0629
 1.0002.0776.3748.156.6092.0783.2188.1411.3438.0777.1249.0777.2188-.828
 0-1.4682-.156-.641-.1723-1.0786-.5316-.4222-.3585-.6565-.9529-.2188-.593-.2188-1.4682
 0-1.0624.4524-2.0937.4687-1.0306 1.2657-1.9532.8125-.9211
 1.891-1.7025 1.0942-.7815 2.328-1.344Q8.3044.6409 9.6484.3289 11.0079
 0 12.3519 0q.3593 0 .6565.0155.312.0156.624.0466l.2816
 19.687L20.6481.1554h2.2341L13.9924 24H9.3829Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Vala_'''

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

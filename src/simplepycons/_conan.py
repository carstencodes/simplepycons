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


class ConanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "conan"

    @property
    def original_file_name(self) -> "str":
        return "conan.svg"

    @property
    def title(self) -> "str":
        return "Conan"

    @property
    def primary_color(self) -> "str":
        return "#6699CB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Conan</title>
     <path d="M11.709 0 0 5.534V16.76L11.984
 24l4.857-2.706V9.998c.13-.084.275-.196.399-.27l.032-.017c.197-.11.329-.102.23.33v10.884l6.466-3.603V6.11L24
 6.093Zm.915 2.83c.932.02 1.855.191 2.706.552 1.32.533 2.522 1.364
 3.45 2.429a62.814 62.814 0 0 1-3.044
 1.616c.56-.853.14-2.009-.76-2.455-.93-.648-2.093-.73-3.205-.674-1.064.175-2.258.51-2.893
 1.474-.722.862-.084 2.11.914 2.408 1.2.509 2.543.38
 3.806.413-.975.457-1.931.97-2.927
 1.358-1.701-.176-3.585-.917-4.374-2.51-.574-1.178.215-2.572
 1.319-3.14a11.426 11.426 0 0 1 3.336-1.348 9.212 9.212 0 0 1
 1.672-.123Z" />
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

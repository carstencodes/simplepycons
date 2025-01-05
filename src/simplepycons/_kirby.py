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


class KirbyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kirby"

    @property
    def original_file_name(self) -> "str":
        return "kirby.svg"

    @property
    def title(self) -> "str":
        return "Kirby"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kirby</title>
     <path d="M16.571 12l-2.857
 1.48v.234h2.857V16H7.43v-2.286h2.857v-.25L7.429 12V9.143L12
 11.598l4.571-2.455M12 0l10.286 5.999V18L12 24 1.714 18.001V6zM2.857
 6.682v10.636L12 22.651l9.143-5.333V6.682L12 1.349Z" />
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

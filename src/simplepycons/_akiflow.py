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


class AkiflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "akiflow"

    @property
    def original_file_name(self) -> "str":
        return "akiflow.svg"

    @property
    def title(self) -> "str":
        return "Akiflow"

    @property
    def primary_color(self) -> "str":
        return "#AF38F9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Akiflow</title>
     <path d="M9.425 5.2 5.457 18h5.795l.948-2.99.947
 2.99h5.795L14.974 5.2Zm.836.8h4.124l3.472
 11.2h-4.124l-1.152-3.632Zm-.543.957 2.063 6.728-1.113 3.515H6.543ZM12
 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0Zm0
 .8C18.186.8 23.2 5.813 23.2 12c0 6.186-5.014 11.2-11.2 11.2C5.814
 23.2.8 18.186.8 12 .8 5.814 5.814.8 12 .8Z" />
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

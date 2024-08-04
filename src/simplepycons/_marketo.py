#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class MarketoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "marketo"

    @property
    def original_file_name(self) -> "str":
        return "marketo.svg"

    @property
    def title(self) -> "str":
        return "Marketo"

    @property
    def primary_color(self) -> "str":
        return "#5C4C9F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Marketo</title>
     <path d="M16.146 0v24l6.134-4.886V3.334zM13.293 18.758l-4.939
 2.157V2.086l4.939 1.462zM1.721 18.205l3.78-.999V5.188l-3.762-.606z"
 />
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

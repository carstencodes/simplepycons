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


class AnkermakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ankermake"

    @property
    def original_file_name(self) -> "str":
        return "ankermake.svg"

    @property
    def title(self) -> "str":
        return "AnkerMake"

    @property
    def primary_color(self) -> "str":
        return "#88F387"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AnkerMake</title>
     <path d="m12.35 10.462 3.075 3.122c.187.187.187.42 0 .606l-3.122
 3.123c-.186.186-.42.186-.606 0L8.575 14.19c-.187-.186-.187-.419
 0-.606l3.169-3.122c.186-.186.419-.186.606
 0Zm-1.585-1.584c.14.186.14.419-.047.605l-3.122
 3.123c-.186.186-.419.186-.606 0l-1.724-1.724v12.675H0V.443h2.33l8.435
 8.435ZM21.717.443H24v23.114h-5.266V10.882l-1.724
 1.724c-.187.186-.42.186-.606 0l-3.122-3.123c-.187-.186-.187-.419
 0-.605L21.717.443Z" />
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

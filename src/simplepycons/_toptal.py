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


class ToptalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "toptal"

    @property
    def original_file_name(self) -> "str":
        return "toptal.svg"

    @property
    def title(self) -> "str":
        return "Toptal"

    @property
    def primary_color(self) -> "str":
        return "#3863A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Toptal</title>
     <path d="M20.227 10.038L10.188 0l-2.04 2.04 3.773 3.769-8.155
 8.153L13.807 24l2.039-2.039-3.772-3.771 8.16-8.152h-.007zM8.301
 14.269l6.066-6.063 1.223 1.223-6.064 6.113-1.223-1.26-.002-.013z" />
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

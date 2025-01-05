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


class AlfredIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alfred"

    @property
    def original_file_name(self) -> "str":
        return "alfred.svg"

    @property
    def title(self) -> "str":
        return "Alfred"

    @property
    def primary_color(self) -> "str":
        return "#5C1F87"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alfred</title>
     <path d="m0 15.902c0-1.142 1.133-2.184 3-2.977v-1.827c0-4.142
 4.029-7.5 9-7.5s9 3.358 9 7.5v1.827c1.867.793 3 1.835 3 2.977 0
 2.485-5.373 4.5-12 4.5s-12-2.015-12-4.5z" />
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

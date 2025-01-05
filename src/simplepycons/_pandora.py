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


class PandoraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pandora"

    @property
    def original_file_name(self) -> "str":
        return "pandora.svg"

    @property
    def title(self) -> "str":
        return "Pandora"

    @property
    def primary_color(self) -> "str":
        return "#224099"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pandora</title>
     <path d="M1.882 0v24H8.32a1.085 1.085 0
 001.085-1.085v-4.61h1.612c7.88 0 11.103-4.442 11.103-9.636C22.119
 2.257 17.247 0 12.662 0H1.882Z" />
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

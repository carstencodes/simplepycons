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


class IndieHackersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "indiehackers"

    @property
    def original_file_name(self) -> "str":
        return "indiehackers.svg"

    @property
    def title(self) -> "str":
        return "Indie Hackers"

    @property
    def primary_color(self) -> "str":
        return "#0E2439"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Indie Hackers</title>
     <path d="M0 0h24v24H0V0Zm5.4 17.2h2.4V6.8H5.4v10.4Zm4.8
 0h2.4v-4h3.6v4h2.4V6.8h-2.4v4h-3.6v-4h-2.4v10.4Z" />
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

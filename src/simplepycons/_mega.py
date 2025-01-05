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


class MegaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mega"

    @property
    def original_file_name(self) -> "str":
        return "mega.svg"

    @property
    def title(self) -> "str":
        return "MEGA"

    @property
    def primary_color(self) -> "str":
        return "#D9272E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MEGA</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0zm6.23 16.244a.371.371 0 0
 1-.373.372H16.29a.371.371 0 0
 1-.372-.372v-4.828c0-.04-.046-.06-.08-.033l-3.32 3.32a.742.742 0 0
 1-1.043 0l-3.32-3.32c-.027-.027-.08-.007-.08.033v4.828a.371.371 0 0
 1-.372.372H6.136a.371.371 0 0
 1-.372-.372V7.757c0-.206.166-.372.372-.372h1.076a.75.75 0 0 1
 .525.22l4.13 4.13a.18.18 0 0 0 .26
 0l4.13-4.13c.14-.14.325-.22.525-.22h1.075c.206 0 .372.166.372.372z"
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

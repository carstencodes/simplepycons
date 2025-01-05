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


class BmcSoftwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bmcsoftware"

    @property
    def original_file_name(self) -> "str":
        return "bmcsoftware.svg"

    @property
    def title(self) -> "str":
        return "BMC Software"

    @property
    def primary_color(self) -> "str":
        return "#FE5000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BMC Software</title>
     <path d="M6.375 23.999c-.95
 0-1.95-.749-1.95-2.2v-3.4c0-1.349.85-2.899
 2.05-3.548l4.75-2.8-4.75-2.8C5.325 8.5 4.425 7 4.425 5.65V2.2c0-1.45
 1-2.2 2.002-2.2.4 0 .849.1 1.249.35l10.7 6.35c.75.45 1.15 1.149 1.15
 1.849 0 .75-.452 1.45-1.15 1.85l-2.55 1.5 2.55 1.501c.75.45 1.2 1.15
 1.2 1.85 0 .75-.452 1.45-1.2 1.85L7.674
 23.65c-.45.25-.85.35-1.3.35zm7.15-10.599l-5.85 3.45c-.45.25-.9
 1.05-.9 1.55v3.05l10.15-6zM6.775 2.6v3.05c0 .5.45 1.3.9 1.55l5.85
 3.45 3.45-2.05z" />
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

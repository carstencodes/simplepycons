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


class TedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ted"

    @property
    def original_file_name(self) -> "str":
        return "ted.svg"

    @property
    def title(self) -> "str":
        return "TED"

    @property
    def primary_color(self) -> "str":
        return "#E62B1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TED</title>
     <path d="M0 7.664v2.223h2.43v6.449H5.1v-6.45h2.43V7.665zm7.945
 0v8.672h7.31v-2.223h-4.638v-1.08h4.637v-2.066h-4.637v-1.08h4.637V7.664zm7.759
 0v8.672h3.863c3.024 0 4.433-1.688 4.433-4.349
 0-2.185-1.021-4.323-3.912-4.323zm2.672 2.223h.85c1.931 0 2.102 1.518
 2.102 2.063 0 .815-.243 2.163-1.907 2.163h-1.045z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.ted.com/participate/organize-a-lo
cal-tedx-event/tedx-organizer-guide/branding-promotions/logo-and-desig'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ted.com/participate/organize-a-lo
cal-tedx-event/tedx-organizer-guide/branding-promotions/logo-and-desig'''

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

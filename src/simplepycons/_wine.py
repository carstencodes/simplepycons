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


class WineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wine"

    @property
    def original_file_name(self) -> "str":
        return "wine.svg"

    @property
    def title(self) -> "str":
        return "Wine"

    @property
    def primary_color(self) -> "str":
        return "#800000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wine</title>
     <path d="M11.045 0C8.839.03 5.68 1.06 4.915 2.34c.848 3.193 2.025
 9.576 4.7 12.09.6.565 1.455.785 2.27 1.768l.193.324c.6 1.676 1.371
 3.814.246 5.104-1.833.54-3.08 1.253-2.976 1.78.133.676 2.42.792
 5.107.26 2.687-.53 4.759-1.508
 4.625-2.183-.11-.554-1.672-.73-3.715-.482-1.884-.885-1.955-3.022-2.226-4.674l.025-.4c.116-.556.689-1.793
 1.035-2.393
 1.605-2.779.003-8.337-1.203-13.066-.37-.338-1.088-.479-1.951-.467zm1.832
 3.674c.208-.002.44.052.705.176 2.759 8.733-.429 11.097-1.217
 11.816-2.55-.882-4.278-1.862-6.244-9.312 4.972 2.58 4.744-2.659
 6.756-2.68z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.winehq.org/wine/wine/-/blob/65'''

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

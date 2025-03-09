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


class VelocityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "velocity"

    @property
    def original_file_name(self) -> "str":
        return "velocity.svg"

    @property
    def title(self) -> "str":
        return "Velocity"

    @property
    def primary_color(self) -> "str":
        return "#1BBAE0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Velocity</title>
     <path d="m7.623 6.719-4.752.959a.65.65 0 0 0-.44.324L.083
 12.248a.65.65 0 0 0 .045.701l2.986 4.076a.66.66 0 0 0
 .657.256l4.736-.957a.65.65 0 0 0 .363-.215h11.694a.542.542 0 0 0
 0-1.084h-2.95a.53.53 0 0 1-.394-.152.545.545 0 0 1 0-.78.55.55 0 0 1
 .394-.152h5.875a.53.53 0 0 0 .512-.33v-.422a.53.53 0 0
 0-.512-.33h-9.79a.547.547 0 0 1-.544-.543.54.54 0 0 1
 .543-.54h5.85a.544.544 0 0 0 .525-.542.54.54 0 0
 0-.525-.543H15.68a.54.54 0 1 1 0-1.082h5.86a.546.546 0 0 0
 .524-.543.54.54 0 0 0-.525-.54H9.416L8.279 6.972a.65.65 0 0
 0-.656-.254M7.576 7.77a.527.527 0 0 1 .207.715l-1.451 2.631a.88.88 0
 0 0 .059.945L8.1 14.39a.528.528 0 0 1-.854.623l-1.709-2.326a.88.88 0
 0 0-.88-.344l-2.897.586a.523.523 0 0 1-.621-.412.525.525 0 0 1
 .41-.621l3.14-.635a.9.9 0 0 0 .596-.438l1.576-2.845a.524.524 0 0 1
 .715-.206m13.608 2.92a.54.54 0 1 0-.001 1.082.54.54 0 0 0 0-1.082" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/PaperMC/website/blob/cc46d'''

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

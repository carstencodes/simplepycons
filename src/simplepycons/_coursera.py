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


class CourseraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coursera"

    @property
    def original_file_name(self) -> "str":
        return "coursera.svg"

    @property
    def title(self) -> "str":
        return "Coursera"

    @property
    def primary_color(self) -> "str":
        return "#0056D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coursera</title>
     <path d="M11.374
 23.977c-4.183-.21-8.006-2.626-9.959-6.347-2.097-3.858-1.871-8.864.732-12.454C4.748
 1.338 9.497-.698 14.281.23c4.583.857 8.351 4.494 9.358 8.911 1.122
 4.344-.423 9.173-3.925 12.04-2.289 1.953-5.295 2.956-8.34
 2.797zm7.705-8.05a588.737 588.737 0 0 0-3.171-1.887c-.903 1.483-2.885
 2.248-4.57 1.665-2.024-.639-3.394-2.987-2.488-5.134.801-2.009
 2.79-2.707 4.357-2.464a4.19 4.19 0 0 1 2.623 1.669c1.077-.631
 2.128-1.218 3.173-1.855-2.03-3.118-6.151-4.294-9.656-2.754-3.13
 1.423-4.89 4.68-4.388 7.919.54 3.598 3.73 6.486 7.716 6.404a7.664
 7.664 0 0 0 6.404-3.563z" />
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

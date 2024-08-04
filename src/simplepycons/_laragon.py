#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class LaragonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "laragon"

    @property
    def original_file_name(self) -> "str":
        return "laragon.svg"

    @property
    def title(self) -> "str":
        return "Laragon"

    @property
    def primary_color(self) -> "str":
        return "#0E83CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Laragon</title>
     <path d="M12.843.979c-2.12-.096-3.477 1.439-3.477 1.439C2.52
 2.5.791 8.429.75 8.552l-.248.74c-2.268 8.78 3.889 12.22 3.889
 12.22.188.091.375-.066.375-.066.5-.31.252-.53.252-.53-1.43-1.742-1.595-5.864-1.596-5.899-.64-.532-1.248-1.318-1.111-2.342
 0 0 .084-.51.584-.197 0 0 1.186.644 2.123.83-.001 0 .476.043.5.177 0
 0 .374 1.752-.78 2.32.745.437 1.465.85 1.465.85.124 1.263.81 5.32.81
 5.32.064.797.906.954.906.954.483.172 4.12.062 4.12.062 1.014-.044
 1.062-.953
 1.062-.953.015-.545.03-3.62.03-3.62.096-.575.766-.5.766-.5.703-.03.688.454.688.454-.017.515.045
 3.496.045 3.496.03.858.781 1.125.781 1.125.488 0 .828-.004 1.365 0
 .252.002 1.473 0 1.473 0 .55-.307 1.377-.969 1.377-.969 5.868-4.91
 4.135-11.9 4.135-11.9C22.93 5.88 17.792 5.1 17.792
 5.1c-.582-1.811-1.643-2.682-1.643-2.682-1.222-1.015-2.343-1.396-3.306-1.44zm5.006
 4.273s1.845 3.08-1.727 7.86c.001.001-2.94 4.116-8.232 1.223 1.084.523
 5.536 2.312 8.375-1.98 0 0 2.632-3.437 1.584-7.103zM6.703
 8.868s1.296.036 1.341 1.82c0 0-1.02-2.668-3.271-.2 0 0 .404-1.729
 1.93-1.62z" />
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
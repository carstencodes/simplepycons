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


class DroneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "drone"

    @property
    def original_file_name(self) -> "str":
        return "drone.svg"

    @property
    def title(self) -> "str":
        return "Drone"

    @property
    def primary_color(self) -> "str":
        return "#212121"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Drone</title>
     <path d="M15.07 13.633a3.07 3.07 0 1 1-6.14 0 3.07 3.07 0 0 1
 6.14 0zM12 1.856c5.359.042 11.452 3.82 12 10.94h-7.256S15.809 8.863
 12 8.889s-4.744 3.907-4.744 3.907H0C.353 5.802 6.344 1.812 12
 1.856zM12.05 22.144c-3.996.011-7.729-3.005-9.259-7.674h4.465s.963
 3.889 4.773 3.863 4.716-3.863 4.716-3.863h4.465c-.995 4.94-5.164
 7.664-9.159 7.674z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/drone/brand/tree/f3ba7a1ad'''

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

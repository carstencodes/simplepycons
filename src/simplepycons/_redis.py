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


class RedisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redis"

    @property
    def original_file_name(self) -> "str":
        return "redis.svg"

    @property
    def title(self) -> "str":
        return "Redis"

    @property
    def primary_color(self) -> "str":
        return "#FF4438"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Redis</title>
     <path d="M22.71 13.145c-1.66 2.092-3.452 4.483-7.038 4.483-3.203
 0-4.397-2.825-4.48-5.12.701 1.484 2.073 2.685 4.214 2.63 4.117-.133
 6.94-3.852 6.94-7.239 0-4.05-3.022-6.972-8.268-6.972-3.752 0-8.4
 1.428-11.455 3.685C2.59 6.937 3.885 9.958 4.35 9.626c2.648-1.904
 4.748-3.13 6.784-3.744C8.12 9.244.886 17.05 0 18.425c.1 1.261 1.66
 4.648 2.424 4.648.232 0 .431-.133.664-.365a100.49 100.49 0 0 0
 5.54-6.765c.222 3.104 1.748 6.898 6.014 6.898 3.819 0 7.604-2.756
 9.33-8.965.2-.764-.73-1.361-1.261-.73zm-4.349-5.013c0 1.959-1.926
 2.922-3.685 2.922-.941 0-1.664-.247-2.235-.568 1.051-1.592
 2.092-3.225 3.21-4.973 1.972.334 2.71 1.43 2.71 2.619z" />
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

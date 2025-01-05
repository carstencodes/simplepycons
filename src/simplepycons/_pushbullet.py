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


class PushbulletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pushbullet"

    @property
    def original_file_name(self) -> "str":
        return "pushbullet.svg"

    @property
    def title(self) -> "str":
        return "Pushbullet"

    @property
    def primary_color(self) -> "str":
        return "#4AB367"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pushbullet</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm0 1.688A10.312 10.312 0 0 1 22.312 12 10.312
 10.312 0 0 1 12 22.312 10.312 10.312 0 0 1 1.688 12 10.312 10.312 0 0
 1 12 1.688zM7.258 6.92a.659.772 0 0 0-.659.772v8.643a.603.603 0 0 0
 .603.603h1.733a.603.603 0 0 0 .603-.603V7.692a.659.772 0 0
 0-.658-.772zm6.94.001c-.975.005-1.93.005-2.867.002-.28
 0-.474.254-.534.499a1.7 1.7 0 0 0-.043.405c.004 2.854.007 5.677.007
 8.47 0 .397.21.643.589.641 1.002-.004 1.967-.003 2.895 0 .058 0
 .129.022.176.02.824-.018 1.552-.251 2.182-.698 2.02-1.43 2.554-4.264
 1.662-6.47-.574-1.417-1.743-2.573-3.27-2.82a5.027 5.027 0 0
 0-.797-.049z" />
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

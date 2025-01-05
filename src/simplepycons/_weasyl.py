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


class WeasylIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "weasyl"

    @property
    def original_file_name(self) -> "str":
        return "weasyl.svg"

    @property
    def title(self) -> "str":
        return "Weasyl"

    @property
    def primary_color(self) -> "str":
        return "#990000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Weasyl</title>
     <path d="M21.23 4.156a8.488 8.488 0 0
 0-5.871-1.857c-3.766.243-6.324 2.662-7.364
 6.481-1.28-1.224-1.892-3.238-2.093-5.54-1.02.215-1.658.702-2.233
 1.237.445 2.316 1.802 4.015 3.264 5.158-2.559.317-5.99 2.442-6.771
 4.904-.507 1.598.258 3.415 1.283 4.52 1.237 1.333 3.75 1.998 6.355
 1.754.037.362-.104.536-.058.907 4.067-.306 7.174-1.646 10.04-3.894
 1.119-.877 2.659-2.037 3.756-3.227 1.101-1.192 2.296-2.578
 2.443-4.52.21-2.79-1.236-4.694-2.751-5.923zm-1.434 10.938c-1.035
 1.001-2.241 1.797-3.351 2.675-1.249-1.987-2.583-3.984-3.887-5.917.017
 2.63.006 5.432.04
 7.957-.78.381-1.789.558-2.744.763-1.935-2.917-3.968-5.99-5.961-8.908.693-.447
 1.627-.785 2.478-1.075 1.419 2.05 2.729 4.253 4.171
 6.333.019-3.113-.009-6.673-.061-9.919a14.175 14.175 0 0 0
 1.527-.434c1.813 2.721 3.553 5.628 5.464 8.359a547.35 547.35 0 0
 1-.018-9.768c.858-.282 1.803-.535 2.669-.809.02 3.499-.338 7.128-.327
 10.743z" />
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

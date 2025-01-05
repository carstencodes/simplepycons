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


class LaravelHorizonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "laravelhorizon"

    @property
    def original_file_name(self) -> "str":
        return "laravelhorizon.svg"

    @property
    def title(self) -> "str":
        return "Laravel Horizon"

    @property
    def primary_color(self) -> "str":
        return "#405263"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Laravel Horizon</title>
     <path d="M20.486 3.516C15.8-1.171 8.202-1.172 3.516 3.513A11.963
 11.963 0 0 0 0 11.998a11.975 11.975 0 0 0 4.2 9.13h.01a12 12 0 0 0
 16.274-.642c4.687-4.685 4.688-12.283.002-16.97zM16 13.998c-4
 0-4-4-8-4-2.5 0-3.44 1.565-4.765 2.74H3.23a8.801 8.801 0 0 1
 17.54-1.48c-1.33 1.175-2.27 2.74-4.77 2.74z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/laravel/horizon/blob/79ed5'''

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

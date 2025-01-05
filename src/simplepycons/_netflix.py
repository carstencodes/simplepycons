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


class NetflixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "netflix"

    @property
    def original_file_name(self) -> "str":
        return "netflix.svg"

    @property
    def title(self) -> "str":
        return "Netflix"

    @property
    def primary_color(self) -> "str":
        return "#E50914"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Netflix</title>
     <path d="M5.398 0v.006c3.028 8.556 5.37 15.175 8.348 23.596
 2.344.058 4.85.398 4.854.398-2.8-7.924-5.923-16.747-8.487-24zm8.489
 0v9.63L18.6 22.951c-.043-7.86-.004-15.913.002-22.95zM5.398
 1.05V24c1.873-.225 2.81-.312 4.715-.398v-9.22z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.netflix.com/en/assets/brand-sym'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brand.netflix.com/en/assets/brand-sym'''

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

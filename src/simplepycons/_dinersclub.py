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


class DinersClubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dinersclub"

    @property
    def original_file_name(self) -> "str":
        return "dinersclub.svg"

    @property
    def title(self) -> "str":
        return "Diners Club"

    @property
    def primary_color(self) -> "str":
        return "#004C97"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Diners Club</title>
     <path d="M16.506 11.982a6.026 6.026 0 0 0-3.866-5.618V17.6a6.025
 6.025 0 0 0 3.866-5.618zM8.33 17.598V6.365a6.03 6.03 0 0 0-3.863
 5.617 6.028 6.028 0 0 0 3.863 5.616zm2.156-15.113A9.497 9.497 0 0 0
 .99 11.982a9.495 9.495 0 0 0 9.495 9.494c5.245 0 9.495-4.25
 9.496-9.494a9.499 9.499 0 0 0-9.496-9.497Zm-.023 19.888C4.723 22.4 0
 17.75 0 12.09 0 5.905 4.723 1.626 10.463 1.627h2.69C18.822 1.627 24
 5.903 24 12.09c0 5.658-5.176 10.283-10.848 10.283" />
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

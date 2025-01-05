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


class MotorolaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "motorola"

    @property
    def original_file_name(self) -> "str":
        return "motorola.svg"

    @property
    def title(self) -> "str":
        return "Motorola"

    @property
    def primary_color(self) -> "str":
        return "#E1140A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Motorola</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12C24.002 5.375 18.632.002 12.007 0H12zm7.327
 18.065s-.581-2.627-1.528-4.197c-.514-.857-1.308-1.553-2.368-1.532-.745
 0-1.399.423-2.2 1.553-.469.77-.882 1.573-1.235 2.403 0
 0-.29-.675-.63-1.343a8.038 8.038 0 0
 0-.605-1.049c-.804-1.13-1.455-1.539-2.2-1.553-1.049-.021-1.854.675-2.364
 1.528-.948 1.574-1.528 4.197-1.528 4.197h-.864l4.606-15.12 3.56
 11.804.024.021.024-.021 3.56-11.804 4.61 15.113h-.862z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://motorola-global-portal-de.custhelp.co'''

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

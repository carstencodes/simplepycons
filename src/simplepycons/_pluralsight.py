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


class PluralsightIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pluralsight"

    @property
    def original_file_name(self) -> "str":
        return "pluralsight.svg"

    @property
    def title(self) -> "str":
        return "Pluralsight"

    @property
    def primary_color(self) -> "str":
        return "#F15B2A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pluralsight</title>
     <path d="M15.72 1.755C10.08-.301 3.811 2.625 1.771 8.25c-2.071
 5.699.854 11.956 6.494 14.01 5.655 2.055 11.956-.87 14.01-6.51
 2.057-5.67-.87-11.939-6.524-13.995h-.031zM12 24C5.4 24 0 18.6 0
 12S5.4 0 12 0s12 5.4 12 12-5.4 12-12 12M8.926 5.805v12.391L19.68 12
 8.926 5.805zm1.049 1.769L17.625 12l-7.65 4.426V7.574M6.449
 7.155v9.689L14.85 12 6.449 7.155zm1.051 1.8L12.811 12 7.5
 15.061V8.939" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.pluralsight.com/newsroom/brand-as'''

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

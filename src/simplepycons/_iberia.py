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


class IberiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iberia"

    @property
    def original_file_name(self) -> "str":
        return "iberia.svg"

    @property
    def title(self) -> "str":
        return "Iberia"

    @property
    def primary_color(self) -> "str":
        return "#D7192D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iberia</title>
     <path d="M9.356 11.563c4.53-3.254 9.047-5.217 13.547-5.723L24
 2.978c-6.662 0-7.57 1.457-9.873 3.752M0 21.021c14.719 0 18.189-3.46
 20.213-8.17l1.7-4.434c-4.958.143-12.441 3.066-17.673 8.324" />
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

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


class AvmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "avm"

    @property
    def original_file_name(self) -> "str":
        return "avm.svg"

    @property
    def title(self) -> "str":
        return "AVM"

    @property
    def primary_color(self) -> "str":
        return "#E2001A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AVM</title>
     <path d="m19.501 11.786-.003-4.823-10.9
 11.925h3.172l5.481-6.07v4.864l4.321-4.783v3.657H24V6.86zm-2.643-6.675-5.267
 5.87V7.443H9.345v9.38L20.049 5.111zM0
 16.556h3.148l2.924-3.25v3.25H8.41v-9.21z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://business.avm.de/de/data/allgemeine-nu'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.fritz.com/about-avm/press/press-me'''

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

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


class AdonisjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adonisjs"

    @property
    def original_file_name(self) -> "str":
        return "adonisjs.svg"

    @property
    def title(self) -> "str":
        return "AdonisJS"

    @property
    def primary_color(self) -> "str":
        return "#5A45FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AdonisJS</title>
     <path d="M0 12c0 9.68 2.32 12 12 12s12-2.32 12-12S21.68 0 12 0 0
 2.32 0 12Zm4.84 2.492 3.762-8.555C9.238 4.498 10.46 3.716 12
 3.716c1.54 0 2.762.781 3.398 2.223l3.762 8.554c.172.418.32.953.32
 1.418 0 2.125-1.492 3.617-3.617 3.617-.726
 0-1.3-.183-1.883-.37-.597-.192-1.203-.387-1.98-.387-.77
 0-1.39.195-1.996.386-.59.188-1.168.371-1.867.371-2.125
 0-3.617-1.492-3.617-3.617 0-.465.148-1 .32-1.418ZM12 7.43l-3.715
 8.406c1.102-.512 2.371-.758 3.715-.758 1.297 0 2.613.246 3.664.758Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://adonisjs.notion.site/adonisjs/Welcome
-to-the-AdonisJS-Brand-Assets-Guidelines-a042a6d0be7640c6bc78eb32e1bba'''
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

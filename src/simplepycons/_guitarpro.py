#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GuitarProIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "guitarpro"

    @property
    def original_file_name(self) -> "str":
        return "guitarpro.svg"

    @property
    def title(self) -> "str":
        return "Guitar Pro"

    @property
    def primary_color(self) -> "str":
        return "#569FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Guitar Pro</title>
     <path d="M11.998 0C6.422 0 1.773 3.573 1.773 7.295S8.561 23.973
 11.998 24c3.435.027 10.218-12.971 10.229-16.705C22.227 3.575 17.575 0
 11.998 0zm3.842 5.078a2.292 2.292 0 0 1 2.389 2.34l.007 1.783a2.267
 2.267 0 0 1-2.265 2.342 2.364 2.364 0 0
 1-1.772-.799v3.115l-1.746.239V5.375l1.688-.287.058.785a2.292 2.292 0
 0 1 1.64-.795zm-5.555.035h1.7l-.005 5.953c0 1.736-.931 2.973-2.58
 2.973a4.946 4.946 0 0 1-2.423-.523l.207-1.748a3.297 3.297 0 0 0
 1.996.843.946.946 0 0 0 1.056-.998v-.904l-.011.014a2.333 2.333 0 0
 1-1.77.806 2.28 2.28 0 0 1-2.26-2.345V7.47a2.285 2.285 0 0 1
 4.03-1.551zM9.082 6.385a1.156 1.156 0 0 0-1.139 1.273v1.26a1.164
 1.164 0 0 0 1.139 1.258 1.183 1.183 0 0 0 1.154-1.139V7.55a1.158
 1.158 0 0 0-1.154-1.153zm5.98.008a1.152 1.152 0 0 0-.874
 1.228v1.33a1.18 1.18 0 0 0 1.152 1.26 1.166 1.166 0 0 0
 1.14-1.26v-1.33a1.152 1.152 0 0 0-1.418-1.228z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.guitar-pro.com/c/12-visual-resour'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.guitar-pro.com/c/12-visual-resour'''

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
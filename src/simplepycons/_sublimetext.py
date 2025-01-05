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


class SublimeTextIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sublimetext"

    @property
    def original_file_name(self) -> "str":
        return "sublimetext.svg"

    @property
    def title(self) -> "str":
        return "Sublime Text"

    @property
    def primary_color(self) -> "str":
        return "#FF9800"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sublime Text</title>
     <path d="M20.953.004a.397.397 0 0 0-.18.017L3.225
 5.585c-.175.055-.323.214-.402.398a.42.42 0 0 0-.06.22v5.726a.42.42 0
 0 0 .06.22c.079.183.227.341.402.397l7.454 2.364-7.454
 2.363c-.255.08-.463.374-.463.655v5.688c0
 .282.208.444.463.363l17.55-5.565c.237-.075.426-.336.452-.6.003-.022.013-.04.013-.065V12.06c0-.281-.208-.575-.463-.656L13.4
 9.065l7.375-2.339c.255-.08.462-.375.462-.656V.384c0-.211-.117-.355-.283-.38z"
 />
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

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


class StylelintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stylelint"

    @property
    def original_file_name(self) -> "str":
        return "stylelint.svg"

    @property
    def title(self) -> "str":
        return "stylelint"

    @property
    def primary_color(self) -> "str":
        return "#263238"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>stylelint</title>
     <path d="M3.415.549L0 3.712 2.242 5.65.547 7.483l11.176
 15.909h.114c-2.625-9.386-2.55-9.428-4.446-16.12l-.456.263c-.248.143-.451.026-.451-.26V4.084C5.98
 2.321 5.586.958 5.47.549zm15.115 0c-.116.41-.51 1.772-1.014
 3.535v3.191c0 .286-.203.403-.45.26l-.457-.264c-1.897 6.693-1.821
 6.735-4.446 16.12-.017.07.06.09.114 0L23.453 7.484 21.757 5.65 24
 3.712 20.585.549zm-11.496.75c-.118.007-.2.105-.2.271v5.127c0
 .242.172.34.38.22l3.068-1.772a.336.336 0
 01-.086-.222V3.287c0-.067.021-.129.056-.182L7.215 1.35a.333.333 0
 00-.18-.051zm9.939 0a.331.331 0 00-.18.052l-3.038 1.753a.33.33 0
 01.057.183v1.636a.335.335 0 01-.088.223l3.068
 1.77c.21.122.38.023.38-.218V1.57c0-.166-.08-.264-.199-.27zm-6.35
 1.863c-.101 0-.183.056-.183.125v1.636c0
 .069.082.125.183.125h2.761c.101 0
 .184-.056.184-.125V3.287c0-.07-.083-.125-.184-.125zm1.294
 3.642a.829.829 0 00-.83.83.829.829 0 00.83.828.829.829 0
 00.829-.829.829.829 0 00-.83-.829zm-.01 4.93a.829.829 0
 00-.82.829.829.829 0 00.83.829.829.829 0 00.828-.83.829.829 0
 00-.829-.828.829.829 0 00-.009 0zm.01 4.93a.829.829 0
 00-.83.828.829.829 0 00.83.83.829.829 0 00.829-.83.829.829 0
 00-.83-.829z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/stylelint/stylelint/blob/1
f7bbb2d189b3e27b42de25f2948e3e5eec1b759/identity/stylelint-icon-black.'''

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

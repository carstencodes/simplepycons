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


class MicroEditorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "microeditor"

    @property
    def original_file_name(self) -> "str":
        return "microeditor.svg"

    @property
    def title(self) -> "str":
        return "Micro Editor"

    @property
    def primary_color(self) -> "str":
        return "#2E3192"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Micro Editor</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0Zm5.698 13.628c-.117.465-.303.837-.558
 1.14-.233.302-.466.488-.721.58-.256.094-.512.14-.791.14-.28
 0-.512-.046-.698-.162-.186-.093-.325-.256-.442-.442a1.922 1.922 0 0
 1-.232-.675 4.688 4.688 0 0 1-.07-.837c0-.116
 0-.232.023-.395.022-.163.047-.372.07-.372h-.047c-.373.93-.883
 1.604-1.534 2.14-.652.534-1.372.79-2.164.79-.535
 0-.977-.21-1.28-.605-.325-.395-.487-1-.487-1.79 0-.117
 0-.233.022-.373.023-.116.023-.162.046-.395h-.163c-.209.465-.395
 1.116-.534 1.698-.14.58-.255 1.116-.326 1.604-.093.489-.14.93-.186
 1.303-.047.372-.07.628-.093.767.023.116.046.233.07.372.046.14.07.28.116.396.046.116.07.255.093.372.023.116.046.209.046.279
 0 .325-.07.58-.209.744-.14.162-.302.255-.465.255a.83.83 0 0
 1-.535-.186c-.163-.14-.232-.35-.232-.628
 0-.396.07-.907.21-1.512.14-.604.348-1.372.604-2.279.14-.418.255-.837.395-1.256.14-.418.256-.814.372-1.162.116-.35.21-.675.302-.954a3.71
 3.71 0 0 0
 .163-.65c.023-.07.047-.234.07-.466.023-.233.046-.489.093-.79.046-.303.07-.629.116-.954.047-.35.093-.652.116-.93.047-.21.07-.443.117-.698.046-.255.116-.512.209-.72.093-.233.233-.42.395-.583.163-.162.372-.232.628-.232.28
 0
 .465.093.558.256.093.162.14.372.117.604-.023.233-.047.49-.117.744-.07.256-.14.49-.21.675-.185.581-.371
 1.116-.58 1.558-.21.442-.396.93-.558 1.442-.14.35-.186.674-.186.953 0
 .512.162.884.465 1.163.325.28.697.395 1.14.395a1.63 1.63 0 0 0
 1.022-.372c.326-.255.628-.558.907-.907.28-.348.512-.72.698-1.14a8.3
 8.3 0 0 0
 .419-1.069c.023-.046.046-.14.07-.325.046-.187.07-.396.116-.628.046-.233.093-.465.14-.72.046-.257.091-.466.116-.629.046-.186.07-.372.116-.605.046-.232.116-.442.21-.65.092-.21.232-.373.371-.513a.87.87
 0 0 1 .605-.209c.302 0 .488.093.605.256.093.163.14.372.14.605a3.58
 3.58 0 0 1-.117.697c-.07.233-.116.42-.163.558a23.236 23.236 0 0
 1-.558 1.558c-.186.466-.349.884-.512
 1.21-.14.349-.256.604-.349.814-.093.21-.14.349-.14.418 0 .605.14
 1.047.396 1.303.256.255.535.395.837.395.512 0 .907-.163
 1.21-.465.302-.326.535-.907.674-1.605h.186a5.386 5.386 0 0 1-.14
 1.698z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/zyedidia/micro/blob/486459'''

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

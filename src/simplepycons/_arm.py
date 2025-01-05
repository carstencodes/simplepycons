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


class ArmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arm"

    @property
    def original_file_name(self) -> "str":
        return "arm.svg"

    @property
    def title(self) -> "str":
        return "Arm"

    @property
    def primary_color(self) -> "str":
        return "#0091BD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Arm</title>
     <path d="M5.419
 8.534h1.614v6.911H5.419v-.72c-.71.822-1.573.933-2.07.933C1.218 15.658
 0 13.882 0 11.985c0-2.253 1.542-3.633 3.37-3.633.507 0 1.4.132
 2.049.984zm-3.765 3.491c0 1.198.751 2.202 1.918 2.202 1.015 0
 1.959-.74 1.959-2.181
 0-1.512-.934-2.233-1.959-2.233-1.167-.01-1.918.974-1.918
 2.212zm7.297-3.49h1.613v.618a3 3 0 0 1
 .67-.578c.314-.183.619-.233.984-.233.396 0 .822.06 1.269.324l-.66
 1.462a1.432 1.432 0 0 0-.822-.244c-.345
 0-.69.05-1.005.376-.446.477-.446 1.136-.446 1.593v3.582H8.94zm5.56
 0h1.614v.639c.538-.66 1.177-.822 1.705-.822.72 0 1.4.345 1.786
 1.015.579-.822 1.441-1.015 2.05-1.015.842 0 1.573.396 1.969
 1.086.132.233.365.74.365
 1.745v4.272h-1.614V11.65c0-.771-.08-1.086-.152-1.228-.101-.264-.345-.609-.923-.609-.396
 0-.741.213-.954.508-.284.395-.315.984-.315
 1.572v3.562H18.43V11.65c0-.771-.081-1.086-.152-1.228-.102-.264-.345-.609-.924-.609-.396
 0-.74.213-.954.508-.284.395-.314.984-.314 1.572v3.562h-1.573z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.arm.com/company/policies/trademar'''
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

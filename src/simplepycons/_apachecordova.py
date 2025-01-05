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


class ApacheCordovaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachecordova"

    @property
    def original_file_name(self) -> "str":
        return "apachecordova.svg"

    @property
    def title(self) -> "str":
        return "Apache Cordova"

    @property
    def primary_color(self) -> "str":
        return "#E8E8E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Cordova</title>
     <path
 d="M18.545,0.545H5.455L0,9.273l2.182,14.182h3.886l-0.273-3.273h1.909l0.273,3.273
 h8.045l0.273-3.273h1.909l-0.273,3.273h3.886L24,9.273L18.545,0.545z
 M18.545,18H5.455L4.364,9.273l2.182-4.364h3.506L9.818,6.545
 h4.364l-0.234-1.636h3.506l2.182,4.364L18.545,18z
 M15.545,11.045c0.301,0,0.545,0.908,0.545,2.029
 c0,1.121-0.244,2.029-0.545,2.029c-0.301,0-0.545-0.908-0.545-2.029C15,11.954,15.244,11.045,15.545,11.045z
 M8.659,11.215
 c0.301,0,0.545,0.908,0.545,2.029c0,1.121-0.244,2.029-0.545,2.029c-0.301,0-0.545-0.908-0.545-2.029
 C8.114,12.123,8.358,11.215,8.659,11.215z" />
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

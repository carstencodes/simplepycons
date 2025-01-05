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


class ArduinoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arduino"

    @property
    def original_file_name(self) -> "str":
        return "arduino.svg"

    @property
    def title(self) -> "str":
        return "Arduino"

    @property
    def primary_color(self) -> "str":
        return "#00878F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Arduino</title>
     <path d="M18.087 6.146c-.3 0-.607.017-.907.069-2.532.367-4.23
 2.239-5.18 3.674-.95-1.435-2.648-3.307-5.18-3.674a6.49 6.49 0 0
 0-.907-.069C2.648 6.146 0 8.77 0 12s2.656 5.854 5.913 5.854c.3 0
 .607-.017.916-.069 2.531-.376 4.23-2.247 5.18-3.683.949 1.436 2.647
 3.307 5.18 3.683.299.043.607.069.915.069C21.344 17.854 24 15.23 24
 12s-2.656-5.854-5.913-5.854zM6.53 15.734a3.837 3.837 0 0
 1-.625.043c-2.148 0-3.889-1.7-3.889-3.777 0-2.085 1.749-3.777
 3.898-3.777.208 0 .416.017.624.043 2.39.35 3.847 2.768 4.347
 3.734-.508.974-1.974 3.384-4.355 3.734zm11.558.043c-.208
 0-.416-.017-.624-.043-2.39-.35-3.856-2.768-4.347-3.734.491-.966
 1.957-3.384 4.347-3.734.208-.026.416-.043.624-.043 2.149 0 3.89 1.7
 3.89 3.777 0 2.085-1.75 3.777-3.89
 3.777zm1.65-4.404v1.134h-1.205v1.182h-1.156v-1.182H16.17v-1.134h1.206V10.19h1.156v1.183h1.206zM4.246
 12.498H7.82v-1.125H4.245v1.125z" />
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

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


class MqttIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mqtt"

    @property
    def original_file_name(self) -> "str":
        return "mqtt.svg"

    @property
    def title(self) -> "str":
        return "MQTT"

    @property
    def primary_color(self) -> "str":
        return "#660066"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MQTT</title>
     <path d="M10.657 23.994h-9.45A1.212 1.212 0 0 1 0
 22.788v-9.18h.071c5.784 0 10.504 4.65 10.586 10.386Zm7.606
 0h-4.045C14.135 16.246 7.795 9.977 0 9.942V6.038h.071c9.983 0 18.121
 8.044 18.192 17.956Zm4.53 0h-.97C21.754 12.071 11.995 2.407 0
 2.372v-1.16C0 .55.544.006 1.207.006h7.64C15.733 2.49 21.257 7.789 24
 14.508v8.291c0 .663-.544 1.195-1.207 1.195ZM16.713.006h6.092A1.19
 1.19 0 0 1 24 1.2v5.914c-.91-1.242-2.046-2.65-3.158-3.762C19.588 2.11
 18.122.987 16.714.005Z" />
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

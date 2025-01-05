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


class BabylondotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "babylondotjs"

    @property
    def original_file_name(self) -> "str":
        return "babylondotjs.svg"

    @property
    def title(self) -> "str":
        return "Babylon.js"

    @property
    def primary_color(self) -> "str":
        return "#BB464B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Babylon.js</title>
     <path d="M12 0 1.607 6.002v12L12 24l10.393-6V6L19.14 4.123 16.01
 5.93l3.252 1.879v8.384L12 20.387l-7.264-4.194V7.807l10.393-6zm0
 8.244-3.254 1.879v3.754h.002v.004L12 15.758l3.252-1.877v-3.76z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/BabylonJS/Brand-Toolkit/bl
ob/8583d4d9bf252a233fa480fa02ac6f367d5207a1/babylon_logo/monochrome/ba'''

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

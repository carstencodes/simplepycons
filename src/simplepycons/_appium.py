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


class AppiumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appium"

    @property
    def original_file_name(self) -> "str":
        return "appium.svg"

    @property
    def title(self) -> "str":
        return "Appium"

    @property
    def primary_color(self) -> "str":
        return "#EE376D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Appium</title>
     <path d="M11.923 0C5.937 0 .976 4.384.07 10.115a11.943 11.943 0 0
 1 7.645-2.754 11.982 11.982 0 0 1 9.43 4.58 11.942 11.942 0 0 0
 1.015-8.769 12.066 12.066 0 0 0-.626-1.772l-.003-.008A11.968 11.968 0
 0 0 11.923 0Zm7.721 2.754A12.002 12.002 0 0 1 9.398 16.521a12.082
 12.082 0 0 0 9.02 5.617c.24-.119.766-.51 1.224-.89A11.971 11.971 0 0
 0 23.995 12a11.98 11.98 0 0 0-4.35-9.247zM9.33 7.557a12.159 12.159 0
 0 0-2.647.401A11.944 11.944 0 0 0 .01
 12.595l-.005.006c.021.427.065.853.131 1.275C1.037 19.61 6 24 11.991
 24c1.45 0 2.887-.26 4.243-.773a12 12 0 0 1-6.905-15.67z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/openjs-foundation/artwork/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/openjs-foundation/artwork/
blob/270575392800eb17a02612203f6f0d5868c634a7/projects/appium/appium-i'''

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

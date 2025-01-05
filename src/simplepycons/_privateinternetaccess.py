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


class PrivateInternetAccessIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "privateinternetaccess"

    @property
    def original_file_name(self) -> "str":
        return "privateinternetaccess.svg"

    @property
    def title(self) -> "str":
        return "Private Internet Access"

    @property
    def primary_color(self) -> "str":
        return "#1E811F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Private Internet Access</title>
     <path d="M10.8078 5.7639a.812.812 0 1 0-.812.812.8115.8115 0 0 0
 .812-.812m3.196-.8115a.812.812 0 1 0 .8114.8115.812.812 0 0
 0-.8115-.8115m-.8757 2.1535a1.686 1.686 0 0 1-2.2571 0 .2106.2106 0 0
 0-.2855.3092 2.0645 2.0645 0 0 0 2.8298 0 .2108.2108 0 1
 0-.2866-.3092M11.9473 0C7.9939 0 4.789 3.2048 4.789 7.1582V8.543c0
 .0084.0016.0202.002.0293-.7826.1443-1.3781.8232-1.3888 1.6464a2.3927
 2.3927 0 0 0-.33 1.2208v9.1777a2.4154 2.4154 0 0 0 1.7851
 2.3281A1.7667 1.7667 0 0 0 6.4727 24h2.0058a1.7627 1.7627 0 0 0
 1.5762-.9668h3.6816c.3009.5943.9101.9678 1.5762.9668h2.0078a1.7718
 1.7718 0 0 0 1.5899-1c1.1652-.1914 2.02-1.2
 2.0175-2.3809v-9.1777a2.4275 2.4275 0 0
 0-.3144-1.1973v-.0098c-.001-.7739-.5211-1.423-1.2305-1.625V7.1582C19.3828
 3.2048 16.1761 0 12.2227 0Zm.0312 2.5586h.2149c2.4754 0 4.4824 2.005
 4.4824 4.4805V8.543H15.668a1.6666 1.6666 0 0
 0-1.1739.4804H9.5273a1.675 1.675 0 0
 0-1.1836-.4804h-.8476V7.039c0-2.4754 2.007-4.4804
 4.4824-4.4804zm.0254 9.4922v.0039a1.9739 1.9739 0 0 1 1.1055
 3.6035.3126.3126 0 0 0-.1328.2988l.4863 3.2969a.307.307 0 0
 1-.0703.2461.3137.3137 0 0 1-.2344.1074h-2.3164a.3097.3097 0 0
 1-.3047-.3535l.4844-3.2969a.2934.2934 0 0 0-.129-.2949 1.975 1.975 0
 0 1 .8848-3.5976 2.176 2.176 0 0 1 .2266-.0137z" />
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
        yield from [
            "PIA",
        ]

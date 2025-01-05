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


class LetsEncryptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "letsencrypt"

    @property
    def original_file_name(self) -> "str":
        return "letsencrypt.svg"

    @property
    def title(self) -> "str":
        return "Let's Encrypt"

    @property
    def primary_color(self) -> "str":
        return "#003A70"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Let's Encrypt</title>
     <path d="M11.9914 0a.8829.8829 0 00-.8718.817v3.0209A.8829.8829 0
 0012 4.7207a.8829.8829 0 00.8803-.8803V.817a.8829.8829 0
 00-.889-.817zm7.7048 3.1089a.8804.8804 0 00-.5214.1742l-2.374
 1.9482a.8804.8804 0 00.5592 1.5622.8794.8794 0
 00.5592-.2001l2.3714-1.9506a.8804.8804 0
 00-.5944-1.534zm-15.3763.0133a.8829.8829 0 00-.611 1.5206l2.37
 1.9506a.876.876 0 00.5606.2001v-.002a.8804.8804 0
 00.5597-1.5602L4.8277 3.2831a.8829.8829 0 00-.5078-.161zm7.6598
 3.2275a5.0456 5.0456 0 00-5.0262 5.0455v1.4876H5.787a.9672.9672 0
 00-.9647.9643v9.1887a.9672.9672 0 00.9647.9643H18.213a.9672.9672 0
 00.9643-.9643v-9.1907a.9672.9672 0
 00-.9643-.9623h-1.1684v-1.4876a5.0456 5.0456 0
 00-5.0649-5.0455zm.0127 2.8933a2.1522 2.1522 0 012.1593
 2.1522v1.4876H9.8473v-1.4876a2.1522 2.1522 0
 012.145-2.1522zm7.3812.5033a.8829.8829 0 10.0705
 1.7632h3.0267a.8829.8829 0 000-1.7609H19.444a.8829.8829 0
 00-.0705-.0023zm-17.8444.0023a.8829.8829 0 000
 1.7609h2.9983a.8829.8829 0 000-1.7609zm10.4596 6.7746a1.2792 1.2792 0
 01.641 2.3926v1.2453a.6298.6298 0 01-1.2595 0v-1.2453a1.2792 1.2792 0
 01.6185-2.3926z" />
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

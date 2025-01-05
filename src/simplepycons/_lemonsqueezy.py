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


class LemonSqueezyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lemonsqueezy"

    @property
    def original_file_name(self) -> "str":
        return "lemonsqueezy.svg"

    @property
    def title(self) -> "str":
        return "Lemon Squeezy"

    @property
    def primary_color(self) -> "str":
        return "#FFC233"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lemon Squeezy</title>
     <path d="m7.4916 10.835 2.3748-6.5114a3.1497 3.1497 0 0
 0-.065-2.3418C9.0315.183 6.9427-.398 5.2928.265 3.643.929 2.71 2.4348
 3.512 4.3046l2.8197 6.5615c.219.509.97.489 1.16-.03m1.6798 1.0969
 6.5334-2.7758c2.1699-.9219 2.7218-3.6907
 1.022-5.2905l-.068-.063c-1.6669-1.5469-4.4217-1.002-5.3706
 1.0359L8.3566 11.135c-.234.503.295 1.0199.8159.7979m.373.87
 6.6454-2.5119c2.2078-.8349 4.6206.745 4.5886 3.0398l-.002.09c-.048
 2.2358-2.3938 3.7376-4.5536 2.9467l-6.6724-2.4418a.595.595 0 0
 1-.006-1.1229m-.386 1.9269 6.4375 2.9767a3.2997 3.2997 0 0 1 1.6658
 1.6989c.769 1.7998-.283 3.6396-1.9328
 4.3016-1.6499.662-3.4097.235-4.2097-1.6359l-2.8027-6.5694c-.217-.509.328-1.009.8419-.772"
 />
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

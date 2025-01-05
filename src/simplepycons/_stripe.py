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


class StripeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stripe"

    @property
    def original_file_name(self) -> "str":
        return "stripe.svg"

    @property
    def title(self) -> "str":
        return "Stripe"

    @property
    def primary_color(self) -> "str":
        return "#635BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stripe</title>
     <path d="M13.976 9.15c-2.172-.806-3.356-1.426-3.356-2.409
 0-.831.683-1.305 1.901-1.305 2.227 0 4.515.858 6.09
 1.631l.89-5.494C18.252.975 15.697 0 12.165 0 9.667 0 7.589.654 6.104
 1.872 4.56 3.147 3.757 4.992 3.757 7.218c0 4.039 2.467 5.76 6.476
 7.219 2.585.92 3.445 1.574 3.445 2.583 0 .98-.84 1.545-2.354
 1.545-1.875 0-4.965-.921-6.99-2.109l-.9 5.555C5.175 22.99 8.385 24
 11.714 24c2.641 0 4.843-.624 6.328-1.813 1.664-1.305 2.525-3.236
 2.525-5.732 0-4.128-2.524-5.851-6.594-7.305h.003z" />
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

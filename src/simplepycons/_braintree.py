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


class BraintreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "braintree"

    @property
    def original_file_name(self) -> "str":
        return "braintree.svg"

    @property
    def title(self) -> "str":
        return "Braintree"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Braintree</title>
     <path d="M8.276 20.482h4.717c3.641 0 5.462-1.2 5.462-3.517
 0-2.275-1.945-3.517-5.752-3.517H8.276Zm0-16.965v6.538h4.138c3.103 0
 4.717-1.159 4.717-3.269 0-2.152-1.655-3.269-4.759-3.269zM1.696
 24v-3.518H4.47V3.517H1.697V0h11.089c5.09 0 8.193 2.358 8.193 6.455 0
 2.69-1.572 4.345-3.558 5.131 2.855.787 4.882 2.814 4.882 5.586 0
 4.386-3.393 6.828-8.938 6.828H1.697" />
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

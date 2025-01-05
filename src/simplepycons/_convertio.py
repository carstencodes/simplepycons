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


class ConvertioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "convertio"

    @property
    def original_file_name(self) -> "str":
        return "convertio.svg"

    @property
    def title(self) -> "str":
        return "Convertio"

    @property
    def primary_color(self) -> "str":
        return "#FF3333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Convertio</title>
     <path d="M12 .037C5.373.037 0 5.394 0 12c0 6.606 5.373 11.963 12
 11.963 6.628 0 12-5.357 12-11.963C24 5.394 18.627.037 12 .037zm-.541
 4.8c1.91-.13 3.876.395 5.432 1.934 1.426 1.437 2.51 3.44 2.488
 5.317h2.133l-4.444
 4.963-4.445-4.963h2.313c-.001-1.724-.427-2.742-1.78-4.076-1.325-1.336-2.667-2.11-4.978-2.303a9.245
 9.245 0 013.281-.871zM6.934 6.95l4.445 4.963H9.066c0 1.724.426 2.742
 1.778 4.076 1.326 1.336 2.667 2.112 4.978 2.305-2.684 1.268-6.22
 1.398-8.71-1.064-1.427-1.437-2.512-3.44-2.489-5.317H2.488L6.934
 6.95Z" />
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

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


class CakephpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cakephp"

    @property
    def original_file_name(self) -> "str":
        return "cakephp.svg"

    @property
    def title(self) -> "str":
        return "CakePHP"

    @property
    def primary_color(self) -> "str":
        return "#D33C43"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CakePHP</title>
     <path d="M0 13.875v3.745c0 2.067 5.37 3.743 12 3.743V17.62c-6.63
 0-12-1.68-12-3.743v-.002zm21.384 2.333L12 13.875v3.745l9.384
 2.333C23.02 19.313 24 18.503 24 17.62v-3.745c0 .882-.98 1.692-2.616
 2.333zM12 10.133v3.742c-6.627 0-12-1.677-12-3.744V6.38c0-2.064
 5.37-3.743 12-3.743 6.625 0 12 1.68 12 3.744v3.75c0 .883-.98
 1.69-2.616 2.334L12 10.13v.003z" />
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

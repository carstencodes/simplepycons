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


class QaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qase"

    @property
    def original_file_name(self) -> "str":
        return "qase.svg"

    @property
    def title(self) -> "str":
        return "Qase"

    @property
    def primary_color(self) -> "str":
        return "#4F46DC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qase</title>
     <path d="M23.85
 18.994s-.802.46-1.795.28c-.19-.03-.37-.1-.551-.19a11.768 11.768 0 0 0
 2.367-7.088C23.87 5.428 18.525.1 11.935.1S0 5.428 0 11.996c0 6.568
 5.346 11.897 11.935 11.897 2.087 0 4.042-.54 5.747-1.47.562.59 1.344
 1.21 2.297 1.4 1.796.34 3.1-.48
 3.631-1.58.451-.96.482-2.1.24-3.249m-11.925-.13c-3.79
 0-6.88-3.079-6.88-6.858 0-3.779 3.09-6.858 6.88-6.858 3.792 0 6.89
 3.07 6.89 6.848 0 1.16-.29 2.26-.812
 3.22-.15-.19-.28-.37-.37-.49-.352-.48-.713-.97-1.064-1.47-.461-.65-1.524-1.95-2.989-2.23-1.795-.34-3.099.48-3.63
 1.58-.452.96-.482 2.1-.251 3.239 0 0 .802-.46 1.795-.28.722.13
 1.404.68 2.277 1.76.07.09.371.49.772 1.01-.802.34-1.685.53-2.618.53"
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

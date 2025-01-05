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


class AlamyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alamy"

    @property
    def original_file_name(self) -> "str":
        return "alamy.svg"

    @property
    def title(self) -> "str":
        return "Alamy"

    @property
    def primary_color(self) -> "str":
        return "#00FF7B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alamy</title>
     <path d="M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0
 12s5.373 12 12 12Zm.058-18.533c2.515 0 3.482 1.404 3.482 3.959v7.04c0
 .78 0 1.21.193 1.872H13.47c-.406-.331-.503-1.072-.503-1.423-.464
 1.111-1.102 1.618-2.224 1.618-1.354 0-2.476-1.014-2.476-3.257 0-2.626
 1.618-3.566 2.956-4.343.937-.545 1.736-1.009 1.744-1.917
 0-.858-.29-1.15-.909-1.15-.696 0-.987.468-.987
 1.56v.429H8.5v-.37c0-2.614 1.006-4.018 3.559-4.018Zm-.213 10.667c.6 0
 .948-.526 1.122-.8v-3.393c-.209.345-.544.621-.887.904-.608.5-1.24
 1.023-1.24 1.983 0 .838.367 1.306 1.005 1.306Z" />
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
